from django.contrib import admin

# Register your models here.
from .forms import UserForm
from .models import User, City


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
 list_display = ( 'full_name', 'email')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
 list_display = ( 'name', 'population')