from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>/', views.product_view, name='product_view')
]
