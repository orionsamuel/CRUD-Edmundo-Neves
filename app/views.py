from app.models import Alunos
from django.shortcuts import redirect, render
from app.forms import AlunosForm
from app.models import Alunos

# Create your views here.

def home(request):
    data = {}
    data['db'] = Alunos.objects.all()
    data['form'] = AlunosForm()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = AlunosForm()
    return render(request, 'form.html', data)

def create(request):
    form = AlunosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def edit(request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)
    data['form'] = AlunosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)
    form = AlunosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Alunos.objects.get(pk=pk)
    db.delete()
    return redirect('home')