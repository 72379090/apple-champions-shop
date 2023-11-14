from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def master(request):
    return render(request, 'master.html')
