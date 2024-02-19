import requests
from tests.assertions.booking_assertions import *
from client.booking_client import BookingClient


client = BookingClient()


def test_get_all_booking_ids_returns_200():
    response = client.get_all_booking_ids()

    (assert_that(response.status_code, description=f"Status code is not {requests.codes.ok}").
        is_equal_to(requests.codes.ok))


def test_get_all_booking_ids_greater_than_zero():
    response = client.get_all_booking_ids()

    (assert_that(response.status_code, description=f"Status code is not {requests.codes.ok}").
        is_equal_to(requests.codes.ok))
    assert_that_booking_amount_greater_than_zero(response.json())
