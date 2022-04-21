from django.shortcuts import render, HttpResponse, redirect
from .models import *
import random
# Create your views here.
def index(request):
    # calculate total questions
    questions = Question.objects.all()
    total_questions = len(questions)

    # calculate total solved
    solved_questions = Question.objects.filter(solved=True)
    total_solved = len(solved_questions)
    return render(request, 'index.html', {"total_questions": total_questions, "total_solved": total_solved})

# random question by ds
def random_ds(request, ds):
    questions = Question.objects.all()
    questions_list = []
    for question in questions:
        if question.ds.name == ds and question.solved == True:
            questions_list.append(question.link)
    lucky = random.choice(questions_list)
    return redirect(lucky)