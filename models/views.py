from django.shortcuts import render, get_object_or_404, redirect
from .bot import get_post, get_post1
from .models import ServiceModel, ProductModel, AdviceModel, PartnerModel
from .forms import AdviceForm, ProductForm
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def home(req):
    service = ServiceModel.objects.filter(important=True)
    products = ServiceModel.objects.all()[:3]
    product_footer = ServiceModel.objects.all()[:6]
    partners = PartnerModel.objects.filter(important=True)[:4]
    form = AdviceForm(req.POST or None)
    context = {
        'form': form,
        'service': service,
        "products": products,
        'partners': partners,
        'product_footer': product_footer,
    }
    # if req.method == 'POST' and form.is_valid():
    #     form.save()
    return render(req, 'index.html', context)

def about_us(request):
    products = ServiceModel.objects.all()[:3]
    partners = PartnerModel.objects.all()
    product_footer = ServiceModel.objects.all()[:6]

    context = {
        "products": products,
        'partners': partners,
        "product_footer": product_footer,
    }
    return render(request, 'pages/about.html', context)

def products(request):
    products = ServiceModel.objects.all()[:3]
    partners = PartnerModel.objects.all()
    product_footer = ServiceModel.objects.all()[:6]

    context = {
        "products": products,
        'partners': partners,
        'product_footer': product_footer
    }
    return render(request, 'pages/courses.html', context)

def contact_page(request):
    form = AdviceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print("GOOD")
        form.save()
        get_post(form.data)
        form = AdviceForm()
        return redirect('success_page')
    else:
        form = AdviceForm()
        print("NOT GOOD")
    product_footer = ServiceModel.objects.all()[:6]

    context = {
        'product_footer': product_footer,
        'form': form,
    }

    return render(request, 'pages/contact.html', context)

def form_page(request):
    product_footer = ServiceModel.objects.all()[:6]
    products = ServiceModel.objects.all()
    form = ProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print("GOOD")
        form.save()
        get_post1(form.data)
        form = ProductForm()
        return redirect('success_page')
    else:
        form = ProductForm()
        print("NOT GOOD")
    context = {
        'products': products,
        "product_footer": product_footer,
        'form': form,
    }
    return render(request, 'pages/form.html', context)

def success_page(request):
    product_footer = ServiceModel.objects.all()[:6]
    context = {
        "product_footer": product_footer
    }
    return render(request, 'pages/success.html', context)



def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text

def custom_404_view(request, exception):
    product_footer = ServiceModel.objects.all()[:6]
    context = {
        "product_footer": product_footer
    }
    return render(request, 'pages/404.html',context, status=404)