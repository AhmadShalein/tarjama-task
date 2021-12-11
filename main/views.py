from django.shortcuts import render
form django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'main/index.html', {})

@login_required
def login(request):
    return render(request, 'main/page.html', {})
