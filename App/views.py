from django.shortcuts import render


# Create your views here.

def home(request):
	return render(request, 'App/home.html')


def about(request):
	return render(request, 'App/about.html')


def contacts(request):
	return render(request, 'App/contacts.html')
