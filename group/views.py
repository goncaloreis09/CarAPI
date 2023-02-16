
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Group
from brand.models import Brand
from .serializers import groupSerializer

# Create your views here.


@api_view(['GET'])
def get_all_groups(request):

    queryset = Group.objects.all()

    serializer = groupSerializer(queryset, many = True)

    if len(queryset) == 0:
        return Response({'message' : 'There are no groups created yet.'}, status = status.HTTP_200_OK)

    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def create_group(request):

    serializer = groupSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

