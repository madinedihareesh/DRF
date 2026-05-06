from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer,PersonModelSerialzer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
@csrf_exempt
def singleobj(request,id):
    data=get_object_or_404(Person,id=id)
    if request.method=='PUT':
        raw=request.body
        io_data=io.BytesIO(raw)
        parsed_data=JSONParser().parse(io_data)
        ser=PersonModelSerialzer(data,data=parsed_data)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'update':'successfull'})
        return JsonResponse(ser.errors,status=status.HTTP_401_UNAUTHORIZED)
    if request.method=='PATCH':
        raw=request.body
        io_data=io.BytesIO(raw)
        parsed_data=JSONParser().parse(io_data)
        ser=PersonModelSerialzer(data,data=parsed_data,partial=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'update':'successfull'})
        return JsonResponse(ser.errors,status=status.HTTP_401_UNAUTHORIZED)
    ser=PersonModelSerialzer(data)
    json_data=JSONRenderer().render(ser.data)
    return HttpResponse(json_data, content_type='application/json')
@csrf_exempt
def multipleobj(request):
    if request.method=='POST':
        raw=request.body
        stream=io.BytesIO(raw)
        parse_data=JSONParser().parse(stream)
        ser=PersonModelSerialzer(data=parse_data)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"created":"successfull"},status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    data=Person.objects.all()
    ser=PersonModelSerialzer(data,many=True)
    json_data=JSONRenderer().render(ser.data)
    return HttpResponse(json_data,content_type='application/json')
