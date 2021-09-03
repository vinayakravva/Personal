from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from django.http import HttpResponse
from .models import CreateUserform
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@login_required(login_url='login')
def home(request):
    courses=Course.objects.all()
    context={'courses':courses}
    return render(request,'quiz/home.html',context)

def api_question(request,id):
    raw_questions=Question.objects.filter(course=id)[:20]
    
    questions=[]
    for raw_question in raw_questions:
        question={}
        question['id']=raw_question.id
        question['question']=raw_question.question
        question['answer']=raw_question.answer
        question['marks']=raw_question.marks
        options=[]
        options.append(raw_question.option_one)
        options.append(raw_question.option_two)
        if raw_question.option_three !='':
            options.append(raw_question.option_three)
        if raw_question.option_four !='':
            options.append(raw_question.option_four)
        question['options']=options
        questions.append(question)
    return JsonResponse(questions,safe=False)

def take_quiz(request,id):
    context={'id':id}
    return render(request,'quiz/quiz.html',context)

    
@login_required(login_url='login')
def view_score(request):
    user=request.user
    score=ScoreBoard.objects.filter(user=user)
    context={'score':score}

    return render(request,'quiz/score.html',context)

@csrf_exempt
def check_score(request):
    data=json.loads(request.body)
    user=request.user
    course_id=data.get('course_id')
    solutions=json.loads(data.get('data'))
    course=Course.objects.get(id=course_id)
    score=0
    for solution in solutions:
        question=Question.objects.filter(id=solution.get('question_id')).first()
        if question.answer==solution.get('option'):
            score=score+question.marks
    
    score_board=ScoreBoard(course=course,score=score,user=user)
    score_board.save()
    return JsonResponse({'message':'success','status':True})




#Login/Logout/Registration
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        try:
            if request.method == 'POST':
                form = CreateUserform(request.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request,f'Account created for {username}!')
                    return redirect('login')
            else:
                form=CreateUserform()
                return render(request, 'users/register.html',{'form':form})
        except ValueError:
            form=CreateUserform()
            return render(request, 'users/register.html',{'form':form})



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('blog-home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username OR Password is Incorrect')
                return render(request,'users/login.html')
        
        context={}
        return render(request,'users/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')




    