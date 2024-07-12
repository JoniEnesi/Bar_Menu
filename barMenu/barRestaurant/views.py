from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.utils import timezone
# Create your views here.


class HomeView(ListView):
    template_name = 'index.html'
    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['language'] = self.request.COOKIES.get('lang', 'al')
        return context


class CategoryView(ListView):
    template_name = 'category.html'
    model = Menu

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        prodcategory = Category.objects.get(slug=self.kwargs['slug'])
        return qs.filter(category=prodcategory)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = self.request.COOKIES.get('lang', 'al')
        return context


class OfferView(ListView):
    template_name = 'offer.html'
    model = Offer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["offer"] = Offer.objects.all()
        context['language'] = self.request.COOKIES.get('lang', 'al')
        return context


class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        cart_product = {}
        try:
            cart_product[str(request.GET['id'])] = {
                'title_al': request.GET['title_al'],
                'title_en': request.GET['title_en'],
                'qty': request.GET['qty'],
                'price': request.GET['price']
            }

            if 'cart_data_obj' in request.session:
                if str(request.GET['id']) in request.session['cart_data_obj']:
                    cart_data = request.session['cart_data_obj']
                    cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
                    cart_data.update(cart_data)
                    request.session['cart_data_obj'] = cart_data
                else:
                    cart_data = request.session['cart_data_obj']
                    cart_data.update(cart_product)
                    request.session['cart_data_obj'] = cart_data
            else:
                request.session['cart_data_obj'] = cart_product

            return JsonResponse({'data': request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})

        except MultiValueDictKeyError as e:
            return JsonResponse({'error': str(e)})


class CartViews(View):
    template_name = 'cart_views.html'

    def get(self, request, *args, **kwargs):
        language = request.COOKIES.get('lang', 'al')
        cart_total_amount = 0
        subtotal_without_tax = 0
        tax_value = 0
        if 'cart_data_obj' in request.session:
            for product_id, item in request.session['cart_data_obj'].items():
                cart_total_amount += int(item['qty']) * float(item['price'])
                tax_value = cart_total_amount * 20 / 100
                subtotal_without_tax = cart_total_amount - tax_value
            context = {'cart_data': request.session['cart_data_obj'],
                       'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount, 'language':language, 'subtotal_without_tax':subtotal_without_tax, 'tax_value':tax_value}
            return render(request, self.template_name, context)
        else:
            messages.warning(request, "Your cart is empty!")
            messages.error(request, "Nuk keni asnje porosi!")
            return redirect('home')

    def post(self, request, *args, **kwargs):
        language = request.COOKIES.get('lang', 'al')
        cart_total_amount = 0

        order_content = []
        for product_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
            order_content.append(f"{item['qty']} - {item['title_al' if language == 'al' else 'title_en']}")

        return redirect('table')


class DeleteItemFormCartView(View):
    def get(self, request):
        product_id = str(request.GET['id'])

        if 'cart_data_obj' in request.session:
            if product_id in request.session['cart_data_obj']:
                cart_data = request.session['cart_data_obj']
                del request.session['cart_data_obj'][product_id]
                request.session['cart_data_obj'] = cart_data

            if not request.session['cart_data_obj']:
                del request.session['cart_data_obj']
                return JsonResponse({"redirect": True})

            cart_total_amount = 0
            subtotal_without_tax = 0
            tax_value = 0
            for product_id, item in request.session['cart_data_obj'].items():
                cart_total_amount += int(item['qty']) * float(item['price'])
                tax_value = cart_total_amount * 20 / 100
                subtotal_without_tax = cart_total_amount - tax_value

            context = render_to_string("cart-list.html", {
                'cart_data': request.session['cart_data_obj'],
                'totalcartitems': len(request.session['cart_data_obj']),
                'cart_total_amount': cart_total_amount,
                'subtotal_without_tax': subtotal_without_tax,
                'tax_value': tax_value
            })

            return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})

        return JsonResponse({"error": "Cart is empty or item not found"}, status=400)



class UpdateCartView(View):
    def get(self, request):
        product_id = str(request.GET['id'])
        product_qty = request.GET['qty']

        if 'cart_data_obj' in request.session:
            if product_id in request.session['cart_data_obj']:
                cart_data = request.session['cart_data_obj']
                cart_data[str(request.GET['id'])]['qty'] = product_qty
                request.session['cart_data_obj'] = cart_data

        cart_total_amount = 0
        subtotal_without_tax = 0
        tax_value = 0
        if 'cart_data_obj' in request.session:
            for product_id, item in request.session['cart_data_obj'].items():
                cart_total_amount += int(item['qty']) * float(item['price'])
                tax_value = cart_total_amount * 20 / 100
                subtotal_without_tax = cart_total_amount - tax_value

        context = render_to_string("cart-list.html", {'cart_data': request.session['cart_data_obj'],
                                                      'totalcartitems': len(request.session['cart_data_obj']),
                                                      'cart_total_amount': cart_total_amount,
                                                      'subtotal_without_tax': subtotal_without_tax,'tax_value': tax_value
        })

        return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})


class TableView(ListView):
    template_name = 'table.html'
    model = Table

    def get(self, request, *args, **kwargs):
        messages.success(request, format_html(
            "Ju lutem shkruani numrin e tavolines ku jeni ulur... <br> (Please write the number of table you are sitting at...)"))
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        table_number = request.POST.get('table')

        cart_total_amount = 0
        language = request.COOKIES.get('lang', 'al')
        order_content = []
        for product_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
            order_content.append(f"{item['qty']} - {item['title_al']}__")

        order_content_str = "\n".join(order_content)
        order = Table.objects.create(order=order_content_str, total=cart_total_amount, table=table_number)
        del request.session['cart_data_obj']

        return redirect('done')


class DoneView(ListView):
    template_name = 'done.html'
    model = Table


class DailySummaryView(View):
    template_name = 'daily_summary.html'

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        try:
            summary = DailySummary.objects.get(date=today)
        except DailySummary.DoesNotExist:
            summary = None

        context = {
            'summary': summary,
            'date': today
        }
        return render(request, self.template_name, context)