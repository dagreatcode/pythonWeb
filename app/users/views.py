from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Controllers
def home(request):
    response = "<h1>Hey Ma! Look at this here Django"
    return HttpResponse(response)