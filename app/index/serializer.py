from rest_framework import serializers
from rest_framework.fields import ChoiceField

from index.models import User, City


class DisplayNameWritableField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        self.html_cutoff = kwargs.pop('html_cutoff', self.html_cutoff)
        self.html_cutoff_text = kwargs.pop('html_cutoff_text', self.html_cutoff_text)

        self.allow_blank = kwargs.pop('allow_blank', False)
        super(ChoiceField, self).__init__(**kwargs)

    def to_representation(self, value):
        return self.choices.get(value, value)

    def bind(self, field_name, parent):
        super().bind(field_name, parent)
        self.choices = parent.Meta.model._meta.get_field(field_name).choices


class UserSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    city = serializers.CharField()
    phone = serializers.CharField()
    city_for_work = serializers.CharField()
    city_size = DisplayNameWritableField()
    mariage_status = DisplayNameWritableField()
    status = DisplayNameWritableField()
    work = serializers.CharField()
    registration = DisplayNameWritableField()
    experience = DisplayNameWritableField()
    sector = serializers.CharField()
    why = serializers.CharField()
    income = DisplayNameWritableField()
    satisfaction = DisplayNameWritableField()
    profit_per_month = DisplayNameWritableField()
    why_business1 = serializers.CharField()
    why_business2 = serializers.CharField()
    interest = serializers.CharField()
    main_or_no = DisplayNameWritableField()
    what_need = serializers.CharField()
    what_sector = serializers.CharField()
    other_sector = serializers.CharField()
    when_to_begin = DisplayNameWritableField()
    clients = DisplayNameWritableField()
    description = serializers.CharField()
    advantages = serializers.CharField()
    test_deman = DisplayNameWritableField()
    need = serializers.CharField()
    when_to_gain_profit = DisplayNameWritableField()

    class Meta:
        model = User


class CitySerializers(serializers.ModelSerializer):


    class Meta:
        model = City
        fields = '__all__'