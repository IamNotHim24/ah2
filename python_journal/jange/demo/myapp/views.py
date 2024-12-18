from django.shortcuts import render,HttpResponse
from .models import TodoItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,"home.html")

@login_required
def todo(request):
    items = TodoItem.objects.all()
    return render(request,"todos.html",{"todos":items})

