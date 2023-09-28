from django.shortcuts import render
from django.http import HttpResponse

def get_revenue(request):
    return HttpResponse("<h1>revenue_response<h1/>")
