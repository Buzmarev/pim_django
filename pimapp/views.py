from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Product
    
class Base():
    def get_base_context(self):
        data = {
            'navbar': [
                ('/', 'Home'),
                ('/product', 'Products')
            ]
        }
    
        return data

class IndexView(TemplateView, Base):
    template_name = "pimapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_base_context()
        meta_context = {
            'meta_title': 'PIM - Product information management system'
        }
        return {**context, **base_context, **meta_context}

class ProductListView(ListView, Base):
    model = Product
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_base_context()
        meta_context = {
            'meta_title': 'PIM - Products list'
        }
        return {**context, **base_context, **meta_context}