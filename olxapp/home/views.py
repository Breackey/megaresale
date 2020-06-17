from django.shortcuts import render
from product.models import Product , ProductImages , Category
from django.db.models import Count
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):

    all_category = Category.objects.all()
    products = Product.objects.all()

    template = 'home.html'
    context = { 'all_category' : all_category , 'products' : products}

    return render(request , template , context)

def categories(request , category_slug=None):
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))
    category = Category.objects.all()  
    
    if category_slug :
        category = get_object_or_404(Category ,slug=category_slug)
        productlist = productlist.filter(category=category)
    

    template = 'categories.html'
    context = { 'product_list' : productlist , 'category_list' : categorylist ,'category' : category}

    return render(request , template , context)

def postad(request):
 
    
    template = 'post_ad.html'

    return render(request , template)