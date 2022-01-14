
# Projeto Django Clínica

### Atualizando o sistema
```
sudo apt update 

```

```
sudo apt -y upgrade
```
### Instalando o Python3
```
sudo apt install python3-pip
```
### Instalando o env e virtualenv
```
sudo apt install -y python3-venv
```
```
sudo apt install python3-virtualenv
```
### Criando o ambiente virtual
```
virtualenv env -p python3
```
### Ativando o ambiente virtual
```
. env/bin/activate
```
### Instalando o Django
```
pip install django
```
### Criando o projeto
```
django-admin startproject core .
```
### Mudando as configurações
Abra o arquivo core/settings.py 
```
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') #adicione essa linha
```
depois faça a importação:
```
import os
```
### Criando um banco de dados
```
python3 manage.py migrate
```
### Startando o servidor
```
python3 manage.py runserver
```
### Criando uma aplicação
```
python3 manage.py startapp clinica
```
### Dizendo ao Django para usar a aplicação 
abra o arquivo core/settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clinica', #adicionando a aplicação
]
```
### Instalando a biblioteca Pillow
```
python3 -m pip install Pillow
```
### Criando os modelos
abra o arquivo clinica/models.py 
```
from django.db import models
from django.conf import settings


class Especialidade(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.nome 

class Medico(models.Model):
    nome = models.CharField(max_length=200)
    crm = models.CharField(max_length=8) 
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, verbose_name="Especialidade") #relacionamento 1-n
    imagem = models.ImageField(upload_to='clinica/media', blank=True)


    def __str__(self):
        return self.nome 

    
class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    sexo = models.CharField(max_length=9)
    telefone = models.CharField(max_length=12)

    def __str__(self):
        return self.nome 

class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name="Medico") 
    data = models.DateField()
    
    Horarios = (
        ("1", "08:00 ás 09:00"),
        ("2", "09:00 ás 10:00"),
        ("3", "10:00 ás 11:00"),
        ("4", "13:00 ás 14:00"),
        ("5", "14:00 ás 15:00"),
    )
    horario = models.CharField(max_length=10, choices=Horarios)
        
    def __str__(self):
        return f'{self.medico} - {self.get_horario_display()}'

class Consulta(models.Model):
    agendas = models.ForeignKey(Agenda, on_delete=models.CASCADE, verbose_name="Consulta")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente", blank=False)
        
    def __str__(self):
        return f'{self.agendas} - {self.cliente}'
```
### Criando tabelas para os modelos no banco de dados
```
python3 manage.py makemigrations clinica
```
#### Aplicando ao banco de dados
```
python3 manage.py migrate clinica
```
### Django Admin
abra o arquivo clinica/admin.py
```
from django.contrib import admin
from .models import Especialidade, Medico, Cliente, Agenda, Consulta
#registrando as class do modelo

admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Cliente)
admin.site.register(Agenda)
admin.site.register(Consulta)
```
### Criando um superusuário
```
python3 manage.py createsuperuser
```
### URLs
abra o arquivo core/urls.py
```
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinica.urls')),
]

```
### Criando clinica.urls
crie um arquivo urls.py na pasta clinica/urls.py
adicione:
```
from django.urls import path
from . import views 


urlpatterns = [

    path('', views.pagina_inicial, name='pagina_inicial'),
     ...
    
]
```
### Django view

```
from django.shortcuts import render, get_object_or_404, redirect
from clinica.models import Especialidade, Medico, Cliente, Agenda, Consulta
from clinica.forms import MedicoForm, ClienteForm, AgendaForm, EspForm, ConsultaForm
from django.contrib.auth import authenticate, login, logout

 

def pagina_inicial(request):
    return render(request, 'clinica/index.html', {})
    
    ...

```
crie uma pasta clinica\templates, dentro crie um arquivo index.html

clinica
    templates
        clinica
            index.html
### Adicionando referência para a pasta de img
abra o arquivo core.urls.py
```
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
### Bootstrap
link de configuração do bootstrap
```
<link 
href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
rel="stylesheet" 
integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" c
rossorigin="anonymous">
```
baixe as templates prontas do bootstrap
https://getbootstrap.com/docs/5.0/getting-started/download/

crie uma pasta chamada static dentro da pasta clinica

clinica
    static 
    templates
copie da pasta navbar-fixed:
assets
    dist
        css
        js
cole na pasta static
#### Carregando os arquivos da pasta static
```
{% load static %}
```
#### Criando um template base
crie um arquivo base.html
adicione:
```
{% load static %}

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.84.0">
    <title>Grey Sloan Memorial Hospital</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/navbar-fixed/">

    

     <!-- Bootstrap core CSS -->
     <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
     <link rel="stylesheet" href="{% static 'navbar-top-fixed.css' %}">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>

    
    <!-- Custom styles for this template -->
    <link href="navbar-top-fixed.css" rel="stylesheet">
  </head>
  <body>
    
<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Grey Sloan</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav me-auto mb-2 mb-md-0">
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'pagina_inicial' %}">Home</a>
        </li>
      </ul>>
          <form class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-secondary" type="submit">Search</button>
             
          </form>

      <ul class="nav justify-content-end">
        <li class="nav-item">
        {% if user.is_authenticated %}
          <a class="nav-link active" aria-current="page" href="{% url 'logout_usuario' %}">Sair</a>
        {% else %}
          <a class="nav-link active" aria-current="page" href="{% url 'page_login' %}">Login</a>
        {% endif %}
        </li>
      </ul>
    </div>
  </div>
</nav>

<main class="container">
  <div class="bg-light p-5 rounded">
      {% block content %}


      {% endblock %}
  </div>
</main>


    <script  rel="stylesheet" src="{% static 'js/bootstrap.bundle.min.js' %}"></script>


      
  </body>
</html>
```
### Formulários
crie um arquivo com o nome forms.py dentro da pasta clinica
```
from django import forms

from clinica.models import Consulta, Medico, Cliente, Especialidade, Agenda, Consulta
from datetime import date

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
        
        ...
```
####    Salvando os dados do formulário
abra o arquivo clinica/views.py
```
from django.shortcuts import render, get_object_or_404, redirect
from clinica.models import Especialidade, Medico, Cliente, Agenda, Consulta
from clinica.forms import MedicoForm, ClienteForm, AgendaForm, EspForm, ConsultaForm
from django.contrib.auth import authenticate, login, logout

def cadastrar_medico(request):
    if request.method == "POST":
        form = MedicoForm(request.POST, request.FILES)
        if form.is_valid():
            medico = form.save(commit=False)
            form.save()
            return redirect('detalhar_medico', id=medico.id)
    else:
        form = MedicoForm()
    return render(request, 'clinica/editar_medico.html', {'form': form})
    
    ...
   ```


