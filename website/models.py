from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Users'
        db_table = "Emails"


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    target_industry = models.CharField(max_length=30, null=False, blank=False)
    target_product = models.CharField(max_length=30, null=False, blank=False)


class Sentences(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=30, null=False, blank=False)
    object = models.CharField(max_length=30, null=False, blank=False)
    verb = models.CharField(max_length=30, null=False, blank=False)
    adjective = models.CharField(max_length=30, null=False, blank=False)
    sentence = models.TextField(max_length=30)
