from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .forms import AskForm, AnswerForm
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
    limit = 5
    page = request.GET.get('page', 1)
    paginator = Paginator(popular_question_list, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    context = {'popular_question_list': page,
               'paginator': paginator,
               'page': page}
    return render(request, 'qa/popular.html', context)


def get_question_by_id(request, question_id):
    context = {}
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = Question.get_url(question_id)
            return HttpResponseRedirect(url)
    else:
        question = get_object_or_404(Question, pk=question_id)
        context['question'] = question
        context['answers'] = question.answer_set.all()
        form = AnswerForm()
        form.fields.get('question').queryset = Question.objects.filter(pk=question_id)
        context['form'] = form
        return render(request, 'qa/question.html', context)


def index():
    pass


def add_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = Question.get_url(question.id)
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        context = {'form': form}
        return render(request, 'qa/question_form.html', context)
