from rest_framework import serializers
from .models import Brand
from datetime import datetime
from engine.models import Engine
from line.models import Line

class brandCreationSerializer(serializers.ModelSerializer):
    year_founded = serializers.IntegerField()

    class Meta:
        model = Brand
        fields = ['is_active', 'name', 'year_founded']
        extra_kwargs = {'is_active' : {'required' : False, 'write_only' : True}}
        validators = []

    def validate(self, data):

        if data['year_founded'] < 1880 or data['year_founded'] > datetime.now().year:
            raise serializers.ValidationError("The year inserted needs to be higher than 1880 and lower or equal than current year")
        
        return data


class brandSerializer(serializers.ModelSerializer):

    def get_engines_developed(self, instance):

        list = []
        count = 0
        queryset = Engine.objects.filter(manufacter = instance.id)

        count = len(queryset)

        list.append({'total' : count, 'engines' : []})

        for obj in queryset:
            list[0]['engines'].append(obj.engine_code)

        return list

    def get_owned_lines(self, instance):

        queryset = Line.objects.filter(manufacturer = instance.id)
        list = []

        for q in queryset:
            list.append(q.name)

        return list

    engines_developed = serializers.SerializerMethodField()
    owned_lines = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = '__all__'
        extra_kwargs = {'is_active' : {'write_only' : True}}

    def to_representation(self, instance):

        rep = super(brandSerializer, self).to_representation(instance)

        rep['country_founded'] = instance.country_founded.name
        rep['group'] = instance.group.name
        
        return rep