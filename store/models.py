from django.db import models
from datetime import datetime, timezone
from django.conf import settings

class Category(models.Model):
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"


    name = models.CharField(verbose_name="Nomi",max_length=255)
    icon=models.ImageField(upload_to="images/",null=True)
    slug = models.CharField(max_length=255,null=True)
    


    created_at = models.DateTimeField(verbose_name="yaratilgan sana",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="O'zgartirilgan sana",auto_now=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class Meta:
        verbose_name="Kichik kategoriya"
        verbose_name_plural="Kichik kategoriyalar"

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name





# from mptt.models import MPTTModel, TreeForeignKey


# class Kategoriya(models.Model):
#     title = models.CharField(max_length=255)
#     parent = models.ForeignKey(Kategoriya, on_delete=models.CASCADE, null=True, blank=True, related_name="children")

#     def __str__(self):
#         return self.title
   


# for kategoriya in kategoriyalar:
#     if not kategoriya.parent:
#         print(kategoriya)
#         for child_kategory in kategoriya.children.all():
#             print(child_kategory)







class Product(models.Model):
    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


    title = models.CharField(max_length=255)
    price = models.FloatField()
    old_price = models.FloatField(null=True)
    manufacturer = models.CharField(max_length=255, null=True)
    slug = models.CharField(max_length=255,null=True)
    description = models.TextField()
    rating = models.FloatField()
    guarantee = models.CharField(max_length=255, null=True, default=2)
    delivery_time = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    availabilty = models.BooleanField(default=True, null=True)
    image = models.ImageField(upload_to="images/",null=True)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField(default=True)
    


    created_at = models.DateTimeField(auto_now_add = True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)


    def __str__(self):
        return f"{self.title} - {self.price}"


    def get_rating_percent(self):
        return 100 * (self.rating / 5)


    def is_new_product(self):
        time_delta = datetime.now(timezone.utc) - self.created_at
        return time_delta.seconds < 86400



class  Product_color(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_colors",null=True)


class Product_size(models.Model):
    name = models.CharField(max_length=255) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_size",null=True)
    


class Product_image(models.Model):
    image = models.ImageField(upload_to="images/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")

