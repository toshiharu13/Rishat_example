from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>/', views.product_view, name='product_view'),
    path('buy/<int:item_id>/', views.get_pay, name='get_pay'),
]
