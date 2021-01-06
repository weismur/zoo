from django import forms

class AddAn(forms.Form):
    name = forms.CharField(label="Имя",widget=forms.TextInput(attrs={"class":"myfield"}))
    birthday = forms.CharField(label="Дата рождения",widget=forms.TextInput(attrs={"class":"myfield"}))
    gender = forms.CharField(label="Пол",widget=forms.TextInput(attrs={"class":"myfield"}))
    type = forms.CharField(label="Тип",widget=forms.TextInput(attrs={"class":"myfield"}))
    area_id = forms.IntegerField(label="Зона обитания", widget=forms.NumberInput(attrs={"class": "myfield"}))
    ration_id = forms.IntegerField(label="Рацион", widget=forms.NumberInput(attrs={"class": "myfield"}))
    caretaker_id = forms.IntegerField(label="Смотритель", widget=forms.NumberInput(attrs={"class": "myfield"}))
    veterenarian_id = forms.IntegerField(label="Ветеринар", widget=forms.NumberInput(attrs={"class": "myfield"}))


class AddHa(forms.Form):
    name = forms.CharField(label="Название зоны обитания",widget=forms.TextInput(attrs={"class":"myfield"}))
    characteristic = forms.CharField(label="описание зоны обитания",widget=forms.TextInput(attrs={"class":"myfield"}))

class AddUser(forms.Form):
    name = forms.CharField(label="ФИО пользователя",widget=forms.TextInput(attrs={"class":"myfield"}))
    phone = forms.CharField(label="Номер телефона",widget=forms.TextInput(attrs={"class":"myfield"}))
    position = forms.CharField(label="Должность",widget=forms.TextInput(attrs={"class":"myfield"}))
    birthday = forms.CharField(label="День рождения",widget=forms.TextInput(attrs={"class":"myfield"}))
    marital_status = forms.CharField(label="семейное положение",widget=forms.TextInput(attrs={"class":"myfield"}))

class AddRa(forms.Form):
    name = forms.CharField(label="Название рациона",widget=forms.TextInput(attrs={"class":"myfield"}))
    type = forms.CharField(label="Тип рациона",widget=forms.TextInput(attrs={"class":"myfield"}))

class AddRept(forms.Form):
    normal_temperature = forms.CharField(label="Нормальная температура",widget=forms.NumberInput(attrs={"class":"myfield"}))
    hibernation_period = forms.CharField(label="Срок зимней спячки",widget=forms.TextInput(attrs={"class":"myfield"}))
    animal_id = forms.IntegerField(label="Номер животного", widget=forms.NumberInput(attrs={"class": "myfield"}))

class AddBird(forms.Form):
    wintering_place = forms.CharField(label="Название страны",widget=forms.TextInput(attrs={"class":"myfield"}))
    date_of_arrival = forms.CharField(label="Дата отлёта",widget=forms.DateInput(attrs={"class":"myfield"}))
    flight_date = forms.CharField(label="Дата прилёта",widget=forms.DateInput (attrs={"class":"myfield"}))
    animal_id = forms.IntegerField(label="Номер животного", widget=forms.NumberInput(attrs={"class": "myfield"}))



