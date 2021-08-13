from django.urls import path

from projectapp.views import ProjectCreateView

app_name = 'projectapp'

urlpatterns = [
    path('creat/', ProjectCreateView.as_view(), name='create')
]