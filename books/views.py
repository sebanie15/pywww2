from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def view_books(request):
    return HttpResponse('my books')
    