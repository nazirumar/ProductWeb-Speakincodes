from django.db import models

# Create your models here.


class Category(models.Model):
    CategoryName=models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryName


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
    def __str__(self):
        return self.ProductName


class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    category= models.ForeignKey(Category, on_delete=models.CASCADE )
    ProductImage= models.ImageField(upload_to='product' )

    def __str__(self):
        return str(self.product)

