from django.shortcuts import render
from django.views import View

from .models import Contact, AboutUs, OurServices, ServicesCategory, Reviews


class IndexView(View):
    def get(self, request):
        contact = Contact.objects.all()
        about = AboutUs.objects.all()
        services = OurServices.objects.all()
        category = ServicesCategory.objects.all()
        reviews = Reviews.objects.all().first()

        context = {
            'title': 'Главная страница',
            'contact': contact,
            'about': about,
            'reviews': reviews,
            'category': category,
            'services': services,
        }

        if about:
            description = about.description.split("/")
            context['description'] = description

        if services:
            service = services.description.split("/")
            context['service'] = service

        return render(request, 'cleaning/index.html', context)

