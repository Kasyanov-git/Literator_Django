from django.shortcuts import render
from .models import Articles

from django.views.generic import DetailView

def adv(request):
    adv_list = {}
    adv = Articles.objects.order_by('-date')
    num = 0
    for i in adv:
        adv_list[f"adv_title_{num}"] = i.title
        adv_list[f"adv_anons_{num}"] = i.anons
        num+=1
    return render(request, 'adv/adv.html', adv_list)


