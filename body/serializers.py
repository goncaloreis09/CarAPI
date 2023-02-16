from rest_framework import serializers
from .models import Body

class bodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'
        extra_kwargs = { 'created_at' : {'read_only' : True},
                            'updated_at' : {'read_only' : True}}

    