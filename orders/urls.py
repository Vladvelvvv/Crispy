from django.urls import path

from orders import views

app_name = "orders"

urlpatterns = [
    path('create-order/', views.OrderView.as_view(), name="order"),
]