from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import WishingCardForm
from .models import PhotoFrame,WishingCard,CardDesign,BgImage
from PIL import Image
from django.contrib.auth import logout
from django.http import JsonResponse

def base(request):
    return render(request, 'PhotoUpload/base.html')

def home(request):
    return render(request,'PhotoUpload/home.html')



def photoupload(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        card_design_id = request.POST.get('card_design')
        card_design = CardDesign.objects.get(pk=card_design_id)
        PhotoFrame.objects.create(image=image, card_design=card_design)
        return redirect('photoupload')
    else:
        card_designs = CardDesign.objects.all()
        latest_photo_frame = PhotoFrame.objects.order_by('-id').first()
        return render(request, 'PhotoUpload/photoupload.html', {'card_designs': card_designs, 'latest_photo_frame': latest_photo_frame})




def merge_images(image_path, card_design_path):
    image = Image.open(image_path)
    card_design = Image.open(card_design_path)
    card_design_resized = card_design.resize(image.size)
    combined_image = Image.new('RGB', image.size)
    combined_image.paste(image, (0, 0))
    combined_image.paste(card_design_resized, (0, 0), mask=card_design_resized)
    return combined_image

def download_photo_frame(request, pk):
    try:
        photo_frame = PhotoFrame.objects.get(pk=pk)
        image_path = photo_frame.image.path
        card_design_path = photo_frame.card_design.card_design.path   
        combined_image = merge_images(image_path, card_design_path)
        combined_image_path = 'combined_photo_frame.png'
        combined_image.save(combined_image_path)

        with open(combined_image_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/png')
            response['Content-Disposition'] = f'attachment; filename="PhotoFrame.png"'
        return response
    except Exception as e:
        return HttpResponse(str(e), status=404)






from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import tempfile



def wishingcard(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        background_image_id = request.POST.get('background_image') 
        background_image = get_object_or_404(BgImage, pk=background_image_id)  

        WishingCard.objects.create(name=name, designation=designation, background_image=background_image)
        return redirect('wishingcard')
    else:
        background_images = BgImage.objects.all()
        latest_wishing_card = WishingCard.objects.order_by('-id').first()
        return render(request, 'PhotoUpload/wishingcard.html', {
            'background_images': background_images,
            'latest_wishing_card': latest_wishing_card,
        })



def download_wishing_card(request, pk):
    wishing_card = WishingCard.objects.get(pk=pk)
    image_path = wishing_card.background_image.background_image.path


    background_image = Image.open(image_path)
    width, height = background_image.size


    draw = ImageDraw.Draw(background_image)


    font_name = ImageFont.truetype("arialbd.ttf", 40) 
    font_designation = ImageFont.truetype("arial.ttf", 35)  


    text_name = wishing_card.name
    text_designation = wishing_card.designation
    bbox_name = draw.textbbox((0, 0), text_name, font=font_name)
    bbox_designation = draw.textbbox((0, 0), text_designation, font=font_designation)
    
  
    text_width_name = bbox_name[2] - bbox_name[0]
    text_height_name = bbox_name[3] - bbox_name[1]
    text_width_designation = bbox_designation[2] - bbox_designation[0]
    text_height_designation = bbox_designation[3] - bbox_designation[1]


    text_x_name = (width - text_width_name) / 2
    text_y_name = height * 0.8 - text_height_name / 2

    text_x_designation = (width - text_width_designation) / 2
    text_y_designation = text_y_name + text_height_name + 10  

    draw.text((text_x_name, text_y_name), text_name, fill='#FFFFFF', font=font_name)
    draw.text((text_x_designation, text_y_designation), text_designation, fill='#FFFFFF', font=font_designation)


    image_stream = BytesIO()
    background_image.save(image_stream, format='JPEG')
    image_stream.seek(0)


    response = HttpResponse(image_stream.read(), content_type='image/jpeg')

    response['Content-Disposition'] = f'attachment; filename="{wishing_card.name}.jpg"'

    return response
   





   #----------Admin Panel--------------
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login



from .models import WishingCard, PhotoFrame

@login_required
def dashboard(request):
    total_wishing_cards_uploaded = WishingCard.objects.count()
    total_photo_frames_created = PhotoFrame.objects.count()

    context = {
        'total_wishing_cards_uploaded': total_wishing_cards_uploaded,
        'total_photo_frames_created': total_photo_frames_created,
    }

    return render(request, 'dist/dashboard.html', context)


@login_required
def profile(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'dist/profile.html', {'user': user})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard after successful login
    else:
        form = CustomAuthenticationForm()
    return render(request, 'dist/login.html', {'form': form})

def ShowPhotoFrame(request):
    frames=PhotoFrame.objects.all()
    return render(request,'dist/showphotoframe.html',{"frames":frames})


def edit_frame(request, frame_id):
    frame = get_object_or_404(PhotoFrame, pk=frame_id)
    if request.method == 'POST':
        
        new_image = request.FILES.get('image')
       
        if new_image:
            frame.image = new_image
     
        name = request.POST.get('name')
        frame.name = name
        frame.save()
        return redirect('ShowPhotoFrame') 
    return render(request, 'dist/edit_frame.html', {'frame': frame})

def delete_frame(request, frame_id):
    frame = get_object_or_404(PhotoFrame, pk=frame_id)
    if request.method == 'POST':
        frame.delete()
        return JsonResponse({'message': 'Photo frame deleted successfully.'})
    return JsonResponse({'message': 'Invalid request method.'}, status=400)

def ShowCardDesign(request):
    cards=CardDesign.objects.all()
    return render(request,'dist/showcarddesign.html',{"cards":cards})

def ShowWishingCards(request):
    wishes=WishingCard.objects.all()
    return render(request,'dist/showwishingcards.html',{"wishes":wishes})

def logout_view(request):
    logout(request)
    return redirect('home')


from django.contrib import messages

def add_card_design(request):
    new_card_design = None
    if request.method == 'POST' and request.FILES.get('card_design'):
        card_design = request.FILES['card_design']
        new_card_design = CardDesign.objects.create(card_design=card_design)
        messages.success(request, 'Card design added successfully.')
        return redirect('add_card_design')  # Redirect to the same page after processing the POST request

    return render(request, 'dist/add_card_design.html', {'error': 'No file uploaded.' if request.method == 'POST' else '', 'new_card_design': new_card_design})

def add_bg_image(request):
    new_bg_image = None
    if request.method == 'POST' and request.FILES.get('bg_image'):
        bg_image = request.FILES['bg_image']
        new_bg_image = BgImage.objects.create(background_image=bg_image)
        messages.success(request, 'Background image added successfully.')
        return redirect('add_bg_image')  # Redirect to the same page after processing the POST request
    return render(request, 'dist/add_bg_image.html', {'error': 'No file uploaded.' if request.method == 'POST' else '', 
    'new_bg_image': new_bg_image})
