from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import get_user_model
from django.urls import path

User = get_user_model()
# Create your views here.
def exam_page(request):
    questions = Question.objects.filter(status=True)

    if 'name' in request.session and 'email' in request.session:
        name = request.session['name']
        email = request.session['email']
        answer = {}
        if request.method == 'POST':
            for question in questions:
                answer[question.id] = request.POST.get(f'q_{question.id}')
            Answer.objects.create(
                name=name,
                email=email,
                ans=str(answer)
            )
            del request.session['name']
            del request.session['email']
            return redirect('thank-you')
    else:
        return redirect('home')
    
    context = {
        'name': name,
        'email': email,
        'questions' : questions
    }
    return render(request, 'exam.html', context)

def thank_you(request):
    
    return render(request, 'thank-you.html')
