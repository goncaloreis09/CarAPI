from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Body
from .serializers import bodySerializer

# Create your views here.

@api_view(['GET'])
def get_all_bodies(request):
    queryset = Body.objects.all()

    serializer = bodySerializer(queryset, many = True)

    if len(queryset) == 0:
        return Response({'message' : 'There are no body types created yet.'}, status = status.HTTP_200_OK)

    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def create_body(request):

    serializer = bodySerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
def update_body(request, body):

    queryset = get_object_or_404(Body, id = id)

    serializer = bodySerializer(queryset, data = request.data, partial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)