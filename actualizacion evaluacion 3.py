from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import  Usuario, Precio,Categoria,Supermercado
from django.contrib.auth.models import User  # Importa el modelo de Usuario de Django
#---------------------------------------------------------------------------------
from .forms import CategoriaForm, PrecioForm, SupermercadoForm, UsuarioForm, RegistroFormulario
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoría, Precio, Supermercado, Usuario
from django.http import HttpResponse


# Create your views here.
def Pagina1(request):
    usuario = Usuario.objects.all()

    data = {
        'usuarios': usuario
    }
    return render(request, 'usuario/Pagina1.html',  data)


# Vistas para Categoría
def lista_categorias(request):
    categorias = categorias.objects.all()
    return render(request, 'usuario/lista_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'usuario/crear_categoria.html', {'form': form})

def editar_categoria(request, pk):
    categoria = get_object_or_404(categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'usuario/editar_categoria.html', {'form': form, 'categoria': categoria})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'usuario/confirmar_eliminar.html', {'categoria': categoria})

def lista_precios(request):
    # Tu lógica para manejar la vista de lista de precios
    return HttpResponse("Vista de lista de precios")


def crear_precio(request):
    # Tu lógica para crear un nuevo precio
    return HttpResponse("Formulario para crear un nuevo precio")

def editar_precio(request, pk):
    precio = get_object_or_404(Precio, pk=pk)
    # Tu lógica para editar el precio
    return HttpResponse(f"Formulario para editar el precio con ID {pk}")
def eliminar_precio(request, pk):
    precio = get_object_or_404(Precio, pk=pk)
    # Tu lógica para eliminar el precio
    return HttpResponse(f"Eliminar el precio con ID {pk}")

def lista_supermercados(request):
    # Tu lógica para mostrar la lista de supermercados
    return HttpResponse("Aquí va la lista de supermercados")

def crear_supermercado(request):
    # Tu lógica para mostrar la lista de supermercados
    return HttpResponse("Aquí va la creacion de supermercados")

def editar_supermercado(request, pk):
    # Obtenemos el supermercado por su ID
    supermercado = get_object_or_404(Supermercado, pk=pk)

    # Lógica para editar el supermercado
    if request.method == 'POST':
        # Procesar el formulario de edición si se envió
        # Aquí deberías tener lógica para actualizar el supermercado
        return HttpResponse(f"Supermercado actualizado con ID {pk}")
    else:
        # Mostrar el formulario de edición
        return HttpResponse(f"Formulario para editar supermercado con ID {pk}")

def eliminar_supermercado(request, pk):
    # Obtenemos el supermercado por su ID
    supermercado = get_object_or_404(Supermercado, pk=pk)

    # Lógica para eliminar el supermercado
    if request.method == 'POST':
        # Procesar la eliminación si se envió confirmación
        # Aquí deberías tener lógica para eliminar el supermercado
        return HttpResponse(f"Supermercado eliminado con ID {pk}")
    else:
        # Mostrar confirmación de eliminación
        return HttpResponse(f"¿Seguro que deseas eliminar el supermercado con ID {pk}?")

def lista_usuarios(request):
    # Obtiene todos los usuarios
    usuarios = User.objects.all()
    return render(request, 'usuario/lista_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, pk):
    # Obtiene un usuario por su ID
    usuario = get_object_or_404(User, pk=pk)
    return render(request, 'usuario/detalle_usuario.html', {'usuario': usuario})

def registrar(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario y el usuario en la base de datos
            # Redirigir o mostrar un mensaje de éxito
            return redirect('pagina_inicio')  # Cambia 'pagina_inicio' por el nombre de tu URL de inicio
    else:
        form = RegistroFormulario()
    
    return render(request, 'registro_usuario.html', {'form': form})

def editar_usuario(request, pk):
    # Obtiene un usuario por su ID
    usuario = get_object_or_404(User, pk=pk)

    # Lógica para editar el usuario
    if request.method == 'POST':
        # Procesar el formulario de edición si se envió
        # Aquí deberías tener lógica para actualizar el usuario
        return HttpResponse(f"Usuario actualizado con ID {pk}")
    else:
        # Mostrar el formulario de edición
        return render(request, 'usuario/editar_usuario.html', {'usuario': usuario})

def eliminar_usuario(request, pk):
    # Obtiene un usuario por su ID
    usuario = get_object_or_404(User, pk=pk)

    # Lógica para eliminar el usuario
    if request.method == 'POST':
        # Procesar la eliminación si se envió confirmación
        # Aquí deberías tener lógica para eliminar el usuario
        return HttpResponse(f"Usuario eliminado con ID {pk}")
    else:
        # Mostrar confirmación de eliminación
        return render(request, 'usuario/eliminar_usuario.html', {'usuario': usuario})
    

    
from django.shortcuts import render, redirect
from .forms import RegistroFormulario
from django.contrib.auth.models import User
from django.contrib import messages

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('Pagina1')  # Cambia 'Pagina1' por la URL adecuada
    else:
        form = RegistroFormulario()

    context = {
        'form': form,
    }
    return render(request, 'registro.html', context)



#----------------------------------------------------------------------------

    

def Pagina2(request):

    return render(request, 'usuario/Pagina2.html')

def Pagina3(request):

    return render(request, 'usuario/Pagina3.html')

def Pagina4(request):

    return render(request, 'usuario/Pagina4.html')

def Pagina5(request):

    return render(request, 'usuario/Pagina5.html')

def Pagina6(request):

    return render(request, 'usuario/Pagina6.html')

def registrar(request):
    Nombre_User = request.POST['nombre']
    Correo = request.POST['email']
    contraseña = request.POST['contraseña']

    usuarios = Usuario.objects.create(Nombre_User = Nombre_User, contraseña=contraseña, Correo = Correo)
    return redirect('/')