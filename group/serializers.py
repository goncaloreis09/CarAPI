from rest_framework import serializers
from django.core import serializers as djangoSerilizer
from datetime import datetime
from .models import Group
from brand.models import Brand

class groupSerializer(serializers.ModelSerializer):

    def CheckValidYear(value):
        
        if value > datetime.now().year or value < 1880:
            raise serializers.ValidationError("Given year is invalid, please try something higher than 1880 and lower or equal than current year.")

        return value

    def get_brands(self, instance):

        list = []

        for obj in Brand.objects.filter(group = instance.id):
            if obj.is_active:
                list.append(obj.name)
        
        return list

        
    year_created = serializers.IntegerField(validators=[CheckValidYear])
    brands = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = '__all__'
