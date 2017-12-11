from django.shortcuts import render

def projects( request ):
    context = {'label': 'Тесты'}
    return render(request, 'person_site/projects.html', context)