import pytest

from app.checkout.checkout import CheckoutService
from app.payments.payment_client import PaymentClient, PaymentTimeoutError


def test_successful_checkout_returns_payment_reference():
    service = CheckoutService()

    result = service.process_checkout(
        order_id="ORDER-1001",
        amount=49.99,
    )

    assert result["payment_status"] == "approved"
    assert result["payment_reference"].startswith("PAY-")


def test_payment_client_raises_timeout_when_provider_is_too_slow():
    client = PaymentClient()

    with pytest.raises(PaymentTimeoutError):
        client.charge(
            order_id="ORDER-1002",
            amount=29.99,
            simulated_delay_seconds=6,
        )
