from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q 
# Create your views here.

def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='Cricket')
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='Cricket')
    QSW=Webpage.objects.exclude(topic_name='Cricket')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.filter(topic_name='Kabaddi').order_by('-name')
    QSW=Webpage.objects.all().order_by(Length('name'))
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__contains='s')
    QSW=Webpage.objects.filter(name__regex='\w{6}')
    QSW=Webpage.objects.filter(name__in=['virat','chitra'])
    QSW=Webpage.objects.filter(Q(topic_name='Rugby') & Q(url__startswith='https'))
    QSW=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name='chitra'))

    
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)   

def display_access(request):
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.filter(date='2001-6-26')
    QSA=AccessRecords.objects.filter(date__gt='1992-08-18')
    QSA=AccessRecords.objects.filter(date__gte='2001-06-26')
    QSA=AccessRecords.objects.filter(date__lte='2001-06-26')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__year='2018')
    QSA=AccessRecords.objects.filter(date__day='23')
    QSA=AccessRecords.objects.filter(date__year__gt='2015')
    d={'access':QSA}
    return render(request,'display_access.html',d)    