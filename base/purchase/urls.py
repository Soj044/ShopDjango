from django.urls import path

from . import views
from .views import CreatePurchaseView, CancelPurchaseView

app_name = 'purchase'

urlpatterns = [
    path('buy/<slug:course_slug>', CreatePurchaseView.as_view(), name='buy'),
    path('buy/cancel_purchase/<int:pk>', CancelPurchaseView.as_view(), name='cancel')
    # path('cart/', CartView.as_view(), name='cart')
]