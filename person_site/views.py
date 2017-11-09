from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import ArticleForm
from .models import Article

# Create your views here.


def index(request):
    articles = Article.objects.order_by('date_added')
    context = {'articles': articles[:6]}
    return render(request, 'person_site/index.html', context)


def blog(request):
    articles = Article.objects.order_by('date_added')
    context = {'articles': articles[:6]}
    return render(request, 'person_site/blogs.html', context)


@login_required
def articles(request):
    articles = Article.objects.order_by('date_added')
    context = {'articles': articles}
    return render(request, 'person_site/internal/articles.html', context)


@login_required
def new_article(request):
    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.is_blog_article = True
            article.visible = True

            article.save()
            return HttpResponseRedirect(reverse('person_site:articles'))
    context = {'form': form}
    return render(request, 'person_site/internal/new_article.html', context)


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'person_site/article.html', context)
