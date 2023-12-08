from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AdocaoanimalForm
from .models import Adocaoanimal
from django.contrib.auth.decorators import login_required

# Create your views here.
def add_adocaoanimal(request):
    template_name = 'adocaoanimais/add_adocaoanimal.html'
    context = {}
    if request.method == 'POST':
        form = AdocaoanimalForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('adocaoanimais:list_adocaoanimais')
    form = AdocaoanimalForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_adocaoanimais(request):
    template_name = 'adocaoanimais/list_adocaoanimais.html'
    adocaoanimais = Adocaoanimal.objects.filter()
    context = {
        'adocaoanimais': adocaoanimais
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_adocaoanimal(request, id_adocaoanimal):
    template_name = 'adocaoanimais/add_adocaoanimal.html'
    context ={}
    adocaoanimal = get_object_or_404(Adocaoanimal, id=id_adocaoanimal)
    if request.method == 'POST':
        form = AdocaoanimalForm(request.POST, instance=adocaoanimal)
        if form.is_valid():
            form.save()
            return redirect('adocaoanimais:list_adocaoanimais')
    form = AdocaoanimalForm(instance=adocaoanimal)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_adocaoanimal(request, id_adocaoanimal):
    adocaoanimal = Adocaoanimal.objects.get(id=id_adocaoanimal)
    adocaoanimal.delete()
    return redirect('adocaoanimais:list_adocaoanimais')
