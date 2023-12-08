from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnimalForm
from .models import Animal
from ongs.models import Ong
from django.contrib.auth.decorators import login_required
# Create your views here.

def add_animal(request):
    template_name = 'animais/add_animal.html'
    context = {}
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('animais:list_animais')
    form = AnimalForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_animais(request):
    template_name = 'animais/list_animais.html'
    animais = Animal.objects.filter()
    context = {
        'animais': animais
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_animal(request, id_animal):
    template_name = 'animais/add_animal.html'
    context ={}
    animal = get_object_or_404(Animal, id=id_animal)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animais:list_animais')
    form = AnimalForm(instance=animal)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_animal(request, id_animal):
    animal = Animal.objects.get(id=id_animal)
    animal.delete()
    return redirect('animais:list_animais')

def search_animais(request):
    template_name = 'animais/list_animais.html'
    query = request.GET.get('query')
    animais = Animal.objects.filter(name__icontains=query)
    context = {
        'animais': animais,
    }
    return render(request,template_name, context)