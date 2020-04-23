from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'home.html')
def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

