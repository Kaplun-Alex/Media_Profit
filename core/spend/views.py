from django.shortcuts import render
from django.http import HttpResponse
from .models import SpendStatictic
from revenue.models import RevenueStatictic
from django.db.models import Sum

"""
Написати файл views.py в spend.
Реалізувати ендпоинт
отримуємо queryset моделі SpendStatistic
з поділом по дням (date) та назвою (name),
з агрегованими сумами значень spend, impressions, clicks, conversions
та пов'язаними значеннями revenue з моделі RevenueStatistic.

"""
def get_spend(request):
    #result = SpendStatictic.objects.all()
    #spend_agregation = SpendStatictic.objects.aggregate(Sum('spend'))
    #impressions_agregation = SpendStatictic.objects.aggregate(Sum('impressions'))
    #clicks_agregation = SpendStatictic.objects.aggregate(Sum('clicks'))
    #conversion_agregation = SpendStatictic.objects.aggregate(Sum('conversions'))

    res_transaction = SpendStatictic.objects.filter().values('date', 'name').order_by('date', 'name').annotate(\
        spend_agregation=Sum('spend'),\
        impressions_agregation=Sum('impressions'),\
        clicks_agregation=Sum('clicks'), \
        conversion_agregation=Sum('conversions'),
        revenue_agregation=RevenueStatictic.objects.filter().values('spend_id'))
    
    
    print(res_transaction)
    #print(spend_agregation, impressions_agregation, clicks_agregation, conversion_agregation)

    #print(type(result))
    #print(result)
    return HttpResponse(f"<h1>spend response<h1/>")