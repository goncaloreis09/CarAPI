from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Brand
from .serializers import brandCreationSerializer, brandSerializer
from country.models import Country

@api_view(['GET'])
def list_brands(request):

    queryset = Brand.objects.filter(is_active = True)

    if len(queryset) == 0:
        return Response({'message': 'There are no brands created yet.'})
  

    serializer = brandSerializer(queryset, many = True)
    

    return Response(serializer.data)

@api_view(['GET'])
def list_searched_brands(request):

    brand = request.GET.get('q', None)

    if brand is not None:
        queryset = Brand.objects.filter(name__contains = brand)

        if len(queryset) == 0:
            return Response({'message': 'No matches found.'})
    

        serializer = brandSerializer(queryset, many = True)
        

        return Response(serializer.data)

    return Response({'error' : 'Wrong argument given.'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def create_brand(request):

    serializer = brandCreationSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


# @api_view(['DELETE', 'GET'])
# def delete_brand(request, id):

#     queryset = Brand.objects.filter(id = id)

#     if queryset:
#         queryset.delete()
#         return Response({'message': 'Brand deleted successfully.'}, status = status.HTTP_200_OK)

#     return Response({'message' : 'Given id does not correspond to any object.'}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET'])
def delete_brand(request, id):
    
    queryset = get_object_or_404(Brand, id = id)

    serializer = brandSerializer(queryset, data = {"is_active" : False}, partial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET'])
def  update_brand(request, id):
    
    queryset = get_object_or_404(Brand, id = id)

    serializer = brandSerializer(queryset, data = request.data, partial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)