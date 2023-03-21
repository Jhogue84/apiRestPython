from django.urls import path
from .views import ProductoView

urlpatterns = [
    path('productos/', ProductoView.as_view(), name='productos_list'),
    path('productos/<int:id>', ProductoView.as_view(), name='productos_proceso')#para eliminar y editar.
   
]
