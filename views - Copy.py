from django.shortcuts import render, get_object_or_404
from .models import product, techType, Review 

def index(request):
    return render(request, 'club\index.html')

    def products(request):
        product_list=product.objects.all()
        return render(request, 'club/product.html', {'product_list': product_list})
def productDetail(request, id):
     product=get_object_or_404(product, pk=id)
     return render(request, 'club/productdetail.html', {'product' : product})