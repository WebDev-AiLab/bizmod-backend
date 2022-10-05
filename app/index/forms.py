from django import forms

IncomeField = (('Basic', 'Основной'),
               ('Additional', 'Дополнительный'))

ChoiceField = (('ONE', '1'), ('TWO', '2'), ('TREE', '3'),
               ('FOUR', '4'), ('FIVE', '5'), ('SIX', '6'),
               ('SEVEN', '7'), ('EIGHT', '8'), ('NINE', '9'),
               ('TEN', '10'),)

ProfitPerMonthField = (('FIRST', "50-100 тысяч в месяц"), ('SECOND', '100-200 тысяч в месяц'),
                       ('THIRD', '200-300 тысяч в месяц'), ('FOURTH', '300-500 тысяч в месяц '),
                       ('FIFTH', 'Более 500 тысяч в месяц'),)

GainProfitField = (('FIRST', 'За 3 месяца'), ('SECOND', 'За 4-6 месяцев'), ('THIRD', 'За 7-12 месяцев'),)

CurentProifitField = (('FIRST', 'до 30 тыс. рублей'), ('SECOND', '30-60 тыс. рублей'), ('THIRD', '60-100 тыс. рублей'),
                      ('FOURTH', '100-150 тыс. рублей'), ('FIFTH', '150-300 тыс. рублей'),
                      ('SIXTH', 'больше 300 тыс. рублей'))

CityCizeFiled = (
    ('FIRST', 'до 50 тысяч человек'), ('SECOND', '50-150 тысяч человек'), ('THIRD', '150-300 тысяч человек'),
    ('FOURTH', '300-600 тысяч человек'), ('FIFTH', '600-миллион человек'), ('SIXTH', 'Свыше миллиона человек'),)

WhenToBeginField = (('FIRST', 'В ближайщее время'), ('SECOND', 'В течении 2-3 недель'),
                    ('THIRD', 'Через месяц'), ('FOURTH', 'Позже'),)

DemandField = (('YES', 'ДА'), ('NO', 'НЕТ'),)

ChangeBusinesField = (('YES', 'ДА'), ('NO', 'НЕТ'),)

ExperienceField = (('YES', 'ДА'), ('NO', 'НЕТ'),)

MariageStatusField = (('FIRST', 'В браке'), ('SECOND', 'Не в браке'))


class UserForm(forms.Form):
    full_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'full_name', 'placeholder': "Full Name"}))
    email = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'email', 'name': 'email', 'placeholder': "Email"}))
    notes = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'notes', 'placeholder': "Notes"}))
    work = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'work', 'placeholder': "Work"}))
    interest = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'interest', 'placeholder': "Interest"}))
    age = forms.CharField(label='', widget=forms.NumberInput(
        attrs={'class': 'input', 'type': 'number', 'name': 'age', 'placeholder': "Age"}))
    income = forms.TypedChoiceField(label='', choices=IncomeField)
    satisfaction = forms.TypedChoiceField(label='', choices=ChoiceField)
    importance = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'importance', 'placeholder': "Importance"}))
    experience = forms.TypedChoiceField(label='', choices=ExperienceField)
    need = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'need', 'placeholder': "Need"}))
    profit_per_month = forms.TypedChoiceField(label='', choices=ProfitPerMonthField)
    when_to_gain_profit = forms.TypedChoiceField(label='', choices=GainProfitField)
    curent_profit = forms.TypedChoiceField(label='', choices=CurentProifitField)
    city_size = forms.TypedChoiceField(label='', choices=CityCizeFiled)
    when_to_begin = forms.TypedChoiceField(label='', choices=WhenToBeginField)
    demand = forms.TypedChoiceField(label='', choices=DemandField)
    city_for_work = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'city_for_work ', 'placeholder': 'City_For_Work'}))
    mariage_status = forms.TypedChoiceField(label='', choices=MariageStatusField)
    advantages = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'name': 'advantages', 'placeholder': "Advantages"}))
    change_busines = forms.TypedChoiceField(label='', choices=ChangeBusinesField)
