from datetime import date

from django.shortcuts import render, redirect
from django.views import View

from .models import Contact, AboutUs, OurServices, ServicesCategory, Reviews, Phone
from .forms import ApplicationForm
from .sender import send_application_to_telegram


class IndexView(View):
    def get(self, request):
        contact = Contact.objects.all()
        phone = Phone.objects.all()
        about = AboutUs.objects.all().first()
        services = OurServices.objects.all()
        category = ServicesCategory.objects.all()
        reviews = Reviews.objects.all().first()

        form = ApplicationForm()

        context = {
            'title': 'Главная страница',
            'contact': contact,
            'about': about,
            'reviews': reviews,
            'category': category,
            'services': services,
            'phone': phone,
            'form': form,
        }

        if about:
            description = about.description.split("/")
            context['description'] = description

        # if services:
        #     service = services.description.split("/")
        #     service = services.all().order_by('description')
        #     context['service'] = service

        return render(request, 'cleaning/index.html', context)

    def post(self, request):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']

            message = f'''Новая форма была заполнена:
Имя: {first_name}
Фамилия: {last_name}
Номер тел.: {phone_number}
Дата: {date.today()}'''
            send_application_to_telegram(message)

            return redirect('index')

        return render(request, 'cleaning/index.html', {'form': form})
