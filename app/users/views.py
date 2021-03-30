from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Controllers
def home(request):
    response = "<h1>Hey Ma! Look at this here Django"
    return HttpResponse(response)

def index(request):
    return render(request, 'users/index.html', {})

def detail(request):
    return HttpResponse("<h1>Details Page</h1>")

def add(request):
    return HttpResponse("<h1>Add Page</h1>")