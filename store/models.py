from django.db import models

# Create your models here.
"""
Produit
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

"""
Commande : 
- produit
- article
- quantité
"""
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"



"""
Panier
- nom articles
- prix 
- quantité
- supprimer article(s)
- commander 

"""

class Cart(models.Model):
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False) #l'article est commandé ou pas

#ce qui est retourné sur la page admin :
def __str__(self):
    return self.product

