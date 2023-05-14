from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.dates import DateMixin

def regist(request):
    return render(request, 'regist/regist.html')
