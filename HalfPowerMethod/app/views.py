from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .system import *
from .forms import CreateNewList

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
            'year':datetime.now().year,
        }
    )

def app(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            # load data from input
            Num = form.cleaned_data["Numerator"]
            Den = form.cleaned_data["Denominator"]
            num = []
            den = []
            # parse data
            for s in Num.split():
                num_double = float(s)
                num.append(num_double)
            for s in Den.split():
                den_double = float(s)
                den.append(den_double)
            sys = signal.TransferFunction(num, den)
            # create object
            system1 = System(sys)
            # calculate damping
            system1.calc_damping()
            return render(
                request,
                'app/result.html',
                    {   
                        'title':'Result',
                        'message':'Your result page.',
                        'year':datetime.now().year,
                        'freq_graph': system1.draw_figure(),
                        'nat': system1.nat,
                        'quality': system1.q,
                        'damping': system1.damping
                    }
            )
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
