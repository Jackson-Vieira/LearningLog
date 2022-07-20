from django.shortcuts import render #Shortcuts 
from django.contrib.auth import logout, login, authenticate #Contrib.auth
from django.urls import reverse #Urls

from django.http import HttpResponseRedirect #http

from django.contrib.auth.forms import UserCreationForm #Contrib.auth.forms

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username,
                                            password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form':form}
    return render(request, 'users/register.html', context)

# Create your views here.
def logout_view(request):
    """Log out of user"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))