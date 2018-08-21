from rest_framework import serializers
from .models import Wine, Food, User, Pairing, Favorite

class WineSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Wine
    fields = ('id', 'type')

class FoodSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Food
    fields = ('id', 'type', 'example_1', 'example_2')

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password')

class PairingSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Pairing
    fields = ('id', 'wine', 'food')

class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Favorite
    fields = ('id', 'user', 'pairing')