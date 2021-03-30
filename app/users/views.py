from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Controllers
def home(request):
    response = "<h1>Hey Ma! Look at this here Django"
    return HttpResponse(response)

def index(request):
    response = """
        <h1>Hello, it's me</h1>
        <p>
        klsklsnsknjlnklnklnkjlnjklnlkjnlknklnklnkn
        </p>
    """
    return HttpResponse(response)