from datetime import date

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .models import Contact, AboutUs, OurServices, ServicesCategory, Reviews, Phone, Gallery, Application, Telegram
from .forms import ApplicationForm
from .sender import send_application_to_telegram


class IndexView(View):
    def get(self, request):
        contact = Contact.objects.all()
        phone = Phone.objects.all()
        about = AboutUs.objects.all().first()
        services = OurServices.objects.all()
        category = ServicesCategory.objects.all()
        reviews = Reviews.objects.all()
        gallery = Gallery.objects.order_by()[:4]
        statistic = AboutUs.objects.all().first()

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
            'gallery': gallery,
            'statistic': statistic,
        }

        if about:
            description = about.description.split("/")
            context['description'] = description

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


class GalleryView(View):
    def get(self, request):
        contact = Contact.objects.all()
        phone = Phone.objects.all()
        gallery = Gallery.objects.all()
        context = {
            'contact': contact,
            'phone': phone,
            'gallery': gallery,
        }
        return render(request, 'cleaning/list_gallery.html', context)


class RobotsTxtView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'


class SitemapXmlView(TemplateView):
    template_name = 'sitemapxml.html'
    content_type = 'text/xml'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Contact'] = Contact.objects.all()
        context['Phone'] = Phone.objects.all()
        context['AboutUs'] = AboutUs.objects.all()
        context['Reviews'] = Reviews.objects.all()
        context['ServicesCategory'] = ServicesCategory.objects.all()
        context['OurServices'] = OurServices.objects.all()
        context['Application'] = Application.objects.all()
        context['Telegram'] = Telegram.objects.all()
        context['Gallery'] = Gallery.objects.all()
        return context
