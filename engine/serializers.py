from rest_framework import serializers
from .models import Engine

class engineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Engine
        fields = "__all__"
        validators = [
            serializers.UniqueTogetherValidator(
                queryset = Engine.objects.all(),
                fields = ["engine_code", "manufacter", "fuel"],
                message =("The combination of these values are already in use. Please try something unique.")
            )
        ]

    
    def to_representation(self, instance):

        rep = super(engineSerializer, self).to_representation(instance)

        rep['manufacter'] = instance.manufacter.name

        return rep