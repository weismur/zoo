from django.test import TestCase
import unittest
from firstapp.models import Animal,Reptile,Bird,Habitat_area,Feeding_ration,User
# Create your tests here.

class Habitat_areaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Habitat_area.objects.create(name='Тайга', characteristic='биом, для которого характерно преобладание хвойных лесов.')

    def test_name_label(self):
        area=Habitat_area.objects.get(id=1)
        field_label = area._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_characteristic_label(self):
        area=Habitat_area.objects.get(id=1)
        field_label = area._meta.get_field('characteristic').verbose_name
        self.assertEquals(field_label,'characteristic')

    def test_name_max_length(self):
        area=Habitat_area.objects.get(id=1)
        max_length = area._meta.get_field('name').max_length
        self.assertEquals(max_length,45)

    def test_characteristic_max_length(self):
        area=Habitat_area.objects.get(id=1)
        max_length = area._meta.get_field('characteristic').max_length
        self.assertEquals(max_length,500)

class Feeding_rationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Feeding_ration.objects.create(name='Малыш', type='детский')

    def test_name_label(self):
        ration=Feeding_ration.objects.get(id=1)
        field_label = ration._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_type_label(self):
        ration=Feeding_ration.objects.get(id=1)
        field_label = ration._meta.get_field('type').verbose_name
        self.assertEquals(field_label,'type')

    def test_name_max_length(self):
        ration=Feeding_ration.objects.get(id=1)
        max_length = ration._meta.get_field('name').max_length
        self.assertEquals(max_length,45)

    def test_type_max_length(self):
        ration=Feeding_ration.objects.get(id=1)
        max_length = ration._meta.get_field('type').max_length
        self.assertEquals(max_length,45)

class AnimalModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Animal.objects.create(name='Мурка', birthday='12.12.2019', gender='женский',type='животное')

    def test_name_label(self):
        animal=Animal.objects.get(id=1)
        field_label = animal._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_birthday_label(self):
        animal=Animal.objects.get(id=1)
        field_label = animal._meta.get_field('birthday').verbose_name
        self.assertEquals(field_label,'birthday')

    def test_gender_label(self):
        animal=Animal.objects.get(id=1)
        field_label = animal._meta.get_field('gender').verbose_name
        self.assertEquals(field_label,'gender')

    def test_type_label(self):
        animal=Animal.objects.get(id=1)
        field_label = animal._meta.get_field('type').verbose_name
        self.assertEquals(field_label,'type')

    def test_name_max_length(self):
        animal=Animal.objects.get(id=1)
        max_length = animal._meta.get_field('name').max_length
        self.assertEquals(max_length,40)

    def test_birthday_max_length(self):
        animal=Animal.objects.get(id=1)
        max_length = animal._meta.get_field('birthday').max_length
        self.assertEquals(max_length,20)

    def test_gender_max_length(self):
        animal=Animal.objects.get(id=1)
        max_length = animal._meta.get_field('gender').max_length
        self.assertEquals(max_length,20)

    def test_type_max_length(self):
        animal=Animal.objects.get(id=1)
        max_length = animal._meta.get_field('type').max_length
        self.assertEquals(max_length,40)

class ReptileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Reptile.objects.create(hibernation_period='20/11/2000-30/12/2000',normal_temperature='26')

    def test_normal_temperature_label(self):
        reptile=Reptile.objects.get(id=1)
        field_label = reptile._meta.get_field('normal_temperature').verbose_name
        self.assertEquals(field_label,'normal temperature')

    def test_hibernation_period_label(self):
        reptile=Reptile.objects.get(id=1)
        field_label = reptile._meta.get_field('hibernation_period').verbose_name
        self.assertEquals(field_label,'hibernation period')

    def test_normal_temperature_max_length(self):
        reptile=Reptile.objects.get(id=1)
        max_length = reptile._meta.get_field('normal_temperature').max_length
        self.assertEquals(max_length,40)

    def test_hibernation_period_max_length(self):
        reptile=Reptile.objects.get(id=1)
        max_length = reptile._meta.get_field('hibernation_period').max_length
        self.assertEquals(max_length,45)

class BirdModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Bird.objects.create(wintering_place='Япония', date_of_arrival='20/11/2001', flight_date='22/11/2001')

    def test_wintering_place_label(self):
        bird=Bird.objects.get(id=1)
        field_label = bird._meta.get_field('wintering_place').verbose_name
        self.assertEquals(field_label,'wintering place')

    def test_date_of_arrival_label(self):
        bird=Bird.objects.get(id=1)
        field_label = bird._meta.get_field('date_of_arrival').verbose_name
        self.assertEquals(field_label,'date of arrival')

    def test_flight_date_label(self):
        bird=Bird.objects.get(id=1)
        field_label = bird._meta.get_field('flight_date').verbose_name
        self.assertEquals(field_label,'flight date')

    def test_wintering_place_max_length(self):
        bird=Bird.objects.get(id=1)
        max_length = bird._meta.get_field('wintering_place').max_length
        self.assertEquals(max_length,40)

    def test_date_of_arrival_max_length(self):
        bird=Bird.objects.get(id=1)
        max_length = bird._meta.get_field('date_of_arrival').max_length
        self.assertEquals(max_length,20)

    def test_flight_date_max_length(self):
        bird=Bird.objects.get(id=1)
        max_length = bird._meta.get_field('flight_date').max_length
        self.assertEquals(max_length,20)

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create(name='Вайс Диего Альбертович', phone='88888', position='Смотритель', birthday='12.12.2000', marital_status='не замужем')

    def test_name_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_phone_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('phone').verbose_name
        self.assertEquals(field_label,'phone')

    def test_position_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('position').verbose_name
        self.assertEquals(field_label,'position')

    def test_birthday_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('birthday').verbose_name
        self.assertEquals(field_label,'birthday')

    def test_marital_status_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('marital_status').verbose_name
        self.assertEquals(field_label,'marital status')

    def test_name_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEquals(max_length,45)

    def test_birthday_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('birthday').max_length
        self.assertEquals(max_length,45)

    def test_phone_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('phone').max_length
        self.assertEquals(max_length,40)

    def test_position_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('position').max_length
        self.assertEquals(max_length,45)

    def test_marital_status_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('marital_status').max_length
        self.assertEquals(max_length,90)