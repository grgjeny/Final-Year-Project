from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
        path('',views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('events/', views.events, name='events'),   
    path('explore/', views.explore, name='explore'),   
    path('items/<int:Items_id>', views.items, name='items'),   
    path('blog/', views.blog, name='blog'),   
    path('posts/<int:Blog_id>', views.posts, name='posts'),   
    path('eventsdetails/<int:Events_id>', views.eventsdetails, name='eventsdetails'),   

]