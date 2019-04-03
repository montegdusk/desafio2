from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'app2/index.html')
def equipodocente(request):
	return render(request, 'app2/equipodocente.html')
def skere(request):
	return render(request, 'app2/skere.html')