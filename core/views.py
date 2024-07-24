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
        password = request.POST['password']
        try: 
            answer = Answer.objects.get(email=email)
            
            if answer is not None:
                messages.error(request, 'You Already Submitted The Answers')
                return redirect('home')
        except Answer.DoesNotExist:
            get_password = Core.objects.get(id=1)
            # print(get_password)
            # print(password)
            if password == get_password.exam_password:
                request.session['name'] = name
                request.session['email'] = email
                return redirect('exam')
            else:
                messages.error(request, 'Wrong Password')
                return redirect('home')
        

def winners_page(request):
    winners = Winner.objects.filter(status=True)

    context = {
        'winners': winners,
    }
    return render(request, 'weekly-winner.html', context)