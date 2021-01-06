from django.test import TestCase
import unittest
from firstapp.forms import AddAn,AddHa,AddUser,AddBird,AddRa,AddRept
# Create your tests here.

class AddHaFormTest(TestCase):

    def test_name_label(self):
        form = AddHa()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Название зоны обитания')

    def test_characteristic_label(self):
        form = AddHa()
        self.assertTrue(form.fields['characteristic'].label == None or form.fields['characteristic'].label == 'описание зоны обитания')

    def test_proverka(self):
        form = AddHa(data={'name': "Тайга", 'characteristic': "лесистая местность"})
        self.assertTrue(form.is_valid())

class AddRaFormTest(TestCase):

    def test_name_label(self):
        form = AddRa()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Название рациона')

    def test_type_label(self):
        form = AddRa()
        self.assertTrue(form.fields['type'].label == None or form.fields['type'].label == 'Тип рациона')

    def test_proverka(self):
        form = AddRa(data={'name': "Малыш", 'type': "детский"})
        self.assertTrue(form.is_valid())

class AddUserFormTest(TestCase):

    def test_name_label(self):
        form = AddUser()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'ФИО пользователя')

    def test_phone_label(self):
        form = AddUser()
        self.assertTrue(form.fields['phone'].label == None or form.fields['phone'].label == 'Номер телефона')

    def test_position_label(self):
        form = AddUser()
        self.assertTrue(form.fields['position'].label == None or form.fields['position'].label == 'Должность')

    def test_birthday_label(self):
        form = AddUser()
        self.assertTrue(form.fields['birthday'].label == None or form.fields['birthday'].label == 'День рождения')

    def test_marital_status_label(self):
        form = AddUser()
        self.assertTrue(form.fields['marital_status'].label == None or form.fields['marital_status'].label == 'семейное положение')

    def test_proverka(self):
        form = AddUser(data={'name': "Захаров Марк Игоревич", 'phone': "88858", 'position': "Cмотритель", 'birthday': "20/11/1897", 'marital_status': "не женат"})
        self.assertTrue(form.is_valid())

class AddAnFormTest(TestCase):

    def test_name_label(self):
        form = AddAn()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Имя')

    def test_birthday_label(self):
        form = AddAn()
        self.assertTrue(form.fields['birthday'].label == None or form.fields['birthday'].label == 'Дата рождения')

    def test_gender_label(self):
        form = AddAn()
        self.assertTrue(form.fields['gender'].label == None or form.fields['gender'].label == 'Пол')

    def test_type_label(self):
        form = AddAn()
        self.assertTrue(form.fields['type'].label == None or form.fields['type'].label == 'Тип')

    def test_area_id_label(self):
        form = AddAn()
        self.assertTrue(form.fields['area_id'].label == None or form.fields['area_id'].label == 'Зона обитания')

    def test_ration_id_label(self):
        form = AddAn()
        self.assertTrue(form.fields['ration_id'].label == None or form.fields['ration_id'].label == 'Рацион')

    def test_caretaker_id_label(self):
        form = AddAn()
        self.assertTrue(form.fields['caretaker_id'].label == None or form.fields['caretaker_id'].label == 'Смотритель')

    def test_veterenarian_id_label(self):
        form = AddAn()
        self.assertTrue(form.fields['veterenarian_id'].label == None or form.fields['veterenarian_id'].label == 'Ветеринар')

    def test_proverka(self):
        form = AddAn(data={'name': "Борис", 'birthday': "20/11/1998",'gender': "мужской",'type': "животное",'area_id': 1, 'ration_id': 1,'caretaker_id': 1,'veterenarian_id': 1})
        self.assertTrue(form.is_valid())

class AddBirdFormTest(TestCase):

    def test_wintering_place_label(self):
        form = AddBird()
        self.assertTrue(form.fields['wintering_place'].label == None or form.fields['wintering_place'].label == 'Название страны')

    def test_date_of_arrival_label(self):
        form = AddBird()
        self.assertTrue(form.fields['date_of_arrival'].label == None or form.fields['date_of_arrival'].label == 'Дата отлёта')

    def test_flight_date_label(self):
        form = AddBird()
        self.assertTrue(form.fields['flight_date'].label == None or form.fields['flight_date'].label == 'Дата прилёта')

    def test_animal_id_label(self):
        form = AddBird()
        self.assertTrue(form.fields['animal_id'].label == None or form.fields['animal_id'].label == 'Номер животного')

    def test_proverka(self):
        form = AddBird(data={'wintering_place': "Канада", 'date_of_arrival': "20/10/2005",'flight_date': "23/10/2005", 'animal_id': 1})
        self.assertTrue(form.is_valid())

class AddReptFormTest(TestCase):

    def test_normal_temperature_label(self):
        form = AddRept()
        self.assertTrue(form.fields['normal_temperature'].label == None or form.fields['normal_temperature'].label == 'Нормальная температура')

    def test_type_label(self):
        form = AddRept()
        self.assertTrue(form.fields['hibernation_period'].label == None or form.fields['hibernation_period'].label == 'Срок зимней спячки')

    def test_animal_id_label(self):
        form = AddBird()
        self.assertTrue(form.fields['animal_id'].label == None or form.fields['animal_id'].label == 'Номер животного')

    def test_proverka(self):
        form = AddRept(data={'normal_temperature': "27", 'hibernation_period': "28.12.1998-28.02.1999", 'animal_id': 1})
        self.assertTrue(form.is_valid())