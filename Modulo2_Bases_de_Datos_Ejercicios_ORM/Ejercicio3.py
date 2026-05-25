from db import engine
from Ejercicio_2_db import Base
from Ejercicio4 import UserService, CarsService, AddressService

def main():
    Base.metadata.create_all(engine)
    print("Tablas listas")

    user_service = UserService()
    car_service = CarsService()
    address_service = AddressService()

    user = user_service.create("Greg")

    address_service.create_address("San Jose", user.id)

    car = car_service.create_car("Toyota")

    car_service.associate_user(car.id, user.id)

    print(user_service.get_all())
    print(car_service.get_all_cars())
    print(address_service.get_all_addresses())


if __name__ == "__main__":
    main()