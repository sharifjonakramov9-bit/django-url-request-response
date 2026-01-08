from django.urls import path

from .views import login_view, orders_view, calculators_view


urlpatterns = [
    path('login/<int:pk>', login_view, name='login'),
    path('orders/', orders_view, name='order'),
    path('calculators/', calculators_view, name='calculators'),
]
