from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tag, Genero, Livro
from django.contrib import messages
from django.contrib.messages import constants

@login_required
def DivulgarCreateView(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        generos = Genero.objects.all()
        return render(request, 'create_livro.html', {'tags':tags, 'generos': generos})
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        descricao = request.POST.get('descricao')    
        foto = request.FILES.get('foto')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        genero_id = request.POST.get('genero')
        status = request.POST.get('status')

        genero = Genero.objects.get(id=genero_id)

        livro = Livro(
            usuario = request.user,
            titulo = titulo,
            autor = autor,
            descricao = descricao,
            foto = foto,
            estado = estado,
            cidade = cidade,
            telefone = telefone,
            genero = genero,
            status = status,
        )

        livro.save()

        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            livro.tags.add(tag)
        
        livro.save()
        tags = Tag.objects.all()
        genero = Genero.objects.all()
        messages.add_message(request, constants.SUCCESS, 'Novo Livro Cadastrado')
        return render(request, 'create_livro.html', {'tags':tags, 'genero': genero})
    
def DivulgarUpdateView(request):
    pass

@login_required
def DivulgarListView(request):
    if request.method == "GET":
        livros = Livro.objects.filter(usuario=request.user)
        return render (request, 'list_livro.html', {'livros':livros})

