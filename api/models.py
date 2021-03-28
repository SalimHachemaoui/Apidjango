from django.db import models
import uuid


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Nom")
    description=models.CharField(max_length=500,verbose_name="Déscription")
    direction = models.CharField(max_length=120, verbose_name="Adresse")
    telephone = models.IntegerField()
    url1 = models.CharField(max_length=2085)
    url2 = models.CharField(max_length=2085)
    url3 = models.CharField(max_length=2085)
    url4 = models.CharField(max_length=2085)
    x = models.FloatField(verbose_name="longitude")
    y = models.FloatField(verbose_name="latitude")

    def __str__(self):
        return self.name




class Phrases(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Francais")
    phrase = models.CharField(max_length=500, verbose_name="Kabyle")































































class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    type = models.CharField(max_length=20,
                            choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('COFFEE', 'Coffee'),
                                     ('DINNER', 'Dinner')])
    thumbnail = models.ImageField(upload_to="recipe_thumbnails", default="recipe_thumbnails/default.png")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe = models.ManyToManyField(Recipe)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")

    def __str__(self):
        return self.name
