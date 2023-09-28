from django.shortcuts import render
from django.http import HttpResponse
from .models import RevenueStatictic
from django.db.models import Sum

"""
Написати файл views.py в revenue.
Реалізувати ендпоинт
отримуємо queryset моделі RevenueStatistic
з поділом по дням (date) та назвою (name),
з агрегованими сумами значень revenue
та пов'язаними значеннями spend, impressions, clicks, conversion з моделі SpendStatistic.
"""
def get_revenue(request):

    revenue_res_transaction = RevenueStatictic.objects.filter().values('date', 'name').order_by('date', 'name').annotate(\
        revevue_agregation=Sum('revenue'),)
    print(revenue_res_transaction)
    return HttpResponse("<h1>revenue_response<h1/>")
