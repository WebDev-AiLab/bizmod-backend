from django.db import models


# Create your models here.
Choice = (('full_name', 'full_name'), ('age', 'age'), ('email', 'email'),
          ('city', 'city'), ('phone', 'phone'), ('city_for_work', 'city_for_work'),
          ('city_size', 'city_size'), ('mariage_status', 'mariage_status'), ('status', 'status'),
          ('work', 'work'), ('registration', 'registration'), ('experience', 'experience'), ('sector', 'sector'),
          ('why', 'why'), ('income', 'income'), ('satisfaction', 'satisfaction'), ('profit_per_month', 'profit_per_month'),
          ('why_business1', 'why_business1'), ('why_business2', 'why_business2'), ('interest', 'interest'), ('main_or_no', 'main_or_no'),
          ('main_or_no', 'main_or_no'), ('what_need', 'what_need'), ('other_sector', 'other_sector'), ('when_to_begin', 'when_to_begin'),
          ('clients', 'clients'), ('description', 'description'), ('advantages', 'advantages'), ('test_deman', 'test_deman'),
          ('need', 'need'), ('when_to_gain_profit', 'when_to_gain_profit'))

class TypePage(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название типа')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тип слайда'
        verbose_name_plural = 'Типы слайдов'
        ordering = ('created',)

    def __str__(self):
        return self.name


class Order(models.Model):
    nomber = models.IntegerField(unique=True, verbose_name='Номер')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Страница {self.nomber}'

    class Meta:
        verbose_name = 'Номер слайда'
        verbose_name_plural = 'Номера слайдов'
        ordering = ('created',)




class Page(models.Model):
    type_page = models.ForeignKey(TypePage,
                                  related_name='types',
                                  on_delete=models.CASCADE, verbose_name='Тип слайда')
    order = models.ForeignKey(Order, related_name='orders', null=True, on_delete=models.SET_NULL, verbose_name='Номер слайда')
    title = models.CharField(max_length=300, blank=True, verbose_name='Название')
    sub_title = models.CharField(max_length=300, blank=True, verbose_name='Дополнительное название')
    video_url = models.URLField(blank=True, verbose_name='Ссылка на видео')
    image = models.ImageField(upload_to='pages', blank=True, verbose_name='Картинка')
    description = models.TextField(blank=True, verbose_name='Текст')
    sub_description = models.TextField(blank=True, verbose_name='Дополнительный текст')
    button_text = models.CharField(max_length=300, blank=True, verbose_name='Кнопка')
    pre_button_text = models.CharField(max_length=300, blank=True, verbose_name='Дополнительная кнопка')
    button_link = models.URLField(blank=True, verbose_name='Ссылка кнопки')
    created = models.DateTimeField(auto_now_add=True)
    fild = models.CharField(blank=True, choices=Choice, max_length=500, verbose_name='Поле')
    fild_value = models.CharField(max_length=255, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Слайд {self.order}'

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ('created',)



class Urls(models.Model):
    name = models.CharField(max_length=255)
    page = models.ForeignKey(Page, related_name='urls', null=True, on_delete=models.SET_NULL, verbose_name='Cлайд')
    order = models.ForeignKey(Order, related_name='urls', null=True, on_delete=models.SET_NULL, verbose_name='Номер слайда')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Ссылка {self.id}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ('created',)


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', verbose_name='Картинки')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='images', verbose_name='Cлайд')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Картинка {self.id}'

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
        ordering = ('created',)



