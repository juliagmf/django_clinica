from django.urls import path
from . import views 


urlpatterns = [

    #criando rotas

    path('', views.pagina_inicial, name='pagina_inicial'),
    #login
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
    path('page_login', views.page_login, name='page_login'),
    #especialidade
    path('listar_especialidades', views.listar_especialidades, name='listar_especialidades'),
    path('especialidades/new/', views.cadastrar_especialidade, name='cadastrar_especialidade'),
    #medico
    path('listar_medicos', views.listar_medicos, name='listar_medicos'), 
    path('medico/<int:id>/', views.detalhar_medico, name='detalhar_medico'),
    path('medico/new/', views.cadastrar_medico, name='cadastrar_medico'),  
    #cliente
    path('listar_clientes', views.listar_clientes, name='listar_clientes'), 
    path('cliente/<int:id>/', views.detalhar_cliente, name='detalhar_cliente'),
    path('cliente/new/', views.cadastrar_cliente, name='cadastrar_cliente'),
    #agenda
    path('listar_agenda', views.listar_agenda, name='listar_agenda'),
    path('agenda/new/', views.cadastrar_agenda, name='cadastrar_agenda'),
    #consulta
    path('consulta/new/', views.cadastrar_consulta, name='cadastrar_consulta'),
    
]