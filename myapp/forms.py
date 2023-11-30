from django import forms
from .models import Agendamento
from .models import Piscina


class PiscinaForm(forms.ModelForm):
    class Meta:
        model = Piscina
        fields = ['endereco', 'detalhes', 'localizacao']


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'hora']
