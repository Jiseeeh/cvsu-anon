from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model

from .models import Message
from .forms import RegisterForm


# Create your views here.
def index(request):
    return render(request, 'index.html',{'show_nav':False})

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            User = get_user_model()
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            user = User.objects.create(username=username)
            user.set_password(raw_password)
            user.save()
            
            authenticate(username=username, password=raw_password)
            
            return redirect('login')
    else:
        form = RegisterForm()
        
    context = {
        'form':form,
        'show_nav':False,
    }
    return render(request, 'register.html',context)

def login(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    
    context = {
        'show_nav':False,
        'error':''
    }
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            context['error'] = 'Invalid username or password.'
            return render(request, 'login.html',context)
    
    return render(request, 'login.html',context)

def logout(request):
    auth_logout(request)
    
    return redirect('index')

def send_anon(request,username):
    logged_user = request.user
    receiver = None
    context = {
        'show_nav':True,
        'username':username,
        'error':'',
        'success':'',
    }
    
    # check if user is sending to himself/herself
    if username == logged_user.username:
        context['error'] = 'You cannot send a message to yourself.'
        return render(request, 'send_anon.html',context)
    
    # check if there is a user with the given username to be sent to
    try:
        
        receiver = get_user_model().objects.get(username=username)
    except:
        context['error'] = 'User does not exist.'
        return render(request, 'send_anon.html',context)
    
    if request.method == 'POST':
        
        # if authenticated, increment user ray_points by 1, otherwise just create a message
        if request.user.is_authenticated:
            User = get_user_model()
        
            User.objects.filter(username=logged_user.username).update(ray_points=logged_user.ray_points + 1)
            
            # create a message
            Message.objects.create(receiver_id=receiver,message=request.POST.get('message').strip())
        else:
            Message.objects.create(receiver_id=receiver,message=request.POST.get('message').strip())
            
        context['success'] = f"Message sent to {username}."
        # increment receiver's ray_points by 5
        get_user_model().objects.filter(username=receiver.username).update(ray_points=receiver.ray_points + 5)
            
        
    return render(request, 'send_anon.html',context)


def dashboard(request):
    
    if not request.user.is_authenticated:
        return redirect('register')
    
    logged_user = request.user;
    messages = Message.objects.filter(receiver_id=logged_user)
        
    return render(request, 'dashboard.html',{'show_nav':True,'messages':messages, 'user':logged_user})

def homepage(request):
    # get top three users with the most ray_points, excluding 0 ray_points
    top_users = get_user_model().objects.filter(ray_points__gt=0).order_by('-ray_points')[:3]
    
    return render(request, 'homepage.html',{'show_nav':True,'top_users':top_users})