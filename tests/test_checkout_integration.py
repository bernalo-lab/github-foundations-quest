"""Integration-style tests for the checkout and payment flow.

These tests intentionally focus on the application's expected behaviour:
a normal payment succeeds, while a provider response beyond the configured
timeout is surfaced as a timeout.
"""

import pytest

from app.checkout.checkout import CheckoutService
from app.payments.payment_client import PaymentClient, PaymentTimeoutError


def test_checkout_completes_when_provider_responds_normally():
    service = CheckoutService(
        payment_client=PaymentClient()
    )

    result = service.process_checkout(
        order_id="ORDER-2001",
        amount=79.99,
    )

    assert result["order_id"] == "ORDER-2001"
    assert result["payment_status"] == "approved"
    assert result["payment_reference"].startswith("PAY-")


def test_payment_times_out_when_provider_exceeds_configured_limit():
    client = PaymentClient()

    with pytest.raises(PaymentTimeoutError):
        client.charge(
            order_id="ORDER-2002",
            amount=19.99,
            simulated_delay_seconds=6,
        )
