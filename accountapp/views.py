from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    return render(request, 'accountapp/hello_world.html')     # alt+enter 이름이 같으면 모듈 가져옴