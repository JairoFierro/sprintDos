from django.urls import path
from .views import crear_usuario, pagina_principal, procesar_pago, usuario_padre_familia_edit_view, procesar_pago, pago_pendiente 
urlpatterns = [
    path('', pagina_principal, name='pagina_principal'), 
    path('procesar_pago/', procesar_pago, name='procesar_pago'), 
    path('editar_usuario/', usuario_padre_familia_edit_view, name='editar_usuario'),
    path('crear-usuario/', crear_usuario, name='crear_usuario'),
    path('gerente/pagosPendientes/', pago_pendiente, name='pago_pendiente'),
]
