from django.shortcuts import render,redirect,HttpResponse
from .forms import PhotoFrameForm,WishingCardForm
from .models import PhotoFrame,WishingCard
from PIL import Image

def base(request):
    return render(request, 'PhotoUpload/base.html')

def home(request):
    return render(request,'PhotoUpload/home.html')

def photoupload(request):
    if request.method == 'POST':
        form = PhotoFrameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photoupload')
    else:
        form = PhotoFrameForm()
    
    photo_frames = PhotoFrame.objects.all()
    return render(request, 'PhotoUpload/photoupload.html', {'form': form, 'photo_frames': photo_frames})




    

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
        card_design_path = photo_frame.card_design.path
        combined_image = merge_images(image_path, card_design_path)
        combined_image_path = 'combined_photo_frame.png'
        combined_image.save(combined_image_path)

        with open(combined_image_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/png')
            response['Content-Disposition'] = f'attachment; filename="{photo_frame.name}.png"'
        return response
    except Exception as e:
        return HttpResponse(str(e), status=404)







from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import tempfile




def wishingcard(request):
    latest_wishing_card = WishingCard.objects.order_by('-id').first()

    if request.method == 'POST':
        form = WishingCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            latest_wishing_card = form.instance  # Update the latest wishing card
            return redirect('wishingcard')
    else:
        form = WishingCardForm()
    
    return render(request, 'PhotoUpload/wishingcard.html', {'form': form, 'wishing_card': latest_wishing_card})




def download_wishing_card(request, pk):
    wishing_card = WishingCard.objects.get(pk=pk)
    image_path = wishing_card.background_image.path


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
   