from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator


def index(request):
    #SET UP PAGINATION
    p = Paginator(Registration.objects.all().order_by('-First_Name'), 5)
    page = request.GET.get('page')
    page_list = p.get_page(page)

    context = { 'registration_list' : page_list }
    return render(request, 'index.html', context)


def create(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = { 'form' : form }
    return render(request, 'create.html', context)


def edit(request, pk):
    registration = Registration.objects.get(id = pk)
    form = RegistrationForm(instance = registration)

    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance = registration)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = { 'form' : form }
    return render(request, 'create.html', context)


def delete(request, pk):
    registration = Registration.objects.get(id = pk)
    registration.delete()
    # if request.method == "POST":        
    #     registration.delete()
    return redirect('/')

    # context = { 'mdlRegistration' : registration }
    # return render(request, 'index.html', context)