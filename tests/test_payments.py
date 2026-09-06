from app.checkout.checkout import CheckoutService


def test_successful_checkout_returns_payment_reference():
    service = CheckoutService()

    result = service.process_checkout(
        order_id="ORDER-1001",
        amount=49.99,
    )

    assert result["payment_status"] == "approved"
    assert result["payment_reference"].startswith("PAY-")
