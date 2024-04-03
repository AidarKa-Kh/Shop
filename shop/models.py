from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


#  Модель категорий товара
class Category(models.Model):
    name = models.CharField('Категория', max_length=255)
    slug = models.SlugField('URL', max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


#  Модель добавления товара
class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='products', on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=255)
    slug = models.SlugField('URL', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Изображение', upload_to='item_images/%Y/%m/%d', blank=True, null=True)
    available = models.BooleanField('Активно', default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


#  Модель свяжитесь с нами на странице контакты
class Message(models.Model):
    name = models.TextField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return self.name
