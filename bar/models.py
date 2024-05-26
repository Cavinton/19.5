from django.db import models

# Create your models here.

class AlcoholicDrink(models.Model):
    title = models.CharField(max_length=30, verbose_name='Алкогольные напитки')
    image = models.ImageField(blank=True, null=True, upload_to='title')

    def __str__(self):
        return self.title



class Cocktail(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена')
    type = models.ForeignKey(AlcoholicDrink,on_delete=models.CASCADE, related_name='cocktails')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
#new, не добавлял никуда
# class LimitedSet(models.Model):
#     type = models.OneToOneField(AlcoholicDrink, on_delete=models.CASCADE, related_name='LimitedSet')
#     title = models.CharField(max_length=70)
#     image = models.ImageField(blank=True, null=True)
#     price = models.IntegerField(verbose_name='Цена')
#     created_at = models.DateTimeField(auto_now_add=True)
#     in_stock = models.BooleanField()

#     def __str__(self):
#         return self.title
    
# class Shot(models.Model):
#     type = models.ManyToManyField()
