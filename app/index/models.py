from django.db import models

Income = (('Basic', 'Основной'), ('Additional', 'Дополнительный'))

Choice = (('ONE', '1'), ('TWO', '2'), ('THREE', '3'),
          ('FOUR', '4'), ('FIVE', '5'), ('SIX', '6'),
          ('SEVEN', '7'), ('EIGHT', '8'), ('NINE', '9'),
          ('TEN', '10'),)

Experience = (('YES', 'Да'), ('NO', 'Нет'),)

Profit = (('FIRST', "50-100 тысяч в месяц"), ('SECOND', '100-200 тысяч в месяц'),
          ('THIRD', '200-300 тысяч в месяц'), ('FOURTH', '300-500 тысяч в месяц'),
          ('FIFTH', 'Более 500 тысяч в месяц'),)

Registration = (('FIRST', 'Физ лицо'), ('SECOND', 'Самозанятый'),
                ('THIRD', 'Я ИП'), ('FOURTH', 'ООО'),)

Clients = (('FIRST', 'Пока нет'), ('SECOND', 'Есть знакомые'),
           ('THIRD', 'Есть несколько клиентов'), ('FOURTH', 'Есть крупные клиенты'),)

GainProfit = (('FIRST', 'За 3 месяца'), ('SECOND', 'За 4-6 месяцев'), ('THIRD', 'За 7-12 месяцев'))

CitySize = (
    ('FIRST', 'до 50 тысяч человек'), ('SECOND', '50-150 тысяч человек'), ('THIRD', '150-300 тысяч человек'),
    ('FOURTH', '300-600 тысяч человек'), ('FIFTH', '600-миллион человек'), ('SIXTH', 'Свыше миллиона человек'),)

CurentProfit = (('FIRST', 'до 30 тыс. рублей'), ('SECOND', '30-60 тыс. рублей'), ('THIRD', '60-100 тыс. рублей'),
                ('FOURTH', '100-150 тыс. рублей'), ('FIFTH', '150-300 тыс. рублей'),
                ('SIXTH', 'больше 300 тыс. рублей'))

WhenToBegin = (('FIRST', 'В ближайщее время'), ('SECOND', 'В течении 2-3 недель'),
               ('THIRD', 'Через месяц'), ('FOURTH', 'Позже'),)

Demand = (('YES', 'Да'), ('NO', 'Нет'),)

MariageStatus = (('FIRST', 'В браке'), ('SECOND', 'Не в браке'))

Status = (('FIRST', 'Работаю'), ('SECOND', 'Не работаю сейчас'),
          ('THIRD', 'Веду бизнес'), ('FOURTH', 'Проблемы в бизнесе'),)


class User(models.Model):
    full_name = models.CharField(max_length=200, blank=True)
    age = models.IntegerField(blank=True)
    email = models.EmailField(blank=True, unique=True)
    city = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    city_for_work = models.CharField(max_length=200, blank=True)
    city_size = models.CharField(max_length=40, choices=CitySize, blank=True)
    mariage_status = models.CharField(max_length=40, choices=MariageStatus, blank=True)
    status = models.CharField(max_length=40, choices=Status, blank=True)
    work = models.CharField(max_length=200, blank=True)
    registration = models.CharField(max_length=40, choices=Registration, blank=True)
    experience = models.CharField(max_length=20,
                                  choices=Experience,
                                  blank=True,
                                  )
    sector = models.TextField(blank=True)
    why = models.TextField(blank=True)
    income = models.CharField(max_length=40, choices=CurentProfit, blank=True)
    satisfaction = models.CharField(
        max_length=20,
        choices=Choice,
        blank=True,
    )
    profit_per_month = models.CharField(max_length=40, choices=Profit, blank=True)
    why_business1 = models.TextField(blank=True)
    why_business2 = models.TextField(blank=True)
    interest = models.TextField(blank=True)
    main_or_no = models.CharField(
        max_length=20,
        choices=Income,
        blank=True,
    )
    what_need = models.TextField(blank=True)
    what_sector = models.TextField(blank=True)
    other_sector = models.TextField(blank=True)
    when_to_begin = models.CharField(max_length=40, choices=WhenToBegin, blank=True)
    clients = models.CharField(max_length=40, choices=Clients, blank=True)
    description = models.TextField(blank=True)
    advantages = models.CharField(max_length=200, blank=True)
    test_deman = models.CharField(max_length=40, choices=Demand, blank=True)
    need = models.TextField(blank=True)
    when_to_gain_profit = models.CharField(max_length=40, choices=GainProfit, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'
        ordering = ('created',)


class City(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    population = models.IntegerField(verbose_name='Население')
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('created',)

    def __str__(self):
        return self.name
