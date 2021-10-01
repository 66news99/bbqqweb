from django.urls import path

from mainapp.views import BasicTemplateView

app_name = 'mainapp'

urlpatterns = [
    path('mainpage/', BasicTemplateView.as_view(), name='mainpage'),
]

