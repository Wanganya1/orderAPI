import os
import africastalking
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from dotenv import load_dotenv
from .models import Customers, Order
from .serializers import OrderSerializer
import logging
from rest_framework import status


# Load environment variables
load_dotenv()

# Initialize Africa's Talking
username = os.getenv('AFRICATALKING_USERNAME')
api_key = os.getenv('AFRICATALKING_API_KEY')

if not username or not api_key:
    raise ValueError("Please set both AFRICATALKING_USERNAME and AFRICATALKING_API_KEY environment variables.")

africastalking.initialize(username=username, api_key=api_key)
sms = africastalking.SMS

# Logger setup
logger = logging.getLogger(__name__)

@api_view(['POST'])
def create_order(request):
    # Validate and save the order
    serializer = OrderSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Save the order
    order = serializer.save()
    customer = order.customer

    # Prepare the SMS message
    message = f"Dear {customer.name}, your order for {order.item} of Ksh {order.amount} has been placed."

    try:
        # Send the SMS
        response = sms.send(message, [customer.phone_number])
        return Response(
            {"order": serializer.data, "sms_response": response},
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        # Log the error
        logger.error(f"Failed to send SMS: {str(e)}")
        return Response(
            {"error": f"Order created but failed to send SMS: {str(e)}", "order": serializer.data},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


  







    















# Load environment variables
"""load_dotenv()

# Initialize Africa's Talking
africastalking.initialize(
    username=os.getenv('AFRICATALKING_USERNAME'),
    api_key=os.getenv('AFRICATALKING_API_KEY')
)
sms = africastalking.SMS


@api_view(['POST'])
def create_order(request):
    # Validate and save the order
    serializer = OrderSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    # Save the order
    order = serializer.save()
    customer = order.customer

    # Prepare the SMS message
    message = f"Dear {customer.name}, your order for {order.item} of Ksh {order.amount} has been placed."

    try:
        # Send the SMS
        response = sms.send(message, [customer.phone_number])
        return Response(
            {"order": serializer.data, "sms_response": response},
            status=HTTP_201_CREATED
        )
    except Exception as e:
        # Handle SMS sending failure
        return Response(
            {"error": f"Order created but failed to send SMS: {str(e)}", "order": serializer.data},
            status=HTTP_500_INTERNAL_SERVER_ERROR
        ) """



#username = "CNU"
#api_key = "9U9JSMxFl"

#africastalking.initialize(username , api_key)

#sms = africastalking.SMS






