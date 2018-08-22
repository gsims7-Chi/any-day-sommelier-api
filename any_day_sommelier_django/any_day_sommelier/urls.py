from django.urls import path
from . import views

urlpatterns = [
  path('api/wines/', views.WineList.as_view(), name='wine-list'),
  path('api/wines/<int:pk>', views.WineDetail.as_view(), name='wine-detail'),
  path('api/food/', views.FoodList.as_view(), name='food-list'),
  path('api/food/<int:pk>', views.FoodDetail.as_view(), name='food-detail'),
  path('api/wine-pairing/<int:pk>', views.wine_pairing, name='wine-pairing'), 
  path('api/food-pairing/<int:pk>', views.food_pairing, name='food-pairing')
]
