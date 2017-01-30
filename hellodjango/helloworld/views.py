from django.shortcuts import render, get_object_or_404
from .models import DatabaseObject


def index(request):
    db_objects = DatabaseObject.objects.order_by('name')
    return render(request, 'helloworld/index.html',
                  context={'objects': db_objects})


def say_hello(request, id_):
    db_object = get_object_or_404(DatabaseObject, id=id_)
    return render(request, 'helloworld/say_hello.html',
                  context={'object': db_object})
