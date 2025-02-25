from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from .models import Customers,Order
from .serializers import CustomersSerializer,OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime ,timedelta
from rest_framework import filters
#from django.views.decorators.csrf import csrf_exempt
#from django.utils.decorators import method_decorator

#@method_decorator(csrf_exempt, name='dispatch')
class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['timestamp']





class OrderSearchView(APIView):
    def get(self, request, *args, **kwargs):
        # Retrieve query parameters
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        try:

            today = datetime.today().date()
            default_start_date = today - timedelta(days = 30)





            # Validate and parse date strings
            if start_date_str:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            else:
                start_date = None

            if end_date_str:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            else:
                end_date = None

            # Ensure both dates are provided
            if not start_date or not end_date:
                return Response(
                    {"error": "Both 'start_date' and 'end_date' must be provided."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Filter orders by date range
            #orders = Order.objects.filter(time__range=(start_date, end_date))
            orders = Order.objects.filter(timestamp__range=(start_date, end_date))


            # Serialize the filtered orders
            serializer = OrderSerializer(orders, many=True)

            # Return the serialized data
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValueError:
            # Handle invalid date format
            return Response(
                {"error": "Invalid date format. Use 'YYYY-MM-DD'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            # Handle other unexpected errors
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


#def orders_page(request):
    #return render(request, 'index.html')








#class OrderSearchView(APIView):
 #   def get(self, request):
  #      start_date = request.query_params.get('start_date')
   #     end_date = request.query_params.get('end_date')
    #    orders = Order.objects.filter(time__range=(start_date, end_date))
     #   serializer = OrderSerializer(orders, many=True)
      #  return Response(serializer.data)







