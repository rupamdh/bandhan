from .models import Answer

def get_answers(request):
    answers = Answer.objects.all()

    context = {
        'answers' : answers
    }
    return context
    