from django.urls import path

from replaceapp.views import BasicTemplateView

app_name = 'replaceapp'

urlpatterns = [
    path('challenge/', BasicTemplateView.as_view(), name='challenge'),
]