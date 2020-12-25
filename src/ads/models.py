from django.db import models
from django.template.defaultfilters import slugify

class Product(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(max_length=200, upload_to='product', null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"



class Partners(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(max_length=200, upload_to='product', null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)

    class Meta:
        verbose_name = "Xamkor"
        verbose_name_plural = "Xamkorlar"



class Contact(models.Model):
    email= models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.email

    def slug(self):
        return slugify(self.email)

    class Meta:
        verbose_name = "aloqa"
        verbose_name_plural = "aloqalar"


class Cart(models.Model):
    name = models.CharField(max_length=500)
    photo = models.ImageField(max_length=200, upload_to='product', null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)

    class Meta:
        verbose_name = "cart"
        verbose_name_plural = "carts"



class Info(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    description = models.TextField()
    info = models.TextField()
    created_at = models.DateTimeField(auto_now=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)


    def slug(self):
        return slugify(self.name)

    class Meta:
        verbose_name = "Malumot"
        verbose_name_plural = "Malumotlar"
