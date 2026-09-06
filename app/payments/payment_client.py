"""Payment-provider client used by the checkout service."""

import time
import uuid
import yaml
from pathlib import Path


CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "payment.yml"


class PaymentClient:
    def __init__(self):
        self.config = self._load_config()

    def _load_config(self) -> dict:
        with open(CONFIG_PATH, "r", encoding="utf-8") as config_file:
            return yaml.safe_load(config_file)["payment"]

    def charge(self, order_id: str, amount: float) -> dict:
        """Simulate sending a payment request to an external provider."""
        timeout_seconds = self.config["timeout_seconds"]

        # Simulated provider request.
        time.sleep(0.01)

        return {
            "status": "approved",
            "reference": f"PAY-{uuid.uuid4().hex[:8].upper()}",
            "order_id": order_id,
            "amount": amount,
            "timeout_seconds": timeout_seconds,
        }
