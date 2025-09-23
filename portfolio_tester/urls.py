from django.urls import path
from . import views

app_name = 'portfolio_tester'

urlpatterns = [
    path('form/', views.portfolio_creator, name='portfolio_creator'),
    path('formtest/', views.tester, name='tester'),
    path('my_portfolios/', views.my_portfolios, name='my_portfolios'),
]
