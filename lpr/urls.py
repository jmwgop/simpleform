from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/', views.create_lpr, name='create_lpr'),
]
