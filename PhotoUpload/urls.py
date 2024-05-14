from django.urls import path
from . import views

urlpatterns = [
    # path('', views.base, name='base'),
    path('home/',views.home,name="home"),
    path('photoupload/', views.photoupload, name='photoupload'),
    path('wishingcard/', views.wishingcard, name='wishingcard'),
    path('download_photo_frame/<int:pk>/', views.download_photo_frame, name='download_photo_frame'),
    path('download-wishing-card/<int:pk>/', views.download_wishing_card, name='download_wishing_card'),

    # path('photo_frame_preview/', views.photo_frame_preview, name='photo_frame_preview'),
]
