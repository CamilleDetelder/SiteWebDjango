from django.db import models

# Create your models here.
"""
Product
- Nom
- Description
- Prix 

"""
class Product(models.Model):
    name = models.CharField(max_length=128) #nom en max 128 caractères
    price = models.FloatField(default=0.0) #prix en float possible
    description = models.TextField(blank=True) #pas obligé de mettre description
    image = models.ImageField(upload_to="image_products", blank=True, null=True) #stocker les images dans le dossier image_products, laisser espace vide pour l'image

    def __str__(self):
        return self.name
