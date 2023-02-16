from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Chassi
from .serializers import chassiSerializer
from datetime import datetime
from itertools import chain
# Create your views here.

@api_view(['GET'])
def get_all_chassis(request):

    queryset = Chassi.objects.all()

    serializer = chassiSerializer(queryset, many = True)

    if len(queryset) == 0:
        return Response({'message' : 'There are no chassis created yet.'}, status = status.HTTP_200_OK)

    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def get_all_chassis_within_search(request):

    search = request.GET.get('q')

    queryset = Chassi.objects.filter(code__contains = search)

    serializer = chassiSerializer(queryset, many = True)

    if len(queryset) == 0:
        return Response({'message' : 'There are no chassis created yet.'}, status = status.HTTP_200_OK)

    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def create_chassi(request):

    serializer = chassiSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_chassi(request, id):

    queryset = get_object_or_404(Chassi, id = id)

    serializer = chassiSerializer(queryset, data = request.data, partial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)