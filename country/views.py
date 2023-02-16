from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Country
from .serializers import countrySerializer

from brand.models import Brand

# Create your views here.

@api_view(['GET'])
def get_all_countries(request):

    queryset = Country.objects.all()


    serializer = countrySerializer(queryset, many = True)

    if len(queryset) == 0:
        return Response({'message' : 'There are no countries created yet.'})

    return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(['GET'])
def get_countries_with_given_name(request, name):

    queryset = Country.objects.filter(name = name)

    serializer = countrySerializer(queryset, many = True)

    if len(queryset) == 0:
        return Response({'message' : 'There are no countries created with that name yet.'})

    return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def create_country(request):

    if request.method == "POST":

        serializer = countrySerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    return Response({'message' : 'Method not allowed. Please perform a POST request.'})


@api_view(['GET', 'PUT'])
def update_country(request, id):

        if request.method == "PUT":

            queryset = get_object_or_404(Country, id = id)

            serializer = countrySerializer(queryset, data = request.data, partial = True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)

            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        
        return Response({'message' : 'Method not allowed. Please perform a PUT request.'})
