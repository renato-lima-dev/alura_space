from django.shortcuts import render
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse('<h1>Alura Space atualizado</h1>')

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')