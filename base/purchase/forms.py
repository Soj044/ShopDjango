from django import forms
from django.contrib.auth import get_user_model

from purchase.models import Purchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['courses_qty', 'total_price']