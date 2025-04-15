from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from .models import Order
from django.http import JsonResponse
from django.utils.timezone import now
from django.db.models import Sum

# Create your views here.

@api_view(['POST', 'GET'])
def reg_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def total_sales_today(request):
    if request.method == 'GET':
        today = now().date()
        total = Order.objects.filter(order_date=today).aggregate(amount__sum=Sum('total_price'))['amount__sum'] or 0

        return JsonResponse({'total_sales': total})

