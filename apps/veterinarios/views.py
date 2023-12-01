from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import VeterinarioForm
from .models import Veterinario

# Create your views here.
def add_veterinario(request):
    template_name = 'veterinarios/add_veterinario.html'
    context = {}
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('veterinarios:list_veterinarios')
    form = VeterinarioForm()
    context['form'] = form
    return render(request, template_name, context)

def list_veterinarios(request):
    template_name = 'veterinarios/list_veterinarios.html'
    veterinarios = Veterinario.objects.filter()
    context = {
        'veterinarios': veterinarios
    }
    return render(request, template_name, context)

def edit_veterinario(request, id_veterinario):
    template_name = 'veterinarios/add_veterinario.html'
    context ={}
    veterinario = get_object_or_404(Veterinario, id=id_veterinario)
    if request.method == 'POST':
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect('veterinarios:list_veterinarios')
    form = VeterinarioForm(instance=veterinario)
    context['form'] = form
    return render(request, template_name, context)

def delete_veterinario(request, id_veterinario):
    veterinario = Veterinario.objects.get(id=id_veterinario)
    veterinario.delete()
    return redirect('veterinarios:list_veterinarios')
