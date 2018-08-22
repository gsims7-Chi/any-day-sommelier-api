from django.db import models

# Create your models here.
class Wine(models.Model):
  type = models.CharField(max_length=100)

  def __str__(self):
    return self.food.all()

class Food(models.Model):
  type = models.CharField(max_length=100)
  example_1 = models.CharField(max_length=100)
  example_2 = models.CharField(max_length=100)
  wines = models.ManyToManyField(Wine, through='Pairing')

  def __str__(self):
    return self.wine_set.all()

class User(models.Model):
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)

  def __str__(self):
    return self.username

class Pairing(models.Model):
  wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name='pairings')
  food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='pairings')

  def __str__(self):
    return "{} goes with {}".format(self.food, self.wine)

class Favorite(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
  pairing = models.ForeignKey(Pairing, on_delete=models.CASCADE, related_name='favorites')

  def __str__(self):
    return self.user
