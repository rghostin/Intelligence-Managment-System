from django.shortcuts import render


def search(request):
    return render(request, 'frontend/search.html', locals())
