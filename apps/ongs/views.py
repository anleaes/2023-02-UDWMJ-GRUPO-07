from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OngForm
from .models import Ong
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_ong(request):
    template_name = 'ongs/add_ong.html'
    context = {}
    if request.method == 'POST':
        form = OngForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('ongs:list_ongs')
    form = OngForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_ongs(request):
    template_name = 'ongs/list_ongs.html'
    ongs = Ong.objects.filter()
    context = {
        'ongs': ongs
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_ong(request, id_ong):
    template_name = 'ongs/add_ong.html'
    context ={}
    ong = get_object_or_404(Ong, id=id_ong)
    if request.method == 'POST':
        form = OngForm(request.POST, instance=ong)
        if form.is_valid():
            form.save()
            return redirect('ongs:list_ongs')
    form = OngForm(instance=ong)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_ong(request, id_ong):
    ong = Ong.objects.get(id=id_ong)
    ong.delete()
    return redirect('ongs:list_ongs')