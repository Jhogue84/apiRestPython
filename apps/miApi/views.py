from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Producto2
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class ProductoView(View):

    #metodo que se ejecuta simpre en una peticion. Despachar o enviar
    #
    @method_decorator(csrf_exempt)
    #def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):#para listar un producto, o varios, aumentamos el id e iniciamos a cero.
        #listar todos los productos
        if (id>0):
            productos = list(Producto2.objects.filter(id=id).values())
            if len(productos) > 0:
                producto=productos[0]
                datos={"mensaje": 'Existoso', 'producto': producto}
            else:
                datos={'mensaje': 'No existen productos, para listar'}
            return JsonResponse(datos)
        else:
            #productos = Producto2.objects.all()
            productos = list(Producto2.objects.values())
            if len(productos)>0:
                datos={'mensaje':"Lista Exitosa", 'Productos':productos}
            else:
                datos = {"mensaje": "No existen productos, para listar"}
            return JsonResponse(datos)
    
    def post(self, request):
        #CSRF: erro peticiones, ahor exoneramos este token.
        #print(request.body)#veo en consola el formato, pero no sirve para python
        jsonDatos = json.loads(request.body)#tengo un diccionario de python
        #print(jsonDatos)
        Producto2.objects.create(codigo=jsonDatos['codigo'],producto=jsonDatos['producto'], precio=jsonDatos['precio'], marca=jsonDatos['marca'])
        datos = {'mensaje': "Insercion exitosa."}
        return JsonResponse(datos)

    def put(self, request, id):#para editar, aumentamos el parametro id
        jsonDatos = json.loads(request.body)
        productos = list(Producto2.objects.filter(id=id).values())
        if len(productos) > 0:
            productos = Producto2.objects.get(id=id)
            productos.codigo = jsonDatos['codigo']
            productos.producto = jsonDatos['producto']
            productos.precio = jsonDatos['precio']
            productos.marca = jsonDatos['marca']
            productos.save()
            datos = {'mensaje': 'Modificacion exitosa.'}
        else:
            datos = {'mensaje':'Producto no encontrado para modificar.'}
        return JsonResponse(datos)

    def delete(self, request, id):
        productos = list(Producto2.objects.filter(id=id).values())
        if len(productos) > 0:
            Producto2.objects.filter(id=id).delete()
            datos = {'mensaje': 'Eliminacion Satisfactoria'}
        else:
            datos = {'message': 'Producto no encontrado. Eliminar'}
        return JsonResponse(datos)
