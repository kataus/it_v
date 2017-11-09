from django.db import models


class Image(models.Model):
    label = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    preview_link = models.CharField(max_length=300)
    full_link = models.CharField(max_length=300)
    def __str__(self):
        return 'Image: "' + self.full_link + "' "