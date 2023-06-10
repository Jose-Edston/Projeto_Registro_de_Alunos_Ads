from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
# Home do Projeto.

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_user = auth.authenticate(username=username, password=password)
        
        if check_user == None:
            messages.error(request, message='Usario ou senha inválidos.')
            return redirect('login')
        else:
            auth.login(request, check_user)
            return redirect('home')

    else:
        return render(request, 'pages/login.html')

def logout(request):
    AuthenticationError.logout(request)
    return redirect('login')
