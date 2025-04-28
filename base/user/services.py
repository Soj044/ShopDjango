from purchase.models import Purchase


class PurchaseByUserService:
    def get_purchases(self, user_id):
        return Purchase.objects.filter(buyer_id=user_id).order_by('-purchase_date')
