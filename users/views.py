from django.shortcuts import render #Shortcuts 
from django.contrib.auth import logout, login, authenticate #Contrib.auth
from django.contrib.auth import login as auth_login
from django.urls import reverse #Urls

from django.http import HttpResponseRedirect #http

from django.contrib.auth.forms import UserCreationForm #Contrib.auth.forms
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method != 'POST':
        form = AuthenticationForm(request)
    else:
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form':form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username,
                                            password=request.POST['password1'])
            auth_login(request, authenticate_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form':form}
    return render(request, 'users/register.html', context)

# Create your views here.
def logout_view(request):
    """Log out of user"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))