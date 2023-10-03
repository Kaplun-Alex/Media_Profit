from django.urls import include, path
from revenue.views import RevenueView
from spend.views import SpendView
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('revenue/', RevenueView.as_view()),
    path('spend/', SpendView.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),
]

