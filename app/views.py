from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.


def insert_topic(request):
    tn=input('enter topic name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic is inserted successfully')

def insert_webpage(request):
    tn=input('enter topic_name')
    name=input('enter name')
    url=input('enter url')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    w=webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    w.save()
    return HttpResponse('webpage data is inserted')    
