from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Sala

def entrar(request):
    if request.method == 'GET':
        return render(request, 'entrar.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')

        sala = Sala.objects.filter(nome = nome).first()

        if sala:
            return redirect(reverse('chat', args = {sala.nome, }))
        else:
            return HttpResponse('Nome incorreto')
        
def chat(request, nome):
    return render(request, 'home.html', {'nome': nome})


