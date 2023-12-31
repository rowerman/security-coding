from django.urls import re_path as url
from . import views

app_name = 'image'

urlpatterns = [
    url(r'^list-images/$',views.list_images,name="list_images"),
    url(r'^upload-image/$',views.upload_image,name="upload_image"),
    url(r'^del-image/$',views.del_image,name="del_image"),
    url(r'^images/$',views.falls_images,name="falls_images"),
]