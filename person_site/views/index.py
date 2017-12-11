from django.shortcuts import render

from ..models import Article

def index(request):
    articles = Article.objects.order_by('date_added')
    context = {'articles': articles[:6]}
    return render(request, 'person_site/index.html', context)