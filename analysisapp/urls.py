from django.urls import path

from analysisapp.views import BasicTemplateView

app_name = 'analysisapp'

urlpatterns = [
    path('explain/', BasicTemplateView.as_view(), name='explain'),
]