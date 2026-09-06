"""Simple checkout flow used by the GitHub Foundations Quest."""

from app.payments.payment_client import PaymentClient


class CheckoutService:
    def __init__(self, payment_client=None):
        self.payment_client = payment_client or PaymentClient()

    def process_checkout(self, order_id: str, amount: float) -> dict:
        """Process a payment request for an order."""
        payment_result = self.payment_client.charge(
            order_id=order_id,
            amount=amount,
        )

        return {
            "order_id": order_id,
            "payment_status": payment_result["status"],
            "payment_reference": payment_result["reference"],
        }
