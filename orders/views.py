from django.shortcuts import render
from .models import OrderItem, Messenger
from .forms import OrderCreateForm
from cart.cart import Cart
import requests


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            name1 = request.POST.get('first_name')
            name2 = request.POST.get('last_name')
            phone = request.POST.get('phone')
            messenger_id = request.POST.get('contact')
            messenger = Messenger.objects.get(id=messenger_id)
            messenger_value = messenger.name
            mail = request.POST.get('email')
            token = 'Токен Бота'
            chatId = 'свой chatId'
            #
            message = f'''
            У вас новая заявка!
            Имя - {name1}
            Фамилия - {name2}
            Телефон - {phone}
            Мессенджер - {messenger_value}
            Почта - {mail}
            '''
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&text={message}"
            requests.get(url)

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request, 'created.html', {
                'order': order
            })
    else:
        form = OrderCreateForm()

    return render(request, 'create.html', {
        'cart': cart,
        'form': form
    })
