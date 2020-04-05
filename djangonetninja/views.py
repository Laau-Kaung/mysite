from django.http import HttpResponse

def home(request):
    return HttpResponse("home")

def about(request):
    return HttpResponse('about')

def types(request,name):
    Name = name.capitalize()
    return HttpResponse(f'Hello, <span style="color:blue;">{Name}</span>')