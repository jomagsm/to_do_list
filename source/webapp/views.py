from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ArticleForm
from webapp.models import Article, STATUS_CHOICE


def index_view(request):
    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data
    })


def add_new(request):
    choice = STATUS_CHOICE
    if request.method == 'POST':
        errors = {}
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                create_at=form.cleaned_data['create_at'])
            return redirect('find', pk=article.pk)
        else:
            return render(request, 'add_new.html', context={
                'form': form
            })
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
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')


def edit(request, pk):
    choice = STATUS_CHOICE
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        if article.create_at is None:
            create_at = ''
        else:
            create_at = article.create_at.strftime("%Y-%m-%d")
        form = ArticleForm(initial={
                "name": article.name,
                "description": article.description,
                "status": article.status,
                "create_at": create_at})
        return render(request, 'edit.html', context={
            'form':form,
            'article':article,
            'create_at': create_at,
            'choice':choice
        })
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.name = form.cleaned_data['name']
            article.description = form.cleaned_data['description']
            article.status = form.cleaned_data['status']
            create_at = form.cleaned_data['create_at']
            if create_at == '':
                create_at = None
            article.create_at = create_at
            article.save()
            return redirect('find', pk=article.pk)
        else:
            if article.create_at is None:
                create_at = ''
            else:
                create_at = article.create_at.strftime("%Y-%m-%d")
            return render(request,'edit.html',context={
                'article': article,
                'form': form,
                'create_at':create_at,
                'choice': choice
            })
    else:
         return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])