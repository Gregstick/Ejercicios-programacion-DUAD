from db import session
from Ejercicio_2_db import Users, Cars, Address

class UserService:
    def create(self, name):
        user = Users(name=name)
        session.add(user)
        session.commit()
        return user

    def modify(self, id, new_name):
        user = session.get(Users, id)
        if user:
            user.name = new_name
            session.commit()

    def delete(self, id):
        user = session.get(Users, id)
        if user:
            session.delete(user)
            session.commit()

    def get_all(self):
        return session.query(Users).all()


class CarsService:
    def create_car(self, make, users_id=None):
        car = Cars(make=make, users_id=users_id)
        session.add(car)
        session.commit()
        return car

    def modify_car(self, id, new_make):
        car = session.get(Cars, id)
        if car:
            car.make = new_make
            session.commit()

    def delete_car(self, id):
        car = session.get(Cars, id)
        if car:
            session.delete(car)
            session.commit()

    def associate_user(self, car_id, user_id):
        car = session.get(Cars, car_id)
        if car:
            car.user_id = user_id
            session.commit()

    def get_all_cars(self):
        return session.query(Cars).all()

class AddressService:

    def create_address(self, street, user_id):
        address = Address(street=street, user_id=user_id)
        session.add(address)
        session.commit()
        return address

    def modify_address(self, id, new_street):
        address = session.get(Address, id)
        if address:
            address.street = new_street
            session.commit()

    def delete_address(self, id):
        address = session.get(Address, id)
        if address:
            session.delete(address)
            session.commit()

    def get_all_addresses(self):
        return session.query(Address).all()