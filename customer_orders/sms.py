import africastalking
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customers, Order
#from .serializers import OrderSerializer

africastalking.initialize(username='your-username', api_key='your-api-key')

sms = africastalking.SMS

@api_view(['POST'])
def create_order(request):
    from .serializers import OrderSerializer
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        customer = order.customer

        # Send SMS
        message = f"Dear {customer.name}, your order for {order.item} of Ksh {order.amount} has been placed."
        response = sms.send(message, [customer.phone_number])

        return Response({"order": serializer.data, "sms_response": response})
    
    return Response(serializer.errors, status=400)

