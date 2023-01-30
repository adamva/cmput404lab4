from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    response = "Hello, world. You're at the polls index."
    return HttpResponse(response)

def detail(request, question_id):
    response = "You're looking at question %s." % question_id
    return HttpResponse(response)

def results(request, question_id):
    response = "You're looking at the results of question %s." % question_id
    return HttpResponse(response)

def vote(request, question_id):
    response = "You're voting on question %s." % question_id
    return HttpResponse(response)
