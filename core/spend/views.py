from django.views import View
from django.http import HttpResponse
from .models import SpendStatictic
from django.db.models import Sum

"""
Написати файл views.py в spend.
Реалізувати ендпоинт
отримуємо queryset моделі SpendStatistic
з поділом по дням (date) та назвою (name),
з агрегованими сумами значень spend, impressions, clicks, conversions
та пов'язаними значеннями revenue з моделі RevenueStatistic.

"""

class SpendView(View):
    def get(self, request, *args, **kwargs):
        
        res_transaction = SpendStatictic.objects.all().select_related().order_by('date', 'name').annotate(\
            spend_agregation=Sum('spend'),\
            impressions_agregation=Sum('impressions'),\
            clicks_agregation=Sum('clicks'), \
            conversion_agregation=Sum('conversions'))

  
        print(res_transaction, )

        return HttpResponse(f"<h1>spend response<h1/>")