from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

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
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)   

def display_access(request):
    QSA=AccessRecords.objects.all()
    d={'access':QSA}
    return render(request,'display_access.html',d)    