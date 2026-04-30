from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Create your views here.
def singleobj(request):
    data=Person.objects.get(id=1)
    ser=PersonSerializer(data)
    json_data=JSONRenderer().render(ser.data)
    return HttpResponse(json_data, content_type='application/json')
@csrf_exempt
def multipleobj(request):
    if request.method=='POST':
        raw=request.body
        stream=io.BytesIO(raw)
        parse_data=JSONParser().parse(stream)
        ser=PersonSerializer(data=parse_data)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"created":"successfull"},status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    data=Person.objects.all()
    ser=PersonSerializer(data,many=True)
    json_data=JSONRenderer().render(ser.data)
    return HttpResponse(json_data,content_type='application/json')
