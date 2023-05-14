from django.shortcuts import render, redirect
from .forms import FeedbackForm


def head(request):

    return render(request, 'main/head.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
        else:
            error = "Форма не верна"


    form = FeedbackForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/contacts.html', data)