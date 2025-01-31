from django.shortcuts import render
from rest_framework import viewsets
from .models import Customers,Order
from .serializers import CustomersSerializer,OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime

class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderSearchView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        orders = Order.objects.filter(time__range=(start_date, end_date))
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)






# Create your views here.
