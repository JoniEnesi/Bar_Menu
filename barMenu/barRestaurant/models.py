from django.db import models

# Create your models here.

class Category(models.Model):
    images = models.ImageField(upload_to='', null=True, blank=True)
    category_name_al = models.CharField(max_length=50, null=True, blank=True)
    category_name_en = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.category_name_al}'

class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='', null=True, blank=True)
    title_al = models.CharField(max_length=50, null=True, blank=True)
    title_en = models.CharField(max_length=50, null=True, blank=True)
    price_L = models.IntegerField(null=True, blank=True)
    price_E = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return f'{self.title_al}'

class Offer(models.Model):
    image = models.ImageField(upload_to='', null=True, blank=True)
    title_al = models.CharField(max_length=50, null=True, blank=True)
    title_en = models.CharField(max_length=50, null=True, blank=True)
    price_L = models.IntegerField(null=True, blank=True)
    price_E = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return f'{self.title_al}'


class Table(models.Model):
    table = models.IntegerField(null=True, blank=True, editable=False)
    order = models.TextField(max_length=999999999, null=True, blank=True, editable=False)
    view_order = models.BooleanField(default=False)
    total = models.IntegerField(null=True, blank=True, editable=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.table} - {self.total} Lek'


class Overview(models.Model):
    table = models.IntegerField(null=True, blank=True, editable=False)
    order = models.TextField(max_length=999999999, null=True, blank=True, editable=False)
    total = models.IntegerField(null=True, blank=True, editable=False)
    paid_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'Tavolina-{self.table} - {self.total} Lek - {self.paid_date}'


class DailySummary(models.Model):
    date = models.DateField(auto_now_add=True, unique=True)
    products = models.JSONField(default=dict, blank=True, editable=False)
    total_sales = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return f'{self.date} - {self.total_sales} Lek'
