import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def not_found(request):
    return HttpResponseNotFound('<h1>Stranica nije pronađena</h1>')

## Create your views here.
def homepage(request):
    return HttpResponse('<html><body><strong> Evidencija prehrane</strong></body></html>')

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>Trenutno vrijeme: {}.</body></html>'.format(now)
    return HttpResponse(html)
