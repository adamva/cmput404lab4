from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s." % question_id
    return HttpResponse(response)

def vote(request, question_id):
    response = "You're voting on question %s." % question_id
    return HttpResponse(response)
