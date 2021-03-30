from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('create_task/', views.create_request, name='create-request'),  # создать заявку
    #path('upload_file/', views.simple_upload),
]
