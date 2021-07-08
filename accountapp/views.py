from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'POST METHOD!'})     # alt+enter 이름이 같으면 모듈 가져옴
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD!'})