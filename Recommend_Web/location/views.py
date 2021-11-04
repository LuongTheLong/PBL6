from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from Recommend_Web.location.models import Locations, LocationSerializer
from collections import defaultdict
import re

# Create your views here.
def getLocations(request):
    locations = list(Locations.objects.all().values())
    location_serializer = LocationSerializer(data=locations, many=True)
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

## SPLIT ##
def tokenize(message):
    all_words = re.findall("[A-Za-z0-9]+", message)
    set_all_words = set(all_words)
    if len(all_words) == len(set_all_words):
        return set(all_words)
    else:
        return all_words

## MAPPER ##
def wc_mapper(document):
    for word in tokenize(document):
        yield (word, 1)

## REDUCE ##
def wc_reducer(word, counts):
    array = []
    array.append(int(word))
    array.append(len(counts))
    updateData(array)


def word_count(documents):
    collector = defaultdict(list)
    for document in documents:
        for word, count in wc_mapper(document):
            ## SUFFLE ##
            collector[word].append(count)
    for word, counts in collector.items():
        wc_reducer(word, counts)

def mapReduce(request):
    data = JSONParser().parse(request)
    word_count(data['data'])
    return

def updateData(data):
    count = 0
    location = Locations.objects.get(id=data[0])
    count = location.count_click + data[1]
    location_res = {
        "id": data[0],
        "title": location.title,
        "description": location.description,
        "count_click": count,
        "category": location.category
    }
    location_serializer = LocationSerializer(location, data=location_res)
    if location_serializer.is_valid():
        location_serializer.save()
        print("Done")
    else:
        print('Error')
