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
        Article.objects.create(name=name, description=description,
                               status=status, create_at=create_at)
    return render(request, 'add_new.html', context={
        'choice': choice
    })


def find(request):
    choice = STATUS_CHOICE
    id = request.GET.get('id')
    obj = Article.objects.get(pk=id)
    for i in choice:
        if obj.status in i:
            status = i[1]
    return render(request, 'view.html',context={
                'name': obj.name, 'description': obj.description,
                'status': status, 'create_at': obj.create_at})


def delete(request):
    id = request.GET.get('id')
    obj_del = Article.objects.get(pk=id)
    obj_del.delete()
    data = Article.objects.all()
    return render(request, 'index.html', context={
                            'articles': data})