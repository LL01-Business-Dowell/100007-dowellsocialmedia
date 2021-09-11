from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Users'
        db_table = "Emails"


class IndustryData(models.Model):
    CHOICES = (
        ('Technology & Telecom 1', 'Option 1'),
        ('Food & Beverages', 'Option 2'),
        ('Travel & Leisure', 'Option 2'),
        ('Restaurants & Hotels', 'Option 2'),
        ('Automotive', 'Option 2'),
        ('Apparel', 'Option 2'),
        ('Banking & Insurance', 'Option 2'),
        ('Chain stores', 'Option 2'),
        ('Alcohol', 'Option 2'),
        ('Tobacco', 'Option 2'),
        ('Business Services & consultancies', 'Option 2'),
        ('Transportation', 'Option 2'),
        ('Media', 'Option 2'),
        ('Heavy equipments', 'Option 2'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    target_industry = models.CharField(max_length=30, null=False, blank=False, choices=CHOICES)
    target_product = models.CharField(max_length=30, null=False, blank=False)


class Sentences(models.Model):
    CHOICES = (
        ('Technology & Telecom 1', 'Option 1'),

    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=30, null=False, blank=False,choices=CHOICES)
    object = models.CharField(max_length=30, null=False, blank=False)
    verb = models.CharField(max_length=30, null=False, blank=False)
    adjective = models.CharField(max_length=30, null=False, blank=False)
    sentence = models.TextField(max_length=30)
