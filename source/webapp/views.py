from django.shortcuts import render

from webapp.models import Article


def index_view(request):
    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data
    })


def add_new(request):
    choice = Article.give_choices()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('form-description')
        status = request.POST.get('select_status')
        create_at = request.POST.get('finish_data')
        new_status = None
        for i in choice:
            check = status in i
            if check:
                ind = i.index(status)
                ind = ind - 1
                new_status = choice[ind][0]
                break
        status = new_status
        print(name)
        # Article.objects.create(name=name, description=description,
        #                        status=status, create_at=create_at)
    return render(request, 'add_new.html', context={
        'choice': choice
    })