""" greet.py """
from datetime import date
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(('GET',))
def greeting(request):
    return Response("hello")

def say_hello():
    return "hello"

def get_today():
    return date.today()

def function_to_get_today():
    day = get_today()
    return day
 