from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.generic import FormView
from .models import Animal, Reptile, Bird, Habitat_area, Feeding_ration, User
from .forms import AddAn, AddHa, AddUser, AddRa, AddRept, AddBird
from django.views import generic
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from firstapp import forms

#Определение главных страниц и просмотра данных


def great(request):
    return render(request, "great.html")

def index(request):
    return render(request, "index.html")



def index_animal(request): #index_author
    form_add = AddAn()
    data = Animal.objects.all()
    return render(request, "firstapp/Template_Animal.html", {"form":form_add, "data_show":data})

def index_habitat_area(request): #index_exhibition
    form_ex = AddHa()
    data = Habitat_area.objects.all()
    return render(request, "firstapp/Template_Habitat_area.html", {"form":form_ex, "data_show":data})

def index_feeding_ration(request):
    form_er = AddRa()
    data = Feeding_ration.objects.all()
    return render(request, "firstapp/Template_Feeding_ration.html", {"form":form_er, "data_show":data})

def index_user(request):
    form_ca = AddUser()
    data = User.objects.all()
    return render(request, "firstapp/Template_User.html", {"form":form_ca, "data_show":data})

def index_reptile(request):
    form_ra = AddRept()
    data = Reptile.objects.all()
    return render(request, "firstapp/Template_Reptile.html", {"form":form_ra, "data_show":data})

def index_bird(request):
    form_b = AddBird()
    data = Bird.objects.all()
    return render(request, "firstapp/Template_Bird.html", {"form":form_b, "data_show":data})

#Определение view

class view_feeding_ration(View):
    def add_feeding_ration(request):
        if request.method == "POST":
            ration = Feeding_ration()
            ration.name = request.POST.get("name")
            ration.type = request.POST.get("type")
            ration.save()
            return HttpResponseRedirect("/ration")

    def del_feeding_ration(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Feeding_ration.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/ration")

    def update_feeding_ration(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Feeding_ration.objects.get(id=q)
            que.name = request.POST.get("name")
            que.type = request.POST.get("type")
            que.save()
            return HttpResponseRedirect("/ration")

class view_user(View):
    def add_user(request):
        if request.method == "POST":
            user = User()
            user.name = request.POST.get("name")
            user.phone = request.POST.get("phone")
            user.position = request.POST.get("position")
            user.birthday = request.POST.get("birthday")
            user.marital_status = request.POST.get("marital_status")
            user.save()
            return HttpResponseRedirect("/user")

    def del_user(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = User.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/user")

    def update_user(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = User.objects.get(id=q)
            que.name = request.POST.get("name")
            que.phone = request.POST.get("phone")
            que.position = request.POST.get("position")
            que.marital_status = request.POST.get("marital_status")
            que.save()
            return HttpResponseRedirect("/user")

class view_habitat_area(View):
    def add_habitat_area(request):
        if request.method == "POST":
            area = Habitat_area()
            area.name = request.POST.get("name")
            area.characteristic = request.POST.get("characteristic")
            area.save()
            return HttpResponseRedirect("/area")

    def del_habitat_area(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Habitat_area.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/area")

    def update_habitat_area(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Habitat_area.objects.get(id=q)
            que.name = request.POST.get("name")
            que.characteristic = request.POST.get("characteristic")
            que.save()
            return HttpResponseRedirect("/area")

class view_animal(View):
    def add_animal(request):
        if request.method == "POST":
            animal = Animal()
            animal.name = request.POST.get("name")
            animal.birthday = request.POST.get("birthday")
            animal.gender = request.POST.get("gender")
            animal.type = request.POST.get("type")
            animal.area_id = Habitat_area.objects.get(id=request.POST.get("area_id"))
            animal.ration_id = Feeding_ration.objects.get(id=request.POST.get("ration_id"))
            animal.caretaker_id = User.objects.get(id=request.POST.get("caretaker_id"))
            animal.veterenarian_id = User.objects.get(id=request.POST.get("veterenarian_id"))

            animal.save()
            return HttpResponseRedirect("/animal")

    def del_animal(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Animal.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/animal")

    def update_animal(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Animal.objects.get(id=q)
            que.name = request.POST.get("name")
            que.birthday = request.POST.get("birthday")
            que.gender = request.POST.get("gender")
            que.type = request.POST.get("type")
            que.area_id = Habitat_area.objects.get(id=request.POST.get("area_id"))
            que.ration_id = Feeding_ration.objects.get(id=request.POST.get("ration_id"))
            que.caretaker_id = User.objects.get(id=request.POST.get("caretaker_id"))
            que.veterenarian_id = User.objects.get(id=request.POST.get("veterenarian_id"))

            que.save()
            return HttpResponseRedirect("/animal")

class view_bird(View):
    def add_bird(request):
        if request.method == "POST":
            bird = Bird()
            bird.wintering_place = request.POST.get("wintering_place")
            bird.date_of_arrival = request.POST.get("date_of_arrival")
            bird.flight_date = request.POST.get("flight_date")
            bird.animal_id = Animal.objects.get(id=request.POST.get("animal_id"))
            bird.save()
            return HttpResponseRedirect("/bird")

    def del_bird(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Bird.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/bird")

    def update_bird(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Bird.objects.get(id=q)
            que.wintering_place = request.POST.get("wintering_place")
            que.date_of_arrival = request.POST.get("date_of_arrival")
            que.flight_date = request.POST.get("flight_date")
            que.animal_id = Animal.objects.get(id=request.POST.get("animal_id"))
            que.save()
            return HttpResponseRedirect("/bird")

class view_reptile(View):
    def add_reptile(request):
        if request.method == "POST":
            reptile = Reptile()
            reptile.normal_temperature = request.POST.get("normal_temperature")
            reptile.hibernation_period = request.POST.get("hibernation_period")
            reptile.animal_id = Animal.objects.get(id=request.POST.get("animal_id"))
            reptile.save()
            return HttpResponseRedirect("/reptile")

    def del_reptile(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Reptile.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/reptile")

    def update_reptile(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Reptile.objects.get(id=q)
            que.normal_temperature = request.POST.get("normal_temperature")
            que.hibernation_period = request.POST.get("hibernation_period")
            que.animal_id = Animal.objects.get(id=request.POST.get("animal_id"))
            que.save()
            return HttpResponseRedirect("/reptile")


