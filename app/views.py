from django.http import HttpResponse
from django.shortcuts import render
from .models import Review

# Create your views here.


def index(req):
    return render(req, 'index.html')


def clients(req):
    return render(req, 'clients.html')


def reviews(req):
    reviews = Review.objects.all()
    return render(req, 'reviews.html', {'reviews': reviews})


def career(req):
    return render(req, 'career.html')


def contact(req):
    return render(req, 'contact.html')
