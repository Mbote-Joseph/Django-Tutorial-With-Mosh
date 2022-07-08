from django.shortcuts import render, HttpResponse

# Create your views here.
# request -> response
# def say_hello(request):
#     return HttpResponse("Hello World!")

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Mbote-Joseph'})