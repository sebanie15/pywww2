from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_views(request):
    return HttpResponse('Hello World!')
    