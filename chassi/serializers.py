from rest_framework import serializers
from datetime import datetime
from .models import Chassi
from body.models import Body

class chassiSerializer(serializers.ModelSerializer):

    bodies_available = serializers.SlugRelatedField(
        many = True,
        read_only = False,
        slug_field = "name",
        queryset = Body.objects.all()
    )

    class Meta:
        model = Chassi
        fields = "__all__"
        extra_kwargs = {'updated_at' : {'read_only' : True}}
        validators = [
            serializers.UniqueTogetherValidator(
                queryset = Chassi.objects.all(),
                fields = ['code', 'line'],
                message = ("This chassi code already exists for this line.")
            )
        ]

    def validate(self, data):

        existing_data = self.to_representation(self.instance)
        
        if data:
            if 'year_created' in data:
                if data['year_created'] < 1880 or data['year_created'] > datetime.now().year:
                    raise serializers.ValidationError({'year_created' : 'Year created must be higher than 1880 and lower or equal than current year.'}) 


            if 'year_end_of_production' in data and data['year_end_of_production'] <= existing_data['year_created']:
                raise serializers.ValidationError({'year_end_of_production' : 'Year of end of production must be higher than the year of creation.'})

        return data

    def to_representation(self, instance):

        rep = super(chassiSerializer, self).to_representation(instance)

        rep['line'] = instance.line.name

        return rep