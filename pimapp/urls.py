from django.urls import path
from .views import IndexView, ProductListView

urlpatterns = [
    path('', IndexView.as_view(), name = 'home'),
    path('product', ProductListView.as_view(), name = 'product_list'),
]