from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='viewer_home'),
    path('next/', views.next_image, name='next_image'),
    path('prev/', views.prev_image, name='prev_image'),
    path('delete/', views.delete_image, name='delete_image'),

    path('crop/', views.crop_image, name='crop_image'),

]
