
from django.contrib import admin
from rest_framework import routers
from django.urls import path
from core import api_views



router = routers.SimpleRouter()
router.register(r'categories', api_views.CategoryModelViewSet, basename="category")
router.register(r'transactions', api_views.TransactionModelViewset, basename="transaction")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("currencies/", api_views.CurrencyListAPIView.as_view(), name="currencies"),
] + router.urls
