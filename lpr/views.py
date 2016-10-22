from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import LPRForm

@login_required(login_url='/accounts/login/')
def create_lpr(request):
    if request.method == "POST":
        form = LPRForm(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('create_lpr')
    else:
        form = LPRForm()

    return render(request, "lpr/create_lpr.html", {'form': form})
