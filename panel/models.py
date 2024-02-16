from django.db import models


class Header(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название банера шапки')
    image = models.ImageField(upload_to='media/header', verbose_name='Изображение')
    standart = models.BooleanField(default=False, verbose_name='Стандартный')
    summer = models.BooleanField(default=False, verbose_name='Летний')
    winter = models.BooleanField(default=False, verbose_name='Зимний')

    class Meta:
        verbose_name = 'Шапка'
        verbose_name_plural = 'Шапка на главной'

    def __str__(self):
        return self.name


class BackGround(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название фона')
    image = models.ImageField(upload_to='media/header', blank=True, verbose_name='Изображение')
    standart = models.BooleanField(default=False, verbose_name='Стандартный')
    summer = models.BooleanField(default=False, verbose_name='Летний')
    winter = models.BooleanField(default=False, verbose_name='Зимний')

    class Meta:
        verbose_name = 'Фон'
        verbose_name_plural = 'Фоны панели'

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название кружка')
    image = models.ImageField(upload_to='media/section', verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Кружок'
        verbose_name_plural = 'Кружки'

    def __str__(self):
        return self.name


class QrCode(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название кода')
    image = models.ImageField(upload_to='media/qr', verbose_name='QR-code')

    class Meta:
        verbose_name = 'QR код'
        verbose_name_plural = 'QR коды'

    def __str__(self):
        return self.name


class PushkinKarta(models.Model):
    name = models.CharField(max_length=150, verbose_name='Заголовок')
    image = models.ImageField(upload_to='media/section', verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Пушкинская карта'
        verbose_name_plural = 'Пушкинская карта'

    def __str__(self):
        return self.name


class Karta(models.Model):
    name = models.CharField(max_length=150, verbose_name='Заголовок')
    image = models.ImageField(upload_to='media/section', verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карта ИКЦ'

    def __str__(self):
        return self.name
