from django.db import models

class Metadata(models.Model):
    label = models.CharField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Metadata: "' + self.label + "' "
