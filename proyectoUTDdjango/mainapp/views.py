from django.shortcuts import render,HttpResponse, redirect
""" from django.contrib.auth.forms import UserCreationForm """
from mainapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request,'mainapp/index.html',{
        'title':'Inicio',
        'content':'.:: ¡ Bienvenido a mi página de inicio !::.'
    })

def about(request):
    return render(request,'mainapp/about.html',{
        'title':'Acerca de',
        'content':'.:: ¡ Somos un equipo de desarrollo de software !::.'
    })

def mision(request):
    return render(request,'mainapp/mision.html',{
        'title':'Mision',
    })

def vision(request):
    return render(request,'mainapp/vision.html',{
        'title':'Vision',
    })
def registro(request):
    return render(request,'mainapp/registro.html',{
        'title':'Registro',
    })
def inicioSesion(request):
    return render(request,'mainapp/inicioSesion.html',{
        'title':'Inicio de Sesión',
    })
    
""" def error404(request,exception):
    return render(request,'errors/error404.html',{
        'title':'Error 404',
        'content':'''<h2>ERROR 404</h2>
        </p>lO SENTIMOS NO PUDIMOS ENCONTRAR TU PAGINA <a class+="backhome" href={% url "mainapp/index.html" %}>regresar a inicio</a></p>'''
    }) """
    
""" def error404(request, exception):
    return redirect('inicio')
    
def error500(request):
    return render(request, 'errors/error500.html', {
        'title': 'Error 500',
        'content': '''<h2>ERROR 500</h2>
        <p>Ocurrió un error en el servidor. <a href="{% url 'inicio' %}">Regresar a inicio</a></p>'''
    }) """
    
def error404(request,exception):
    return render(request, 'errors/error404.html')

def register_user(request):
    if request.user.is_authenticated:
        redirect('inicio')
    else:
        register_form=RegisterForm()
        
        if request.method == "POST":
            register_form = RegisterForm(request.POST)
            
            if register_form.is_valid():
                register_form.save()
                messages.success(request,'Te has registrado correctamente')
                return redirect('inicio')
                
        return render(request,'mainapp/registro.html',{
            'title':'Registro',
            'register_form':register_form
        })
        
def login_user(request):
    return render(request,'mainapp/inicioSesion.html',{
        'title':'Inicio de Sesión',
    })