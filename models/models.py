from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CharField
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField


class AdviceModel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = CharField(max_length=13)
    address = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.phone_number}"

class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    count = models.IntegerField()
    address = models.CharField(max_length=255)
    feature_count = models.IntegerField(validators=[MaxValueValidator(8), MinValueValidator(3)])
    feature_1 = models.CharField(max_length=255, null=True, blank=True)
    feature_2 = models.CharField(max_length=255, null=True, blank=True)
    feature_3 = models.CharField(max_length=255, null=True, blank=True)
    feature_4 = models.CharField(max_length=255, null=True, blank=True)
    feature_5 = models.CharField(max_length=255, null=True, blank=True)
    feature_6 = models.CharField(max_length=255, null=True, blank=True)
    feature_7 = models.CharField(max_length=255, null=True, blank=True)
    feature_8 = models.CharField(max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} {self.phone_number}"


class ServiceModel(models.Model):
    photo = CloudinaryField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    currency = models.DecimalField(decimal_places=2,max_digits=7, default=200.00)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class PartnerModel(models.Model):
    photo = CloudinaryField()
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    opinion = models.TextField()
    important = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        return self.name

class ImagesModel(models.Model):
    about = CloudinaryField()
    favicon = CloudinaryField()
    logo = CloudinaryField()

class Customer_Opinion(models.Model):
    url = models.URLField()
    opinion = models.TextField()
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} {self.url}"

class FunctionsModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name