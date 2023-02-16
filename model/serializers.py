from rest_framework import serializers
from .models import Model


class modelSerializer(serializers.ModelSerializer):

    def get_brand(self, instance):

        return instance.chassi.line.manufacturer.name

    def get_line(self,instance):
        return instance.chassi.line.name

    def get_fuel(self, instance):
        return instance.engine.fuel

    def get_production_period(self, instance):
        if instance.chassi.year_end_of_production:
            return str(instance.chassi.year_created) + " - " + str(instance.chassi.year_end_of_production)

        
        return str(instance.chassi.year_create) + "+"

    brand = serializers.SerializerMethodField()
    line = serializers.SerializerMethodField()
    fuel = serializers.SerializerMethodField()
    production_period = serializers.SerializerMethodField()
    body_type = serializers.CharField()

    class Meta:
        model = Model
        fields = "__all__"
        extra_kwargs = {'updated_at' : {'read_only' : True}}

    def to_representation(self, instance):

        rep = super(modelSerializer, self).to_representation(instance)

        rep['engine'] = instance.engine.engine_code
        rep['chassi'] = instance.chassi.code

        return rep