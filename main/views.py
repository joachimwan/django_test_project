from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def index(request):
    # return HttpResponse("<h1>Hi Joachim, this is the main page.</h1>")
    context = {}
    messages.set_level(request, messages.DEBUG)
    messages.debug(request, 'This is DEBUG.')
    messages.info(request, 'This is INFO.')
    messages.success(request, 'This is SUCCESS.')
    messages.warning(request, 'This is WARNING.')
    messages.error(request, 'This is ERROR.')
    return render(request, 'main/index.html', context)
