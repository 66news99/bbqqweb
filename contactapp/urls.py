from django.urls import path

from contactapp.views import BasicTemplateView

app_name = 'contactapp'

urlpatterns = [
    path('introduce/', BasicTemplateView.as_view(), name='introduce'),
]