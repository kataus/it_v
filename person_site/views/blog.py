from django.shortcuts import render

from person_site.models import Article

def blog(request):
    articles = Article.objects.order_by('date_added')
    context = {'articles': articles[:6]}
    return render(request, 'person_site/blogs.html', context)