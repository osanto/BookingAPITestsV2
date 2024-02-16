from assertpy import assert_that


def assert_that_booking_amount_greater_than_zero(response):
    bookings_amount = len(response)
    assert_that(bookings_amount).is_not_zero()
    print(f"Bookings Amount is: {bookings_amount}")