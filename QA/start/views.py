
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, render, redirect
from start import forms
from start.models import Answer, Question

def home(request):
    return render(request, 'index.html', {
    'questions': Question.objects.all()
})

def question(request, id):
    quest = Question.objects.get(pk=id)

    AnswerFormSet = forms.AnswerForm
    data = {'form': AnswerFormSet, 'quest': quest}
    if request.method == 'POST':
        formset = AnswerFormSet(request.POST)
        if formset.is_valid():
            post = formset.cleaned_data['post']
            answerer = formset.cleaned_data['answerer']
            answer = quest
            Answer.objects.create(post=post, answerer=answerer, answer=answer)
            return redirect('//')
        else:
            return render(request, "questionview.html", context=data)
    else:
        return render(request, "questionview.html", context=data)

def questioncreate(request):
    QuestionFormSet = forms.QuestionForm
    data = {'form': QuestionFormSet}
    if request.method == 'POST':
        formset = QuestionFormSet(request.POST)
        if formset.is_valid():
            poster = formset.cleaned_data['poster']
            title = formset.cleaned_data['title']
            content = formset.cleaned_data['content']
            Question.objects.create(poster=poster, title=title, content=content)
            return redirect('//')
        else:
            return render(request, "createquestion.html", data)
    else:
        return render(request, "createquestion.html", data)