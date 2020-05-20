from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse(f'Hello, People From the Earth. Stating your request:{request}')
