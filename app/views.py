from django.shortcuts import render
from app.models import *

# Create your views here.
def shopping(request):
    if request.method=='POST':
        pn=request.POST['pn']

        SO=shop.objects.get_or_create(product_name=pn)[0]
        SO.save()

        QLSO=shop.objects.all()
        d={'shop':QLSO}

        return render(request,'display_shopping.html',d)
    return render(request,'shopping.html')


def product(request):
    QLSO=shop.objects.all()
    d={'shop':QLSO}

    
    if request.method=='POST':
        pn=request.POST['pn']
        qu=request.POST['qu']
        am=request.POST['am']
        mf=request.POST['mf']
        SO=shop.objects.get(product_name=pn)
        PO=products.objects.get_or_create(product_name=SO,quantity=qu,amount=am,mfg=mf)[0]
        PO.save()
        QLPO=products.objects.all()
        d1={'products':QLPO}
        return render(request,'display_product.html',d1)
    return render(request,'product.html',d)