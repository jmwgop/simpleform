from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import LPRForm

@login_required(login_url='/accounts/login/')
def create_lpr(request):
    form = LPRForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        model_instance = form.save(commit=False)
        model_instance.timestamp = timezone.now()
        model_instance.save()
        return redirect('create_lpr')
    return render(request, "lpr/create_lpr.html", {'form': form})
