from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Cliente

# Criar views e models do contato


def home(request):
    return render(request, 'base/home.html')

def contato(request):
    if request.method=='POST':
        cliente=Cliente()
        name=request.POST.get('name')
        telefone=request.POST.get('telefone')
        email=request.POST.get('email')
        menssagem=request.POST.get('menssagem')
        cliente.nome=name
        cliente.telefone=telefone
        cliente.email=email
        cliente.menssagem=menssagem
        cliente.save()
        # return HttpResponse('Obrigado pelo Contato')

    return render(request,'base/contato.html')
