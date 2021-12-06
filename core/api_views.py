from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from core import serializers
from core.models import Category, Currency, Transaction
from core.serializers import (CategorySerializer, CurrencySerializer,
                              ReadTransactionSerializer,
                              WriteTransactionSerializer)


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    # Dont paginate this List Endpoint
    pagination_class = None

    # Set a Pagination to this Endpoint * Just declare it in SETTINGS.PY
    # pagination_class = PageNumberPagination


# CRUD USE, it needs ROUTERS
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionModelViewset(ModelViewSet):
    # This will speed the query from 2seconds to 195ms
    queryset = Transaction.objects.select_related("currency", "category")
    # serializer_class = TransactionSerializer

    # Use to search with filter
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("description", "amount")
    ordering_fields = ("amount", "date")
    filterset_fields = ("currency__code",)


    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
