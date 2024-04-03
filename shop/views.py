from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Category, Message
from cart.forms import CartAddProductForm
from shop.forms import UsersMessageForm


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()

    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'index.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form
    })


def contacts(request):
    return render(request, 'contacts.html')


# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     cart_product_form = CartAddProductForm()
#
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'index.html', {
#         'category': category,
#         'categories': categories,
#         'products': products,
#         'cart_product_form': cart_product_form
#     })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    return render(request, 'product.html', {
        'product': product,
        'cart_product_form': cart_product_form
    })


def contact(request):
    if request.method == 'POST':
        form = UsersMessageForm(request.POST)

        if form.is_valid():
            messages = form.save(commit=False)
            messages.save()

            return redirect('shop:index')
    else:
        form = UsersMessageForm()

    return render(request, 'contacts.html', {
        'form': form
    })


@login_required
def message(request):
    messages = Message.objects.all()

    return render(request, 'message.html', {
        'messages': messages,
    })

