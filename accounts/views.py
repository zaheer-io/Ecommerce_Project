from django.shortcuts import render, redirect
from django.contrib import messages
from django import views

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.
class UserRegistrationView(views.View):
    template_name = 'auth/register.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form' : UserRegistrationForm()})
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('account:login')
        
        return render(request, self.template_name, {'form' : form})

class UserLoginView(views.View):
    template_name = 'auth/login.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form' : UserLoginForm()})
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username = username, password = password)
            
            if user:
                login(request, user)
                return redirect('shop:category')
            
            messages.error(request, 'login failed check username and password')
            return redirect('account:login')
        
        return render(request, self.template_name, {'form' : form})

class UserLogout(views.View):
    def get(self, request):
        logout(request)
        return redirect('account:login')