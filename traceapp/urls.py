from django.urls import path

from traceapp.views import BasicTemplateView

app_name = 'traceapp'

urlpatterns = [
    path('group/', BasicTemplateView.as_view(), name='group'),
]