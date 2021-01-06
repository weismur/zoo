from django.test import TestCase
import unittest
from firstapp.models import Animal,Reptile,Bird,Habitat_area,Feeding_ration,User
# Create your tests here.
from firstapp.models import Habitat_area
from django.urls import reverse
from firstapp.forms import AddAn,AddHa,AddUser,AddBird,AddRa,AddRept

class AreaViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Habitat_area.objects.create(name='Тундра' , characteristic = 'холодно и голодно')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/area/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('area'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('area'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Habitat_area.html')

class RationViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Feeding_ration.objects.create(name='Малыш ' , type = 'детский ')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/ration/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('ration'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('ration'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Feeding_ration.html')

class UserViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='Вайс Диего Альбертович', phone='88888', position='Смотритель', birthday='12.12.2000', marital_status='не замужем')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/user/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('user'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('user'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_User.html')

class AnimalViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Animal.objects.create(name='Мурка', birthday='12.12.2019', gender='женский',type='животное')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/animal/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('animal'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('animal'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Animal.html')

class BirdViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Bird.objects.create(wintering_place='Япония', date_of_arrival='20/11/2001', flight_date='22/11/2001')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/bird/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('bird'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('bird'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Bird.html')

class ReptileViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Reptile.objects.create(hibernation_period='20/11/2000-30/12/2000',normal_temperature='26')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/reptile/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('reptile'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('reptile'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_Reptile.html')

class AnotherViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='Вайс Диего Альбертович', phone='88888', position='Смотритель', birthday='12.12.2000', marital_status='не замужем')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/zoo/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_view_url_exists_at_desired_location1(self): # существование url по адресу
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name1(self): # существование url по имени
        resp = self.client.get(reverse('great'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template1(self): # соответствие шаблону
        resp = self.client.get(reverse('great'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'great.html')