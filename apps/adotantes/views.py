from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AdotanteForm
from .models import Adotante
from django.contrib.auth.decorators import login_required

# Create your views here.

def add_adotante(request):
    template_name = 'adotantes/add_adotante.html'
    context = {}
    if request.method == 'POST':
        form = AdotanteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('adocoes:add_adocao')
    form = AdotanteForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_adotantes(request):
    template_name = 'adotantes/list_adotantes.html'
    adotantes = Adotante.objects.filter()
    context = {
        'adotantes': adotantes
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_adotante(request, id_adotante):
    template_name = 'adotantes/add_adotante.html'
    context ={}
    adotante = get_object_or_404(Adotante, id=id_adotante)
    if request.method == 'POST':
        form = AdotanteForm(request.POST, instance=adotante)
        if form.is_valid():
            form.save()
            return redirect('adotantes:list_adotantes')
    form = AdotanteForm(instance=adotante)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_adotante(request, id_adotante):
    adotante = Adotante.objects.get(id=id_adotante)
    adotante.delete()
    return redirect('adotantes:list_adotantes')