from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
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
            
            try:
                user = User.objects.create(username=username,client_ip=request.META['REMOTE_ADDR'])
                user.set_password(raw_password)
                user.save()
                
                authenticate(username=username, password=raw_password)
                
                return redirect('login')
            except Exception as e:
                if str(e) != None and "NOT NULL constraint failed" in str(e):
                    form.add_error('username',"You already have an account here. If you believe this is a mistake, please contact the developer.")
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
            return redirect('index')
        else:
            context['error'] = 'Invalid username or password.'
            return render(request, 'login.html',context)
    
    return render(request, 'login.html',context)

def logout(request):
    auth_logout(request)
    
    return redirect('index')