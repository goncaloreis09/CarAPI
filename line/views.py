
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Line
from .serializers import lineSerializer

# Create your views here.

@api_view(['GET'])
def get_all_lines(request):

    queryset = Line.objects.all()

    if len(queryset) == 0:
        return Response({"message" : "There are no lines created yet."})

    serializer = lineSerializer(queryset, many = True)

    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def create_line(request):

    serializer = lineSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_line(request, id):

    queryset = get_object_or_404(Line, id = id)
    
    serializer = lineSerializer(queryset, data = request.data, partial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
