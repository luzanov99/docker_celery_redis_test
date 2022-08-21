from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from ticket.celery import app
from .tasks import task12
 
@app.task

def get_task(request):

    task12.delay()
    return HttpResponse('das')