from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Engine
from .serializers import engineSerializer

# Create your views here.

@api_view(['GET'])
def get_all_engines(request):

    queryset = Engine.objects.all()


    serializer = engineSerializer(queryset, many = True)

    if len(queryset) == 0:
        return Response({'message' : 'This brand didn\'t developed an engine yet.'})

    return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def create_engine(request):

    serializer = engineSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
