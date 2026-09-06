"""Payment-provider client used by the checkout service."""

import time
import uuid
import yaml
from pathlib import Path


CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "payment.yml"


class PaymentTimeoutError(Exception):
    """Raised when the external payment provider exceeds our timeout."""


class PaymentClient:
    def __init__(self):
        self.config = self._load_config()

    def _load_config(self) -> dict:
        with open(CONFIG_PATH, "r", encoding="utf-8") as config_file:
            return yaml.safe_load(config_file)["payment"]

    def _send_provider_request(
        self,
        order_id: str,
        amount: float,
        simulated_delay_seconds: float = 0.01,
    ) -> dict:
        """Simulate a request to the external payment provider."""
        timeout_seconds = self.config["timeout_seconds"]

        if simulated_delay_seconds > timeout_seconds:
            raise PaymentTimeoutError(
                f"Payment provider exceeded {timeout_seconds}s timeout"
            )

        time.sleep(simulated_delay_seconds)

        return {
            "status": "approved",
            "reference": f"PAY-{uuid.uuid4().hex[:8].upper()}",
            "order_id": order_id,
            "amount": amount,
        }

    def charge(
        self,
        order_id: str,
        amount: float,
        simulated_delay_seconds: float = 0.01,
    ) -> dict:
        """Send a payment request, retrying transient timeouts when configured."""
        retry_attempts = self.config["retry_attempts"]
        attempts = 0

        while attempts < retry_attempts:
            attempts += 1

            try:
                return self._send_provider_request(
                    order_id=order_id,
                    amount=amount,
                    simulated_delay_seconds=simulated_delay_seconds,
                )
            except PaymentTimeoutError:
                if attempts >= retry_attempts:
                    raise

        raise PaymentTimeoutError("Payment request exhausted configured attempts")
