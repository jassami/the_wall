from typing import Sequence
from django.shortcuts import redirect, render
from django.apps import apps
User = apps.get_model('login_app', 'User')
from .models import *
from datetime import datetime, timedelta
import bcrypt

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context={
        'user': User.objects.get(id= request.session['user_id']),
        'messages': Message.objects.all().order_by('-created_at'),
        'comments': Comment.objects.all().order_by('created_at')        
    }
    return render(request, 'wall.html', context)

def message(request):
    this_user= User.objects.get(id= request.session['user_id']) 
    message= Message.objects.create(message= request.POST['message'], user= this_user)
    request.session['message_id']= message.id
    return redirect('/wall')

def comment(request):
    this_message= Message.objects.get(id= request.POST['message_id']) 
    comment_user= User.objects.get(id= request.session['user_id'])
    comment= Comment.objects.create(comment= request.POST['comment'], message= this_message, user= comment_user)
    print(comment)
    request.session['comment_id']= comment.id
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')

def delete(request):
    this_comment= Comment.objects.get(id= request.POST['comment_id'])
    this_comment.delete()
    return redirect('/wall')