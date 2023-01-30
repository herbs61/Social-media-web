from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return HttpResponse("user authenticated and logged in")
            else:
                return HttpResponse('Invalid credentials')
                
    else:   
        form = LoginForm()
    return render(request,'users/login.html',{'form':form})

@login_required
def index(request):
    return render (request, 'users/index.html')

# Creating a registration form in view
def register(request):
    # This if statement saves the users details after he/she inputs his password
    #It does not save the details if just the name and other details are passed
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'users/register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request,'users/register.html',{'user_form':user_form})
        