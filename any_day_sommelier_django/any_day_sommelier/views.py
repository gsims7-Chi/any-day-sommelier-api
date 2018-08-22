# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Food, Wine, User, Pairing, Favorite
from django.http import JsonResponse
import json
from .serializers import FoodSerializer, WineSerializer, UserSerializer, PairingSerializer, FavoriteSerializer
from django.forms.models import model_to_dict

class WineList(generics.ListCreateAPIView):
  queryset = Wine.objects.all()
  serializer_class = WineSerializer

class WineDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Wine.objects.all()
  serializer_class = WineSerializer

class FoodList(generics.ListCreateAPIView):
  queryset = Food.objects.all()
  serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Food.objects.all()
  serializer_class = FoodSerializer

def wine_pairing(request, pk):
  wine = Wine.objects.get(id=pk)
  foods = wine.food_set.all().values('type', 'example_1', 'example_2')
  foods_list = list(foods)
  # return JsonResponse(foods_list, safe=False)
  # it = model_to_dict(foods_list)
  return JsonResponse(foods_list, safe=False)

def food_pairing(request, pk):
  food = Food.objects.get(id=pk)
  wines = food.wines.all().values('type')
  wines_list = list(wines)
  return JsonResponse(wines_list, safe=False)

