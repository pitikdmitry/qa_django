from django.shortcuts import render, get_object_or_404

from .models import Question


def latest_questions(request):
    latest_question_list = Question.objects.new()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'qa/index.html', context)


def popular_questions(request):
    popular_question_list = Question.objects.popular()
    context = {'popular_question_list': popular_question_list}
    return render(request, 'qa/popular.html', context)


def get_question_by_id(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'qa/question.html', context)


def index():
    pass
