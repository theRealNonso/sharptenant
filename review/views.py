from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.contrib.auth.decorators import login_required
import review.models as rm
import review.forms as rf
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = rf.RegisterForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_form.set_password(password)
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('review')

    else:
        form = rf.RegisterForm()
    return render(request, 'review/signup.html', {'form': form})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('write-review')
        return redirect('write-review')        
    else:
        form = rf.LoginForm()
        return render(request, 'review/login.html', {'form': form})

def userlogout(request):
    logout(request)
    return redirect('/')

def index(request):
    recent_review = rm.Review.objects.all().order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(recent_review, 10)
    try:
        review = paginator.page(page)
    except PageNotAnInteger:
        review = paginator.page(1)
    except EmptyPage:
        review = paginator.page(paginator.num_pages)
    form = rf.SearchForm()
    return render(request, 'review/index.html', 
                  {'form': form, 'review':review})


def searchReview(request):
    if request.method == 'POST':
        number = request.POST['number']
        address = request.POST['address']
        location = request.POST['location']
        recent_review = rm.Review.objects.filter(location__icontains=location,
                                                     street_name__icontains=address,
                                                     house_number__icontains=number)
        page = request.GET.get('page', 1)
        paginator = Paginator(recent_review, 16)
        try:
            review = paginator.page(page)
        except PageNotAnInteger:
            review = paginator.page(1)
        except EmptyPage:
            review = paginator.page(paginator.num_pages)
        form = rf.SearchForm(request.POST)
        if form.is_valid():
            context = {'review': recent_review}
            return render(request, 'review/review.html', context)
        else:
            form = rf.SearchForm()
        return render(request, 'index.html', {'form':form})
    else:
        form = rf.SearchForm()
        return render(request, 'index.html', {'form':form})

@login_required(login_url='login')
def writeReview(request):
    if request.method == 'POST':
        user = rm.User.objects.all()
        form = rf.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return HttpResponseRedirect('review')
        else:
            print(form.errors)
            form = rf.ReviewForm()
        return render(request, 'review/new-post.html', {'form':form})
    else:
        form = rf.ReviewForm()
        return render(request, 'review/new-post.html', {'form': form})


def review(request):
    review = rm.Review.objects.all()
    if request.method == 'GET':
        return render(request, 'review/review.html', {'review':review})
    else:
        return render(request, 'review/review.html', {'review':review})

def about(request):
    return render(request, 'review/about.html')


def detailReview(request, id):
    review = rm.Review.objects.get(id=id)
    context = {'review': review}
    return render(request, 'review/reviewSingle.html',context)




