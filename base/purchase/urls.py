from django.urls import path

from . import views
from .views import CreatePurchaseView

app_name = 'purchase'

urlpatterns = [
    path('buy/<slug:course_slug>', CreatePurchaseView.as_view(), name='buy'),
    # path('cart/', CartView.as_view(), name='cart')
]