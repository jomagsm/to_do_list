from django.shortcuts import render

from webapp.models import Article


def index_view(request):
    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data
    })