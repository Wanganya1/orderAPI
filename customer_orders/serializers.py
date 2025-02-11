from rest_framework import serializers
from .models import Customers, Order
#from .sms import send_sms


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__' 



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__' 

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        customer = order.customer
        from .sms import send_sms
        send_sms(customer.phone_number, f"New order: {order.item} for {order.amount}")
        return order