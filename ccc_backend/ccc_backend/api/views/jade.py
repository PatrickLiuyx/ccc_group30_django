from django.shortcuts import render


def main_page(request):
    return render(request, 'main.html')


def emotion(request):
    return render(request, 'emotion.html')
