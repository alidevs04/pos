from .models import Menu
from .serializers import MenuSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound


@api_view(['GET', 'POST'])

def menu_list(request, format=None):

    if request.method == 'GET':
        menuitems = Menu.objects.all()
        serializer = MenuSerializer(menuitems, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def menuitem_detail(request, id, format=None):


    try:
        item = Menu.objects.get(pk=id)
    except Menu.DoesNotExist:
        raise NotFound("Menu with this id is not found")
    
    if request.method == 'GET':
        serializer = MenuSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def category(request, cat):
    if request.method == 'GET':
        items = Menu.objects.filter(category__iexact=cat)
        serializer = MenuSerializer(items, many = True)
        return Response(serializer.data)

