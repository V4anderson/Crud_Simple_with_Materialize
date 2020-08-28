from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse 
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    dicio = {}
    dicio['Person'] = Person.objects.all()
    return render(request, 'index.html',dicio)

def cadastro(request):
    dicio = {}
    form = PersonForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    else:
        dicio['form'] = form
        return render (request, 'cadastro.html',dicio)
def atualizar(request,id):
    dicio = get_object_or_404(Person,pk=id)
    formulario = PersonForm(request.POST or None, instance=dicio)

    if formulario.is_valid():
       formulario.save()
       return redirect('url_home')

    else:
        dicio={"form":formulario}
        return render(request,'cadastro.html',dicio)  

def deletar(request,id):
    dicio = get_object_or_404(Person,pk=id)
    formulario = PersonForm(request.POST or None, instance=dicio)

    if request.method=="POST":
       dicio.delete()
       return redirect('url_home')

    else:
        dicio={"form":formulario
        ,"delete":dicio
        }
        return render(request,'deletando.html',dicio)

