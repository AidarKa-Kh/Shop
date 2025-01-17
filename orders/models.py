from django.db import models
from shop.models import Product
from phonenumber_field.modelfields import PhoneNumberField


class Messenger(models.Model):
    name = models.CharField('Мессенджер', max_length=20)

    verbose_name = 'Мессенджер'
    verbose_name_plural = 'Мессенджеры'

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    phone = PhoneNumberField('Телефон', unique=True, null=False, blank=False)
    contact = models.ForeignKey(Messenger, verbose_name='Мессенджер для связи', on_delete=models.CASCADE)
    email = models.EmailField('Почта', )
    address = models.CharField('Адрес', max_length=250)
    postal_code = models.CharField('Индекс', max_length=20)
    city = models.CharField('Город', max_length=100)
    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)
    paid = models.BooleanField('Оплата', default=False)

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created']), ]

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
