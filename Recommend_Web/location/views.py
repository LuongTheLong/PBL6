from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from Recommend_Web.location.models import Locations, LocationSerializer

# Create your views here.
def getLocations(request):
    locations = list(Locations.objects.all().values())
    location_serializer = LocationSerializer(data=locations, many=True)
    print(location_serializer)
    if location_serializer.is_valid():
        return JsonResponse(location_serializer.data, safe=False)
    return JsonResponse(location_serializer.errors, safe=False)

def createLocation(request):
    location_data = JSONParser().parse(request)
    location_serializer = LocationSerializer(data=location_data)
    if location_serializer.is_valid():
        location_serializer.save()
        return JsonResponse("add success", safe=False)
    return JsonResponse(location_serializer.errors, safe=False)

