from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('category/<slug:slug>/', CategoryView.as_view(), name="category"),
    path('offer/', OfferView.as_view(), name="offer"),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart-views/', CartViews.as_view(), name="cart_views"),
    path('delete-item-from-cart/', DeleteItemFormCartView.as_view(), name="delete-item-from-cart"),
    path('update-cart/', UpdateCartView.as_view(), name="update-cart"),
    path('table/', TableView.as_view(), name="table"),
    path('done/', DoneView.as_view(), name="done"),
    path('daily-summary/', DailySummaryView.as_view(), name="daily_summary"),
]