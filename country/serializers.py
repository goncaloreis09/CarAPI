from rest_framework import serializers
from .models import Country

class countrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'
        