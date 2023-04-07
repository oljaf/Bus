from django.shortcuts import render

# Create your views here.
def Home(request):
    return render (request,'bus/home.html')
def allcar(request):
    return  render(request,'bus/all.html')
def create(request):
return render(request,'bus/create.html')