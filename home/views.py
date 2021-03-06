from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages




# Create your views here.

def home(request):
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form has been sent")
            return redirect("home")
    else:
        form = ContactForm()
        
    context = {
        'form':form
    }
    return render(request, "home/index.html", context)

def about(request):
    return render(request, "home/about.html")

def teacher(request):
    return render(request, "home/teacher.html")