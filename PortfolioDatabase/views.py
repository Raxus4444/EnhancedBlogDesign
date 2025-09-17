from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Hobby, Portfolio
from django.template import loader

# Create your views here.
def home(request):
    context = {}
    return render(request, 'index.html', context)
def hobbies(request):
    hobby_list = Hobby.objects.all()
    context = {
        'hobby_list' : hobby_list,
    }
    return render(request, 'hobbies.html', context)

def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list' : portfolio_list,
    }
    return render(request, 'portfolio.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def hobby_detail(request, hobby_id):
    hobby = Hobby.objects.get(pk=hobby_id)
    context = {
        'hobby' : hobby,
    }
    return render(request, 'hobby_details.html', context)

def portfolio_detail(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    context = {
        'portfolio' : portfolio,
    }
    return render(request, 'portfolio_details.html', context)