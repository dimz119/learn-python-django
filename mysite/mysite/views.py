import logging
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

log = logging.getLogger(__name__)

def index(request):
    log.info(f"{__name__} index info ...")
    # log.info(f"{__name__} index info ...", extra={"user": "me"})
    return render(request, 'main.html')

def error_404_view(request, exception):
    # return HttpResponseNotFound("The page is not found!")
    return render(request, '404.html')

def error_500_view(request):
    return render(request, '500.html')
