from rest_framework.decorators import api_view
from . serializers import CartItemSerializer, CartSerializer
from . models import Cart, CartItem
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def CartItemView(request):
    
    if request.method == 'GET':
        carts = CartItem.objects.all()
        serializer = CartItemSerializer(carts,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    if request.method == 'POST':
        
        serializer = CartItemSerializer(carts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def CartItemDetailView(request,pk):

    try:
        carts = CartItem.objects.get(pk=pk)
    except CartItem.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CartItemSerializer(carts)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    if request.method == 'PUT':
        
        serializer = CartItemSerializer(carts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


 




        


