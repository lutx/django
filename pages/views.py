from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	#print(request.user)
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request,"home.html",{})

def about_view(request,*args,**kwargs):
	#return HttpResponse("<h1>Troche o nas!</h1>")
	return render(request,"about.html",{})

def contact_view(request,*args,**kwargs):
	#return HttpResponse("<h1>Kontakt</h1>")
	return render(request,"contact.html",{})

def social_view(request,*args,**kwargs):
	#return HttpResponse("<h1>Linki do social media</h1>")
	return render(request,"social.html",{})			