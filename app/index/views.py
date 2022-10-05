from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from index.models import User
from index.serializer import UserSerializer


class Index(TemplateView):
    """ Главная страница сайта: Тут должна быть генерация блоков
     по сценарию который дал заказчик данные берутся из webhook-ов
     напрямую из сайта заказчика """
    template_name = 'view.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, email=kwargs.get('email'))
        context['user'] = UserSerializer(user).data
        return context