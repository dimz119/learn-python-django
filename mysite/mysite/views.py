from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

def index(request):
    return render(request, 'main.html')

def error_404_view(request, exception):
    # return HttpResponseNotFound("The page is not found!")
    return render(request, '404.html')

def error_500_view(request):
    return render(request, '500.html')
