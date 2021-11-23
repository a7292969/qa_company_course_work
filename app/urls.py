from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.clients, name='clients'),
    path('reviews', views.reviews, name='reviews'),
    path('career', views.career, name='career'),
    path('contact', views.contact, name='contact'),
]