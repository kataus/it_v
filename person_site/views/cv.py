from django.shortcuts import render

def cv( request ):
    context = {'label': 'Тесты'}
    return render(request, 'person_site/projects.html', context)