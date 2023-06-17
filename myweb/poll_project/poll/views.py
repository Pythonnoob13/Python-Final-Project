from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreatePollForm, CreatePollFormAdmin
from .models import Poll

def profile(request,):
    
    
    return render(request, 'poll/profile.html',)


def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)


def create(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            form = CreatePollFormAdmin(request.POST)
        else:
            form = CreatePollForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.owner = request.user.id
            question.save()
            #form.save()
            return redirect('home')
    else:
        if request.user.is_superuser:
            form = CreatePollFormAdmin
        else:
            form = CreatePollForm
    context = {
        'form' : form
    }
    return render(request, 'poll/create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)

@login_required
def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)

def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'poll_list.html', {'polls': polls})

def search_for(request):
    if request.method == "POST":
        searched = request.POST['searched']
        questions = Poll.objects.filter(question__contains= searched)
        return render(request,'poll/search_for.html', {
            'searched': searched,
            'questions':questions,
        })
    else:
        return render(request,'poll/search_for.html', {})
    
def questions(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/questions.html', context)

def update_question(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    form = CreatePollForm(request.POST or None, instance=poll)
    if form.is_valid():
        form.save()
        return redirect('questions')


    context = {
        'poll' : poll,
        'form':form
    }
    return render(request, 'poll/update_questions.html', context)


def delete_question(request, poll_id):
        if request.user.is_superuser:
            poll = Poll.objects.get(pk=poll_id)
            poll.delete()
            messages.success(request, ("Question Deleted!!"))

            return redirect('questions')
        else:
            messages.success(request, ("You Aren't Authorized To Delete This Poll!"))
            return redirect('questions')	
            



