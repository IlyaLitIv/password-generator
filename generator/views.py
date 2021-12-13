from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    char = list('aeiouybcdfghjklmnpqrstvwxz')

    if request.GET.get('uppercase'):
        char.extend(list('AEIOUYBCDFGHJKLMNPQRSTVWXZ'))
    if request.GET.get('numbers'):
        char.extend(list('0123456789'))
    if request.GET.get('special'):
        char.extend(list('!#$%&*+,-./:;<=>?@[\]^_'))

    length = int(request.GET.get('length', 12))
    the_password = ''
    for i in range(length):
        the_password += random.choice(char)

    return render(request, 'generator/password.html', {'password': the_password})

def about(request):
    return render(request, 'generator/about.html', {'about': about})
