from django.contrib import admin

# Register your models here.
from website.models import Sentences, SentenceResults

admin.site.register(Sentences)
admin.site.register(SentenceResults)
