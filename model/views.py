from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Model
from .serializers import modelSerializer

@api_view(['GET'])
def get_all_models(request):

    queryset = Model.objects.all()

    serializer = modelSerializer(queryset, many = True)

    if len(queryset) == 0:
        return Response({'message' : 'There are no models created yet.'}, status = status.HTTP_200_OK)

    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def create_model(request):

    serializer = modelSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    