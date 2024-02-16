import requests

from booking_client.base_client import BaseClient
from config import BASE_URL, AUTH_URL


class BookingClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = BASE_URL
        self.auth_url = AUTH_URL

    def get_all_booking_ids(self):
        return requests.get(self.base_url, headers=self.headers)
