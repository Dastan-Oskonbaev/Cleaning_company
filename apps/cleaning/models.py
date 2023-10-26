from django.db import models

from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    email = models.EmailField(
        _('Email'),
        max_length=50,
        null=True,
        blank=True,
    )
    instagram = models.URLField(
        _('Instagram'),
        max_length=100,
        null=True,
        blank=True,
    )
    tiktok = models.URLField(
        _('TikTok'),
        max_length=255,
        null=True,
        blank=True,
    )
    whatsapp = models.URLField(
        _('WhatsApp'),
        max_length=100,
        null=True,
        blank=True,
    )
    telegram = models.URLField(
        _('Telegram'),
        max_length=100,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        _('Номер тел.'),
        max_length=20,
        null=True,
        blank=True,
    )
    address = models.URLField(
        _('Адрес'),
        max_length=100,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')

    def __str__(self):
        return self.email


class AboutUs(models.Model):
    title = models.CharField(
        _('Заголовок'),
        max_length=255,
    )
    description = models.TextField(
        _('Описание'),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('О нас')
        verbose_name_plural = _('О нас')


class Reviews(models.Model):
    title = models.CharField(
        _('Заголовок'),
        max_length=255,
    )
    file = models.FileField(
        _('Файл'),
        upload_to='reviews/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Отзывы')
        verbose_name_plural = _('Отзывы')


class ServicesCategory(models.Model):
    title = models.CharField(
        _('Заголовок'),
        max_length=255,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория услуг')
        verbose_name_plural = _('Категории услуг')


class OurServices(models.Model):
    category = models.ForeignKey(
        ServicesCategory,
        on_delete=models.CASCADE,
        verbose_name=_('Категория услуг'),
        related_name='services',
    )
    title = models.CharField(
        _('Заголовок'),
        max_length=255,
    )
    description = models.TextField(
        _('Описание'),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Наши услуги')
        verbose_name_plural = _('Наши услуги')

