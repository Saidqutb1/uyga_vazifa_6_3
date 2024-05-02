from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'templates/index.html', context=context)