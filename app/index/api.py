import requests as req
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from validate_email import validate_email

from index.models import User, City
from index.serializer import UserSerializer, CitySerializers


# #
# test_request = {"age":"33","mariage_status":"В браке","city_for_work":"Казань","city_size":"Свыше миллиона человек",
# "status":"Работаю","registration":"Физ лицо","work":"Кем то","income":"100-150 тыс. рублей",
# "satisfaction":"4","experience":"Да","sector":"Любой","why":"Просто",
# "profit_per_month":"300-500 тысяч в месяц","when_to_gain_profit":"За 3 месяца","why_business1":"Потому что",
# "why_business2":"Потому что","interest":"Всем","main_or_no":"Основной","what_need":"Все","when_to_begin":
# "В ближайщее время","clients":"Пока нет","other_sector":"Да","what_sector":"В любой","need":"Все","description":"Кратко",
# "advantages":"Все","test_deman":"Да интересно","full_name":"тест не трогайте","phone":"+79999990040","email":"40@mail.ru","city":"Казань"}


class UserCreateAPI(APIView):

    def _check_user_in_database(self, email):
        if User.objects.filter(email=email).exists():
            return True
        return False

    def _valid_email(self, email):
        return validate_email(email)

    def post(self, request):
        try:
            form = request.data
            email = form.get("email")
            if not self._valid_email(email):
                return Response({'detail': 'invalid email'}, status.HTTP_400_BAD_REQUEST)
            if self._check_user_in_database(email):
                return Response({'detail': 'There is already an entry in the database at this address'},
                                status.HTTP_400_BAD_REQUEST)
            User.objects.create(**form)
            user_model = get_object_or_404(User, email=email)
            return Response(UserSerializer(user_model).data, status.HTTP_201_CREATED)

        except (TypeError, ValueError, IntegrityError):
            return Response({'detail': 'invalid request data'}, status.HTTP_400_BAD_REQUEST)


class UserGetObjectAPI(APIView):

    def get(self, request, **kwargs):
        user_model = get_object_or_404(User, email=kwargs.get("email"))
        return Response(UserSerializer(user_model).data, status.HTTP_200_OK)


class UserYandexAPi(APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, **kwargs):
        user_model = get_object_or_404(User, email=kwargs.get("email"))
        urls = [
            f'https://search-maps.yandex.ru/v1/?text={"кафе", user_model.city}&type=biz&lang=ru_RU&results=2&apikey=848f34c8-65cc-4f42-a044-67663e66d519',
            f'https://search-maps.yandex.ru/v1/?text={"ресторан", user_model.city}&type=biz&lang=ru_RU&results=1&apikey=848f34c8-65cc-4f42-a044-67663e66d519',
            f'https://search-maps.yandex.ru/v1/?text={"торговый центр", user_model.city}&type=biz&lang=ru_RU&results=1&apikey=848f34c8-65cc-4f42-a044-67663e66d519',
            f'https://search-maps.yandex.ru/v1/?text={"магазин одежды", user_model.city}&type=biz&lang=ru_RU&results=1&apikey=848f34c8-65cc-4f42-a044-67663e66d519']
        rest = [req.get(i).json() for i in urls]
        context = {'user': UserSerializer(user_model).data, 'yandex_rest': rest}

        return Response(context, status.HTTP_200_OK)

class GetCity(APIView):


    def get(self, request, **kwargs):
        city = get_object_or_404(City, name=kwargs.get("name").title())
        return Response(CitySerializers(city).data, status.HTTP_200_OK)

