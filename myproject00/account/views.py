from django.shortcuts import render, HttpResponse 

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('index-page')