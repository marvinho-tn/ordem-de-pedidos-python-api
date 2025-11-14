import httpx

from infra.config.env import settings


class OrderExternalService:
    BASE_URL = settings.orders_api_host

    @staticmethod
    def update_status(id: str) -> str:
        with httpx.Client() as client:
            response = client.get(f"{OrderExternalService.BASE_URL}/orders/{id}/update-status")
            data = response.json()
            result = data["result"]
            
            if not result is None:
                return result["status"]
            
            return None