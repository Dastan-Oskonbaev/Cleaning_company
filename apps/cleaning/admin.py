from django.contrib import admin

from .models import Contact, ServicesCategory, OurServices, AboutUs, Reviews, Application, Telegram, Phone


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'email',
        'instagram',
        'tiktok',
        'telegram',
        'whatsapp',
        'address',
    )
    list_display_links = (
        'email',
    )
    list_filter = (
        'email',
    )
    search_fields = (
        'email',
    )


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'phone_number',
    )
    list_display_links = (
        'phone_number',
    )
    search_fields = (
        'id',
        'phone_number',
    )
    list_filter = (
        'id',
        'phone_number',
    )


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'title',
        'description',
    )
    list_display_links = (
        'title',
    )
    list_filter = (
        'title',
    )
    search_fields = (
        'title',
    )
    ordering = (
        'title',
    )


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'title',
    )
    list_display_links = (
        'title',
    )
    list_filter = (
        'title',
    )
    search_fields = (
        'title',
    )
    ordering = (
        'title',
    )


@admin.register(ServicesCategory)
class ServicesCategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'title',
    )
    list_display_links = (
        'title',
    )
    list_filter = (
        'title',
    )
    search_fields = (
        'title',
    )
    ordering = (
        'title',
    )


@admin.register(OurServices)
class OurServicesAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'title',
        'description',
    )
    list_display_links = (
        'title',
    )
    list_filter = (
        'title',
    )
    search_fields = (
        'title',
    )
    ordering = (
        'title',
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone_number',
    )
    list_display_links = (
        'first_name',
    )
    search_fields = (
        'id',
        'first_name',
        'last_name',
        'phone_number',
    )
    list_filter = (
        'id',
        'first_name',
        'last_name',
        'phone_number',
    )


@admin.register(Telegram)
class TelegramAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'chat_id',
    )
    list_display_links = (
        'username',
    )
    search_fields = (
        'id',
        'username',
        'chat_id',
    )
    list_filter = (
        'id',
        'username',
        'chat_id',
    )
