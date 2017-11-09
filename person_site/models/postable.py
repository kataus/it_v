from django.db import models

class Postable(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    message = models.TextField(max_length=500, null=True )
    class Meta:
        abstract = True