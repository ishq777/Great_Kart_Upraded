from rest_framework.views import APIView
from rest_framework import generics, viewsets, status
from .models import Product, Variation
from .serializers import ProductSerializer, VariationSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response



# ---------------PRODUCTS------------


# @api_view(['GET', 'POST'])
# def ProductView(request):
#     if request.method == 'GET':

#         products = Product.objects.all()
#         # search = request.GET.get('search')
#         # if search:
#         #     products = Product.objects.filter(product_name__icontains=search)  

#         serializer = ProductSerializer(products, many=True)     
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
#     if request.method == 'POST':
        
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET', 'PUT','DELETE'])
# def ProductDetailView(request,pk):

#     try:
#         products = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response(status.HTTP_404_NOT_FOUND)
    

#     if request.method == 'GET':
#         serializer = ProductSerializer(products)     
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
#     if request.method == 'PUT':
        
#         serializer = ProductSerializer(products,data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         products.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# #-----------------VARIATIONS---------------------

# @api_view(['GET', 'POST'])
# def VariationView(request):
#     if request.method == 'GET':

#         variation = Variation.objects.all()
#         serializer = VariationSerializer(variation, many=True)     
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
#     if request.method == 'POST':
        
#         serializer = VariationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# @api_view(['GET' , 'PUT' , 'DELETE'])
# def VariationDetailView(request,pk):

#     try:
#         variation = Variation.objects.get(pk=pk)
#     except Variation.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    


#     if request.method == 'GET':

#         serializer = VariationSerializer(variation)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         serializer = VariationSerializer(variation, data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)

#     if request.method == 'DELETE':

#         variation.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    



    













    
class ProductView(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['product_name', 'description']
    ordering_fields = ['id']


# class VariationView(viewsets.ModelViewSet):
#     queryset = Variation.objects.all()
#     serializer_class = VariationSerializer


# class VariationListView(generics.ListAPIView):
#     queryset = Variation.objects.all()
#     serializer_class = VariationSerializer


# class VariationDetailView(generics.RetrieveUpdateAPIView):
#     queryset = Variation.objects.all()
#     serializer_class = VariationSerializer
#     lookup_field = 'pk'


