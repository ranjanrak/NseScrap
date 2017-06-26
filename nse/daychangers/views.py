from django.shortcuts import render
from .nse import Nse
from urllib.request import build_opener, HTTPCookieProcessor, Request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.views import generic 
from django.views.generic import View
from .forms import UserForm


def index(request):
        nse = Nse()
        gainer=nse.get_top_gainers()
        loser=nse.get_top_losers()
        return render(request, 'daychangers/index.html',{'gainer': gainer, 'loser':loser,} )

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        nse = Nse()
        gainer=nse.get_top_gainers()
        loser=nse.get_top_losers()
        return render(request, 'daychangers/redlogin.html')
    context = {
        "form": form,
    }
    return render(request, 'daychangers/registration_form.html',{'form': form,} )    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  
            nse = Nse()
            gainer=nse.get_top_gainers()
            loser=nse.get_top_losers()
            return render(request, 'daychangers/index.html',{'gainer': gainer, 'loser':loser,} )
        else:    
            return render(request, 'daychangers/login.html',{'error_message': 'Go and Create new account'})   

    else:   
        return render(request, 'daychangers/login.html')       
def superindex(request):
            nse = Nse()
            gainer=nse.get_top_gainers()
            loser=nse.get_top_losers()
            return render(request, 'daychangers/superindex.html',{'gainer':gainer, 'loser':loser,} )

def supergainer(request):
            nse = Nse()
            gainer=nse.get_top_gainers()
            loser=nse.get_top_losers()
            return render(request, 'daychangers/temp.html',{'gainer':gainer,'loser':loser,} )

def superloser(request):
            nse = Nse()
            gainer=nse.get_top_gainers()
            loser=nse.get_top_losers()
            return render(request, 'daychangers/indexlow.html',{'loser':loser,'gainer':gainer,})

def search(request):
            return render(request, 'daychangers/search.html')

def result(request):
        nse=Nse()
        if request.method=="POST":
            script=request.POST['search']    
            getquote=nse.get_quote(script)
            return render(request, 'daychangers/result.html',{'getquote': getquote,})

        return render(request, 'daychangers/search.html',{'error_message': 'Enter correct name'})    


def stocklist(request):
        nse=Nse()
        stockli=nse.get_stock_codes()
        return render(request,'daychangers/stocklist.html',{'stockli':stockli,})

