from django.urls import path

from analysisapp.views import BasicTemplateView, let_write

app_name = 'analysisapp'

urlpatterns = [
    path('explain/', BasicTemplateView.as_view(), name='explain'),
    path('let_write/', let_write, name='let_write')
]