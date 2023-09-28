from django.shortcuts import render
from django.http import HttpResponse

def get_spend(request):
    return HttpResponse("<h1>spend response<h1/>")