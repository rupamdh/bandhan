from django import template
from exam.models import *
register = template.Library()

@register.filter(name='get_answers')
def get_answer_by_question(id):
    answer = Answer.objects.get(id=id)
    answers_list = [(key, value) for key, value in eval(answer.ans).items()]
        
    return answers_list

@register.filter(name='get_question_text')
def get_question_text(id):
    question = Question.objects.get(id=id)
    return question.title

