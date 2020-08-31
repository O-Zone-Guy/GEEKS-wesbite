from django.shortcuts import render
from .models import Blog


# Create your views here.
def index(request):
    context = {
        'blog': Blog.objects.all()
    }
    return render(request, "blogs/index.html", context=context)


def details(request, id):
    context = {
        'blog': Blog.objects.get(pk=id)
    }
    return render(request, "blogs/details.html", context=context)
