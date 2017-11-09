from django.db import models
from .image import Image
from .postable import Postable

class Article(Postable):
    label = models.CharField(max_length=200)
    text = models.TextField()
    description = models.CharField(max_length=800, null=True)
    is_blog_article = models.BooleanField(default=True)
    preview_image = models.ForeignKey(Image, null=True)
    #metadatas = models.ManyToManyField(Metadata, null=True)
    visible = models.BooleanField(default=False)
    #Связать многие-ко-многим с Metadata
    def __str__(self):
        return 'Article: "' + self.label +"' "