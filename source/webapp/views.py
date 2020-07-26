from django.shortcuts import render, get_object_or_404, redirect
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
        if create_at == '':
            create_at = None
        article = Article.objects.create(name=name, description=description,
                               status=status, create_at=create_at)
        return redirect('find', pk=article.pk)
    return render(request, 'add_new.html', context={
        'choice': choice
    })


def find(request, pk):
    choice = STATUS_CHOICE
    article = get_object_or_404(Article, pk=pk)
    for i in choice:
        if article.status in i:
            article.status = i[1]
    if article.create_at is None:
        article.create_at = "Дата не указанна"
    return render(request, 'view.html', context={'article': article})


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    data = Article.objects.all()
    return render(request, 'index.html', context={
                            'articles': data})


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    choice = STATUS_CHOICE
    if request.method == 'POST':
        article.name = request.POST.get('name')
        article.description = request.POST.get('form-description')
        article.status = request.POST.get('select_status')
        create_at = request.POST.get('finish_data')
        if create_at == '':
            create_at = None
        article.create_at = create_at
        article.save()
        return redirect('find', pk=article.pk)
    if request.method == 'GET':
        for i in choice:
            if article.status in i:
                status = i
        if article.create_at is None:
            create_at = ''
        else:
            create_at = article.create_at.strftime("%Y-%m-%d")
        return render(request, 'edit.html', context={
            'choice': choice, 'article': article, 'status': status, 'create_at': create_at
        })