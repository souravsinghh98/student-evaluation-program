from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
score = 0
count = 0
def home(request):
    global score
    global count
    score = 0
    count = 0
    subjects = Subject.objects.all()
    context = {'subjects':subjects}
    return render(request,'quiz/home.html', context)

@login_required(login_url='login')
def nextQues(request,pk):
    subject = Subject.objects.get(id=pk)
    user = Profile.objects.get(user = request.user)
    user.subjects.add(subject)
    question = Question.objects.filter(subject__name=subject)
    paginator = Paginator(question, 1) #showing 1 ques per page
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {'question':page_obj}
    return render(request,'quiz/test.html',context)

@login_required(login_url='login')
def saveSelected(request,pk):
    global score
    global count
    if request.method=='POST':
        selected = request.POST['option']
        print(selected)
        count += 1
        correct_ans = Question.objects.get(id=pk)
        print(correct_ans.correct)
        if selected == correct_ans.correct:
            score += 1
    return redirect(request.META['HTTP_REFERER']) #ye bht important hai, same page pr redirect krne ke liye use kiya h

@login_required(login_url='login')
def result(request):
    global score
    global count
    total = len(Question.objects.filter(subject__name='Python'))
    return render(request,'quiz/result.html',{'score':score,'count':count,'total':total})


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save() 
                Profile.objects.create(
                    user = user
                )
                messages.success(request,'User created successfully')
                return redirect('login')
        else:
            pass
    context = {'form':form}
    return render(request,'quiz/register.html', context)   

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            uname = request.POST['uname']
            pwd = request.POST['pwd']
            user = authenticate(request, username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')    


    return render(request,'quiz/login.html')

def signout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def userProfile(request):
    profile = Profile.objects.get(user=request.user)
    subject = profile.subjects.all()
    context = {'profile':profile, 'subjects':subject}
    return render(request,'quiz/profile.html',context)

@login_required(login_url='login')
def updateProfile(request):
    curr_user = request.user
    form = ProfileUpdateForm(instance=curr_user)
    if request.method=='POST':
        form = ProfileUpdateForm(request.POST, instance=curr_user)
        if form.is_valid():
            form.save()
            messages.info(request,' Profile Updated!!')
            return redirect('profile')
    context = {'form':form}
    return render(request,'quiz/updateProfile.html', context)  

@login_required(login_url='login')
def changePic(request):
    curr_user = Profile.objects.get(user=request.user)
    form = ProfilePicForm(instance = curr_user)
    if request.method=='POST':
        form = ProfilePicForm(request.POST, request.FILES, instance=curr_user)
        if form.is_valid():
            form.save()
            messages.info(request,'Pic changed')
            return redirect('profile')
    context = {'form':form}
    return render(request, 'quiz/profilePic.html', context)        





