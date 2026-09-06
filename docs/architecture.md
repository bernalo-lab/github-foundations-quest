# Application Architecture

The sample application represents a deliberately small checkout flow.

```text
Customer
   |
   v
Checkout Service
   |
   v
Payment Client
   |
   v
External Payment Provider
```

## Components

### Checkout Service

Receives the order identifier and payment amount, then delegates payment processing to the payment client.

Location:

`app/checkout/checkout.py`

### Payment Client

Reads payment-provider configuration and sends the payment request.

Location:

`app/payments/payment_client.py`

### Payment Configuration

Contains provider-specific timeout and retry settings.

Location:

`config/payment.yml`

### Tests

The initial automated test verifies that a normal successful checkout returns an approved payment and a payment reference.

Location:

`tests/test_payments.py`

## Scope

This training application is intentionally small. Its purpose is to provide a repository that can be investigated, rather than to model a production payment platform in full.
