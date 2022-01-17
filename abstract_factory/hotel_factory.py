from customer import Customer
from room import Room
from payment import Payment
from booking import Booking


class HotelFactory:
    def create_customer(self, cust_id, name) -> Customer:
        pass

    def create_room(self, number, status) -> Room:
        pass

    def create_payment(self, method) -> Payment:
        pass

    def create_booking(self, start_date, end_date, booking_type) -> Booking:
        pass
