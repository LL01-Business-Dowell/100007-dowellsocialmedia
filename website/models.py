from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Users'
        db_table = "Emails"


class IndustryData(models.Model):
    CHOICES = (
        ('Technology & Telecom', 'Technology & Telecom'),
        ('Food & Beverages', 'Food & Beverages'),
        ('Travel & Leisure', 'Travel & Leisure'),
        ('Restaurants & Hotels', 'Restaurants & Hotels'),
        ('Automotive', 'Automotive'),
        ('Apparel', 'Apparel'),
        ('Banking & Insurance', 'Banking & Insurance'),
        ('Chain stores', 'Chain stores'),
        ('Alcohol', 'Alcohol'),
        ('Tobacco', 'Tobacco'),
        ('Business Services & consultancies', 'Business Services & consultancies'),
        ('Transportation', 'Transportation'),
        ('Media', 'Media'),
        ('Heavy equipments', 'Heavy equipments'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    target_industry = models.CharField(max_length=100, null=False, blank=False, choices=CHOICES)
    target_product = models.CharField(max_length=100, null=False, blank=False)


class Sentences(models.Model):
    CHOICES = (
        ('Livinglab', 'Livinglab'),
        ('Innovation', 'Innovation'),
        ('User experience', 'User experience'),
        ('Storytelling', 'Storytelling'),
        ('Consumer Behaviour', 'Consumer Behaviour'),
        ('Behavioral economics', 'Behavioral economics'),
        ('Consumer Insights', 'Consumer Insights'),
        ('Statistics', 'Statistics'),

    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=100, null=False, blank=False,choices=CHOICES)
    object = models.CharField(max_length=100, null=False, blank=False)
    verb = models.CharField(max_length=100, null=False, blank=False)
    adjective = models.CharField(max_length=100, null=False, blank=False)
    sentence = models.TextField(max_length=400)
