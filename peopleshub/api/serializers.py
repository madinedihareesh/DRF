from rest_framework import serializers
from . models import Person
class PersonSerializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    city=serializers.CharField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance

class PersonModelSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=['name','city','age']    