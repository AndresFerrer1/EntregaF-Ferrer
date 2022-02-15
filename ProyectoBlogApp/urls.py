from django.urls import path
from ProyectoBlogApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('eventoformulario/', views.eventoformulario, name="eventoformulario"),
    path('plataforma/', views.plataforma, name="plataforma"),
    path('crearparticipante/', views.crearparticipante, name="crearparticipante"),
    path('buscarparticipante/', views.buscarparticipante, name="buscarparticipante"),
    path('buscarparticipante2/', views.buscarparticipante2, name="buscarparticipante2"),
    path('bienvenida/', views.bienvenida, name="bienvenida"),
    path('evento/', views.evento, name="evento"),
    path('buscarevento/', views.buscarevento, name="buscarevento"),
    path('buscar/', views.buscar, name="buscar"),
    path('errorformulario/', views.errorformulario, name="errorformulario"),
    path('agradecimiento/', views.agradecimiento, name="agradecimiento"),
    path('buscareventosugerido/', views.buscareventosugerido, name="buscareventosugerido"),
    path('buscareventosug2/', views.buscareventosug2, name="buscareventosug2"),

    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name="ProyectoBlogApp/logout.html"), name='Logout'),

    path("editarPerfil/", views.editarPerfil, name='EditarPerfil'),
    path("perfil/", views.perfil, name='Perfil'),

    path('actualizarAvatar/<int:pk>/', views.UpdateAvatar.as_view(), name='actualizarAvatar'),
    path('avatarView/', views.AvatarUserList.as_view(), name='AvatarView'),
    path('crearAvatar/', views.AvatarCreate.as_view(), name='AvatarCreate'),
    path('eliminaAvatar/<pk>/', views.AvatarDelete.as_view(), name='DeleteAvatar'),
    path('agregarAvatar/', views.agregarAvatar, name='AgregarAvatar'),

    path('crearcontacto/', views.crearContacto.as_view(), name='crearcontacto'),
    path('contacto_gracias/', views.contacto_gracias, name='contacto_gracias'),

    path('listaPost/',views.VistaPost.as_view(), name='listaPost'),
    path('detalle/<int:pk>', views.DetallePost.as_view(), name='DetallePost'),
    path('crearPost/', views.CrearPost.as_view(), name='CrearPost'),
    path('actualizarPost/<int:pk>/', views.ActualizarPost.as_view(), name='actualizarPost'),
    path('borrarPost/<int:pk>/', views.BorrarPost.as_view(), name='BorrarPost'),

    path('aboutMe/', views.aboutMe, name='aboutMe'),
]