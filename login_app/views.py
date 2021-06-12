from django.shortcuts import redirect, render
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    # request.session['send']= "register"
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        request.session['first_name']= request.POST['first_name']
        pw_hash= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        user= User.objects.create(first_name= request.POST['first_name'], last_name=request.POST['last_name'], birthday= request.POST['birthday'], email= request.POST['email'], password= pw_hash)
        request.session['user_id'] = user.id
        return redirect('/wall')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        # request.session['send']= "login"
        if errors:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')
        else:
            log_user= User.objects.filter(email=request.POST['email'])
            if len(log_user) != 1:
                return redirect('/')
            if log_user:
                user= log_user[0]
                request.session['first_name'] = user.first_name
                if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                    request.session['user_id']= user.id
                    print(request.POST)
                    return redirect('/wall')
    else:
        return redirect('/')


