from django.urls import path
from . import views

app_name = 'portfolio_tester'

urlpatterns = [
    path('', views.portfolio_tester_home, name='portfolio_tester_home'),
]
