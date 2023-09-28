from django.urls import include, path
from revenue.views import get_revenue
from spend.views import get_spend
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('revenue/', get_revenue),
    path('spend/', get_spend),
]
