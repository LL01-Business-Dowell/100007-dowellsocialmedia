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
    target_industry = models.CharField(max_length=100, blank=False, choices=CHOICES)
    target_product = models.CharField(max_length=100, blank=False)


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
    ADJECTIVES = (
        ('-', ''),
        ('the', 'the'),
        ('a', 'a'),
        ('an', 'an'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject_adjective = models.CharField(max_length=100, blank=False, choices=ADJECTIVES)
    subject = models.CharField(max_length=100, blank=False, choices=CHOICES)
    object_adjective = models.CharField(max_length=100, blank=False, choices=ADJECTIVES)
    object = models.CharField(max_length=100, blank=False)
    verb = models.CharField(max_length=100, blank=False)
    adjective = models.CharField(max_length=100, blank=False)
    sentence = models.TextField(max_length=400)
