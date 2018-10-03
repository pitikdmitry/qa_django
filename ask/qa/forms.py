from django import forms
from datetime import datetime

from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

    # def clean_title(self):
    #     pass
    #
    # def clean_text(self):
    #     pass

    def clean(self):
        added_at = self.cleaned_data.get('added_at')
        if added_at is None:
            self.cleaned_data['added_at'] = datetime.now()


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

    def clean(self):
        added_at = self.cleaned_data.get('added_at')
        if added_at is None:
            self.cleaned_data['added_at'] = datetime.now()
