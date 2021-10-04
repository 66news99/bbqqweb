from django.urls import path

from replaceapp.views import BasicTemplateView, let_write

app_name = 'replaceapp'

urlpatterns = [
    path('challenge/', BasicTemplateView.as_view(), name='challenge'),
    path('let_write/', let_write, name='let_write'),
]