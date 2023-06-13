from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Main page")


def test_page(request):
    return HttpResponse("Test", status=404)


def get_about(request):
    return HttpResponse("Страница о нас")


def get_contacts(request):
    return HttpResponse("Страница с контактами")
