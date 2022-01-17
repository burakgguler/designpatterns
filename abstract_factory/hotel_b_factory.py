from abstract_factory.booking import Booking
from abstract_factory.customer import Customer
from abstract_factory.payment import Payment
from abstract_factory.room import Room
from hotel_factory import HotelFactory


class HotelBFactory(HotelFactory):
    def create_customer(self, cust_id, name) -> Customer:
        return super().create_customer(cust_id, name)

    def create_room(self, number, status) -> Room:
        return super().create_room(number, status)

    def create_payment(self, method) -> Payment:
        return super().create_payment(method)

    def create_booking(self, start_date, end_date, booking_type) -> Booking:
        return super().create_booking(start_date, end_date, booking_type)