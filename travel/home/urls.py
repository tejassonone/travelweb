
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('signin/', views.sign, name='sign_in'),
    path('explore/', views.explore, name='explore'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('help/', views.help, name='help'),
    path('signin/success/', views.success, name='success'),


]