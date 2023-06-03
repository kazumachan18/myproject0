from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy

def index_view(request):
    return render(request, 'index.html')