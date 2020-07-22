from django.shortcuts import render

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
        print(create_at)
        Article.objects.create(name=name, description=description,
                               status=status, create_at=create_at)
    return render(request, 'add_new.html', context={
        'choice': choice
    })