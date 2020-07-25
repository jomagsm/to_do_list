from django.shortcuts import render
from django.http import HttpResponseRedirect
from webapp.models import Article, STATUS_CHOICE


def index_view(request):
    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data
    })


def add_new(request):
    choice = STATUS_CHOICE
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('form-description')
        status = request.POST.get('select_status')
        create_at = request.POST.get('finish_data')
        article = Article.objects.create(name=name, description=description,
                               status=status, create_at=create_at)
        return HttpResponseRedirect(f'/view/{article.pk}')
    return render(request, 'add_new.html', context={
        'choice': choice
    })


def find(request, pk):
    choice = STATUS_CHOICE
    article = Article.objects.get(pk=pk)
    for i in choice:
        if article.status in i:
            article.status = i[1]
    return render(request, 'view.html',context={'article':article})


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    data = Article.objects.all()
    return render(request, 'index.html', context={
                            'articles': data})