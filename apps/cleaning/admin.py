from django.contrib import admin

from .models import Contact, ServicesCategory, OurServices, AboutUs, Reviews


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'email',
        'instagram',
        'tiktok',
        'telegram',
        'whatsapp',
        'phone_number',
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


