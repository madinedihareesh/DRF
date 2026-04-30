from rest_framework import serializers
from . models import Person
class PersonSerializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    city=serializers.CharField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)