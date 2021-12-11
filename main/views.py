from django.shortcuts import render
from django.http import HttpResponseRedirect



# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def login(request):
    if request.user.is_authenticated:
        return render(request, 'main/page.html', {})
    else:
        # return HttpResponseRedirect('')
        return render(request, 'main/index.html', {})
