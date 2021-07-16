from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import favorite_sports, AccountCreateView, AccountDetailView

app_name = 'accountapp'





urlpatterns = [
    path('favorite_sports/', favorite_sports, name='favorite_sports'),

    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name ='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name ='detail'),

]




