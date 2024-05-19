from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm

urlpatterns = [
    # path('', views.base, name='base'),
    path('',views.home,name="home"),
    
    path('photoupload/', views.photoupload, name='photoupload'),
    path('wishingcard/', views.wishingcard, name='wishingcard'),
     path('download_photo_frame/<int:pk>/', views.download_photo_frame, name='download_photo_frame'),
    path('download-wishing-card/<int:pk>/', views.download_wishing_card, name='download_wishing_card'),

    


    path('dashboard/',views.dashboard, name='dashboard'),
   #  path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('ShowPhotoFrame/',views.ShowPhotoFrame,name="ShowPhotoFrame"),
       path('edit_frame/<int:frame_id>/', views.edit_frame, name='edit_frame'),
    

    path('delete_frame/<int:frame_id>/', views.delete_frame, name='delete_frame'),
    path('ShowCardDesign/',views.ShowCardDesign,name="ShowCardDesign"),
    path('ShowWishingCards',views.ShowWishingCards,name="ShowWishingCards"),

     path('add_card_design/', views.add_card_design, name='add_card_design'),
     path('add_bg_image/',views.add_bg_image,name="add_bg_image"),
]
