# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, "chat/index.html")
