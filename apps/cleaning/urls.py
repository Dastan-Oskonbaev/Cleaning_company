from django.urls import path

from .views import IndexView, RobotsTxtView, SitemapXmlView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('robots.txt', RobotsTxtView.as_view()),
    path('sidemap.xml', SitemapXmlView.as_view())
]
