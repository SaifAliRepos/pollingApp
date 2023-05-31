from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice


def home(request):
    return render(request, 'base.html')

def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)

def show(request, question_id):
    try:
        question_with_choices = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesnt exist")
    return render(request, 'polls/show.html', {'question_with_choices': question_with_choices})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/show.html', {
            'question_with_choices': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:show', args=(question.id,)))

