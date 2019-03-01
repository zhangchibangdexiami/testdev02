from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

#首页展示所有问题
def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#查看所有问题
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

#查看投票结果
def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

#选择投票
def vote(request,question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        select_choice.votes +=1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


