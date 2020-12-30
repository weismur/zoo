from django.contrib import admin
from .models import Animal, Reptile, Bird, Habitat_area, Feeding_ration, User

#admin.site.register(User)
#admin.site.register(Animal)
#admin.site.register(Reptile)
#admin.site.register(Bird)
#admin.site.register(Habitat_area)
#admin.site.register(Feeding_ration)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','phone','position','birthday','marital_status')

@admin.register(Reptile)
class ReptileAdmin(admin.ModelAdmin):
    list_display = ('normal_temperature','hibernation_period')

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name','birthday','gender','type')

@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ('wintering_place','date_of_arrival','flight_date')

@admin.register(Habitat_area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name','characteristic')

@admin.register(Feeding_ration)
class RationAdmin(admin.ModelAdmin):
    list_display = ('name','type')

