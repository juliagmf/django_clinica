from django.shortcuts import render, get_object_or_404, redirect
from clinica.models import Especialidade, Medico, Cliente, Agenda, Consulta
from clinica.forms import MedicoForm, ClienteForm, AgendaForm, EspForm, ConsultaForm
from django.contrib.auth import authenticate, login, logout


#parte de login 

def pagina_inicial(request):
    return render(request, 'clinica/index.html', {})

def page_login(request):
    return render(request, 'clinica/login.html',{})

def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        medicos = Medico.objects.all()
        return render(request, 'clinica/listar_medicos.html', {'medicos':medicos})
    else:
        return render(request, 'clinica/login.html',{})   

def logout_usuario(request):
    logout(request)
    return render(request, 'clinica/login.html',{})

# especialidade

def listar_especialidades(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'clinica/listar_especialidades.html', {'especialidades':especialidades})

def cadastrar_especialidade(request):
    if request.method == "POST":
        form = EspForm(request.POST, request.FILES)
        if form.is_valid():
            especialidade = form.save(commit=False)
            form.save()
            return redirect('listar_especialidades')
    else:
        form = EspForm()
    return render(request, 'clinica/editar_especialidade.html', {'form': form})

#medico

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {'medicos':medicos})

def detalhar_medico(request, id):
    medico = get_object_or_404(Medico, pk=id)
    return render(request, 'clinica/detalhar_medico.html', {'medico':medico})

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


#cliente

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clinica/listar_clientes.html', {'clientes':clientes})

def detalhar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request, 'clinica/detalhar_cliente.html', {'cliente':cliente})

def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            cliente = form.save(commit=False)
            form.save()
            return redirect('detalhar_cliente', id=cliente.id)
    else:
        form = ClienteForm()
    return render(request, 'clinica/editar_cliente.html', {'form': form})


# agenda

def listar_agenda(request):
    agendas = Agenda.objects.all()
    return render(request, 'clinica/listar_agenda.html', {'agendas':agendas})

def cadastrar_agenda(request):
    if request.method == "POST":
        form = AgendaForm(request.POST, request.FILES)
        if form.is_valid():
            agenda = form.save(commit=False)
            form.save()
            return redirect('listar_agenda')
    else:
        form = AgendaForm()
    return render(request, 'clinica/editar_agenda.html', {'form': form})

 # consulta   



def cadastrar_consulta(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST, request.FILES)
        if form.is_valid():
            consulta = form.save(commit=False)
            form.save()
            return redirect('pagina_inicial')
    else:
        form = ConsultaForm()
    return render(request, 'clinica/editar_consulta.html', {'form': form})

