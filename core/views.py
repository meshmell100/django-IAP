from django.shortcuts import render, redirect
from . import forms
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for contacting us!")
    else:
        form = forms.ContactForm()
    return render(request, "core/index.html", {"form": form})


def home(request):
    return render(request, "core/home.html")

def catering(request):
    return render(request,"core/catering.html")

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your feedback!")
    return render(request, 'core/feedback.html')

def catering(request):
    return render(request, "core/catering.html")

def login(request):
    return render(request,"registration/login.html")