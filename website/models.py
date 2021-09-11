from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Users'
        db_table = "Emails"


class Sentences(models.Model):
    pass
