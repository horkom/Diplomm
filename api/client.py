import requests
from config.config import BASE_URL, TOKEN


class ApiClient:
    def __init__(self) -> None:
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        }

    def get(self, path: str, **kwargs) -> requests.Response:
        return requests.get(
            f"{self.base_url}{path}", headers=self.headers, **kwargs
            )

    def post(
            self, path: str, json: dict | None = None, **kwargs
            ) -> requests.Response:
        return requests.post(
            f"{self.base_url}{path}",
            headers=self.headers, json=json, **kwargs
            )
