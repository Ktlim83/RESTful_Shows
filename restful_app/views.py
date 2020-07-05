from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, "shows.html", context)  


def new(request): 
    return render(request, "new.html")  


def create(request):
    # CREATE SHOW  
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description'],
    )
    print(request.POST)
    return redirect('/shows') 


def edit(request, show_id):
    # Querys a show with its show id
    # Capture the variable and object, then adding it back into context 
    one_show = Show.objects.get(id=show_id)
    context = {
         'show' : one_show
    }
    return render(request, "edit.html", context)   


def update(request, show_id):
    #  UPDATES THE SHOW
    update_show = Show.objects.get(id=show_id)
    # UPDATE EACH FIELD
    update_show.title = request.POST['title']
    update_show.network = request.POST['network']
    update_show.release_date = request.POST['release_date']
    update_show.description = request.POST['description']
    update_show.save()
    
    
    return redirect('/shows/')
 

def delete(request, show_id):
    # DELETE SHOW
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/shows')  


def show(request, show_id):
    # Querys a show with its show id
    # Capture the variable and object, then adding it back into context 
    one_show = Show.objects.get(id=show_id)
    context = {
         'show' : one_show
    }
    return render(request, "show.html", context)  
