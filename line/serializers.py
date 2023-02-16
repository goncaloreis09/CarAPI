from rest_framework import serializers
from .models import Line
from chassi.models import Chassi
from django.utils import timezone

class lineSerializer(serializers.ModelSerializer):

    chassis = serializers.SerializerMethodField()

    class Meta:
        model = Line
        fields = "__all__"
        validators = [
            serializers.UniqueTogetherValidator(
                queryset = Line.objects.all(),
                fields = ['name', 'manufacturer'],
                message = ("This brand already own that line name.")
            )
        ]

    def get_chassis(self, instance):
        
        list = []
        
        for q in Chassi.objects.filter(line = instance.id):
            list.append(q.code)

        return list

