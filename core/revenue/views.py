from django.views import View
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

class RevenueView(View):

    def get(self, request, *args, **kwargs):

        revenue_res_transaction = RevenueStatictic.objects.all().select_related("spend").order_by("date", "name").\
            annotate(revenueAgregation = Sum('revenue'))
    
        for i in revenue_res_transaction:
            print(i.spend.impressions)
        print(revenue_res_transaction.values_list())
   
        print(revenue_res_transaction)
        
        return HttpResponse("<h1>revenue_response<h1/>")
