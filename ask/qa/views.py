from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Question


def latest_questions(request):
    latest_question_list = Question.objects.new()
    limit = 5
    page = request.GET.get('page', 1)
    paginator = Paginator(latest_question_list, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    context = {'latest_question_list': page,
               'paginator': paginator,
               'page': page}
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
