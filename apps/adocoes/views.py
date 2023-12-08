from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AdocaoForm
from .models import	Adocao
from django.contrib.auth.decorators import login_required

# Create your views here.

def add_adocao(request):
    template_name = 'adocoes/add_adocao.html'
    context = {}
    if request.method == 'POST':
        form = AdocaoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('adocoes:list_adocoes')
    form = AdocaoForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_adocoes(request):
    template_name = 'adocoes/list_adocoes.html'
    adocoes = Adocao.objects.filter()
    context = {
        'adocoes': adocoes
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_adocao(request, id_adocao):
    template_name = 'adocoes/add_adocao.html'
    context ={}
    adocao = get_object_or_404(Adocao, id=id_adocao)
    if request.method == 'POST':
        form = AdocaoForm(request.POST, request.FILES,  instance=adocao)
        if form.is_valid():
            form.save()
            return redirect('adocoes:list_adocoes')
    form = AdocaoForm(instance=adocao)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_adocao(request, id_adocao):
    adocao = Adocao.objects.get(id=id_adocao)
    adocao.delete()
    return redirect('adocoes:list_adocoes')
