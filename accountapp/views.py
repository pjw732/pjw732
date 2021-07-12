from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html',
                      context={'new_hello_world': new_hello_world})     # alt+enter 이름이 같으면 모듈 가져옴
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'POST METHOD!'})