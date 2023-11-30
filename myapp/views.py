from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from myapp.forms import AgendamentoForm, PiscinaForm
from myapp.models import Agendamento


# Create your views here.
@login_required
def index(request):
    agendamentos = Agendamento.objects.filter(user=request.user)
    return render(request, 'index.html', {'agendamentos': agendamentos})


# criar um formulário de agendamento para serviço de piscineiro
@login_required
def agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        piscina_form = PiscinaForm(request.POST)
        if form.is_valid() and piscina_form.is_valid():
            piscina = piscina_form.save()
            agendamento_service = form.save(commit=False)
            agendamento_service.user = request.user
            agendamento_service.piscina = piscina
            agendamento_service.save()
            return redirect('index')
    else:
        form = AgendamentoForm()
        piscina_form = PiscinaForm()
    return render(request, 'formulario_agenda.html', {'form': form, 'piscina_form': piscina_form})
