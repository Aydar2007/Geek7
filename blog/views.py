from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def get_about(request):
    return render(request, "blog/about.html")


def get_contacts(request):
    return render(request, "blog/contacts.html")
