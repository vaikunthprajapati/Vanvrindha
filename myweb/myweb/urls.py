from .views import *
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
from master.urls import producturls

urlpatterns = [
    path('', front), 
    path('master/', include(producturls),name='master'),
    path('front', front, name='front'),
    path('homepage', homepage, name='homepage'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('logout', logoutUser, name='logout'),
    path('founder', founder, name='founder'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
