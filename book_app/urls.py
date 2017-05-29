from django.conf.urls import url

from .views import add_book

urlpatterns = [
    url('/', add_book)
]
