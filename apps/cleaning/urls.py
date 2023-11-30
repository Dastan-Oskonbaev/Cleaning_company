from django.urls import path

from .views import IndexView, RobotsTxtView, SitemapXmlView, GalleryView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('gallery/', GalleryView.as_view(), name='list_gallery'),
    path('robots.txt', RobotsTxtView.as_view()),
    path('sidemap.xml', SitemapXmlView.as_view())
]
