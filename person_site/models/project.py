from django.db import models
from .postable import Postable
from .article import Article

class Project(Postable):
    name = models.CharField(max_length=100)
    article = models.ForeignKey(Article)
    keywords = models.CharField(max_length=300)
    article = models.OneToOneField(
        Article,
        on_delete=models.CASCADE,
        primary_key=True
    )
    def __str__(self):
        return 'Project: "' + self.name + '"'