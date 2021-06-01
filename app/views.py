from app.models import Alunos
from django.shortcuts import render
from app.forms import AlunosForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = AlunosForm()
    return render(request, 'form.html', data)
