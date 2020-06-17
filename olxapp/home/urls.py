from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('' , views.home , name='home') , 
    path('categories.html' , views.categories , name='categories') ,
    path('post_ad/' , views.postad , name='postad') ,
 

]