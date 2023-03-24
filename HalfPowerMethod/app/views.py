from audioop import reverse
from contextlib import redirect_stderr
from datetime import datetime
from re import T
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .system import *
from .forms import CreateNewList
from .models import Input

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact page',
            'message':'Hi, this is the contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def app(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            tf = form.cleaned_data["transfer"]
            f = form.cleaned_data["function"]
            t = form.cleaned_data["time"]
            n = Input(transfer = tf,function = f,time =t)
            n.save()
        return HttpResponseRedirect('/result')
    else:
        form = CreateNewList()
    return render(
        request,
        'app/app.html',
        {   
            'title':'App',
            'message':'Your application page.',
            'year':datetime.now().year,
            'form':form,
        }
    )

def result(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/result.html',
        {   
            'title':'Result',
            'message':'Your result page.',
            'year':datetime.now().year,
            'graph':draw_figure(),
            'input':Input.objects.last()
        }
    )
