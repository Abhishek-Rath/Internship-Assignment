from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from bills.models import Item, Invoice
from bills.serializers import ItemSerializer, InvoiceSerializer
from rest_framework import viewsets, status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import render_to_pdf 
from django.template.loader import render_to_string

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, format=None):
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def post(self, request):

        serializer = InvoiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):   

                    
        instance = Invoice.objects.filter(item = request.data["item"]).first()
        serializer = InvoiceSerializer(instance, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def generate_invoice(request):
    if request.method == "GET":
        
        invoices = Invoice.objects.all()
        total_price = 0
        itemsList = list()

        for i in range(len(invoices)):
            item = Item.objects.get(id = invoices[i].item.id)
            itemsList.append({})
            itemsList[i]['name'] = item.item_name
            itemsList[i]['ppu'] = item.price
            itemsList[i]['quantity'] = invoices[i].quantity
            
            itemsList[i]['price'] = invoices[i].quantity * item.price
            total_price += invoices[i].quantity * item.price


        pdf = render_to_pdf(render_to_string('bills/invoice.html', {
            "items": itemsList,
            "total": total_price
        }))
        
        return HttpResponse(pdf, content_type='application/pdf')


        # return render(request, "bills/invoice.html", {
        #     "items": itemsList,
        #     "total": total_price
        # })


# @api_view(['GET'])
# def itemList(request):
#     items = Item.objects.all()
#     serializer = ItemSerializer(items, many = True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def itemDetail(request, pk):
#     items = Item.objects.get(id = pk)
#     serializer = ItemSerializer(items, many = False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create(request):
#     item = ItemSerializer(data = request.data)

#     if item.is_valid():
#         item.save()
#         return Response(item.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# def itemUpdate(request, pk):
#     item = Item.objects.get(pk=pk)
#     serializer = ItemSerializer(instance = item, data = request.data)
  
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)


#     return Response(request.data)

def index(request):
    return HttpResponse("<h1>Hello, world!</h1>")