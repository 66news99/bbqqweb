from django.urls import path

from accountapp.views import favorite_sports, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('favorite_sports/', favorite_sports, name='favorite_sports'),

    path('create/',AccountCreateView.as_view(), name ='create'),
]