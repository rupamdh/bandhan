from django.shortcuts import render, redirect
from exam.models import Answer
from .models import *
from django.contrib import messages


# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def get_user_details(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        try: 
            answer = Answer.objects.get(email=email)
            if answer is not None:
                messages.error(request, 'You Already Submitted The Answers')
                return redirect('home')
        except Answer.DoesNotExist:
            request.session['name'] = name
            request.session['email'] = email
            return redirect('exam')
        

def winners_page(request):
    winners = Winner.objects.filter(status=True)

    context = {
        'winners': winners,
    }
    return render(request, 'weekly-winner.html', context)