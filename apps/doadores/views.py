from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DoadorForm
from .models import Doador
from django.contrib.auth.decorators import login_required
# Create your views here.

def add_doador(request):
    template_name = 'doadores/add_doador.html'
    context = {}
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('animais:add_animal')
    form = DoadorForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_doadores(request):
    template_name = 'doadores/list_doadores.html'
    doadores = Doador.objects.filter()
    context = {
        'doadores': doadores
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_doador(request, id_doador):
    template_name = 'doadores/add_doador.html'
    context ={}
    doador = get_object_or_404(Doador, id=id_doador)
    if request.method == 'POST':
        form = DoadorForm(request.POST, instance=doador)
        if form.is_valid():
            form.save()
            return redirect('doadores:list_doadores')
    form = DoadorForm(instance=doador)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_doador(request, id_doador):
    doador = Doador.objects.get(id=id_doador)
    doador.delete()
    return redirect('doadores:list_doadores')
