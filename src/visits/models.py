from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db -> table
    # id -> hiddem-> primary key-> auto increment
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)