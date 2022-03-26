from django.db import models

# Create your models here.


class Category(models.Model):
    Category=models.CharField(max_length=100)

    def __str__(self):
        return self.Category


class SubCategory(models.Model):
    Category= models.ForeignKey(Category, on_delete=models.CASCADE)
    SubCategory= models.CharField(max_length=100)

    def __str__(self):
        return self.SubCategory

class SubSubCategory(models.Model):
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    SubSubCategory= models.CharField(max_length=100)

    def __str__(self):
        return self.SubSubCategory

class Products(models.Model):
    SubSubCategory = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE)
    ProductName= models.CharField(max_length=100)
    ProductPrice= models.DecimalField(max_digits=30, decimal_places=2)
    ProductImage= models.ImageField(upload_to='product')
    def __str__(self):
        return self.ProductName
