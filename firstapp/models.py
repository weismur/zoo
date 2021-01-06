from django.db import models

class Habitat_area(models.Model):
    name = models.CharField(max_length=45)
    characteristic = models.CharField(max_length=500)
    objects = models.Manager()

class Feeding_ration(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    objects = models.Manager()

class Animal(models.Model):
    name = models.CharField(max_length=40)
    birthday = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=40)
    area_id = models.ForeignKey('Habitat_area', on_delete=models.CASCADE,null=True)
    ration_id = models.ForeignKey('Feeding_ration', on_delete=models.CASCADE,null=True)
    caretaker_id = models.ForeignKey('User', on_delete=models.CASCADE,related_name='caretaker_id',null=True)
    veterenarian_id = models.ForeignKey('User', on_delete=models.CASCADE,related_name='veterenarian_id',null=True)
    objects = models.Manager()

class Reptile(models.Model):
    normal_temperature = models.CharField(max_length=40)
    hibernation_period = models.TextField(max_length=45,null=True)
    animal_id = models.ForeignKey('Animal', on_delete=models.CASCADE,null=True)
    objects = models.Manager()


class Bird(models.Model):
    wintering_place = models.CharField(max_length=40)
    date_of_arrival = models.CharField(max_length=20)
    flight_date = models.CharField(max_length=20)
    animal_id = models.ForeignKey('Animal', on_delete=models.CASCADE,null=True)
    objects = models.Manager()

class User(models.Model):
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=40)
    position = models.CharField(max_length=45)
    birthday = models.CharField(max_length=45)
    marital_status = models.CharField(max_length=90)
    objects = models.Manager()











