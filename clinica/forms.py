from django import forms

from clinica.models import Consulta, Medico, Cliente, Especialidade, Agenda, Consulta
import datetime 
from django.core.exceptions import ValidationError


class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico

        fields = ('nome','crm','email','telefone', 
        'especialidade', 'imagem')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Dr'}),
            'crm': forms.TextInput(attrs={ 'class': 'form-control',
                                            'placeholder':'PI 0101'}),
            'email': forms.TextInput(attrs={ 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={ 'class': 'form-control'}),
            'especialidade': forms.Select(attrs={ 'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={ 'class': 'form-control'}),
            
        }

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = ('nome','cpf','email','sexo','telefone'
        )

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={ 'class': 'form-control'}),
            'email': forms.TextInput(attrs={ 'class': 'form-control'}),
            'especialidade': forms.Select(attrs={ 'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'F'}),
            'telefone': forms.TextInput(attrs={ 'class': 'form-control'}),
                   
        }


      


class EspForm(forms.ModelForm):

    class Meta:
        model = Especialidade
        fields = ('nome',)

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Cirurgia Plástica'})
            
            
        }

class AgendaForm(forms.ModelForm):
    

    class Meta:
        model = Agenda
        fields = ('medico','data','horario' )

        widgets = {
            'medico': forms.Select(attrs={ 'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class':'form-control', 'type':'date'})
                     
            
        }
    def clean_data(self):
        data = self.cleaned_data['data']

       # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError('Invalid date - renewal in past')

       # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Invalid date - renewal more than 4 weeks ahead')

       # Remember to always return the cleaned data.
        return data

    

class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ('agendas', 'cliente')

        widgets = {
            'agendas': forms.Select(attrs={ 'class': 'form-control'}),
            'cliente': forms.Select(attrs={ 'class': 'form-control'}),
            
            
            
        }

