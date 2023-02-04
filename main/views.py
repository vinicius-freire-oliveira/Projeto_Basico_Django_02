from django.shortcuts import render, get_object_or_404
from .models import Aluno

def alunoView(request):
    alunos = Aluno.objects.all()
    return render(request, 'main/list.html', {'alunos':alunos})
