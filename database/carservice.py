# в сервисе тоже будет орин сервис = кар_сервис (внутри три функции: удалить добавить получить)

from database.models import Car
from database import get_db

# Добавить машину
def add_car_db(car_name, car_color, car_body):
    db = next(get_db())
    new_car = Car(car_name=car_name, car_color=car_color, car_body=car_body)
    db.add(new_car)
    db.commit()
    return "Машина добавлена"


# Получить информацию о машине
def get_car_db(car_id):
    db = next(get_db())
    exact_car = db.query(Car).filter_by(car_id=car_id).first()
    return exact_car


# Удалить машину
def delete_car_db(car_id):
    db = next(get_db())
    exact_car = db.query(Car).filter_by(car_id=car_id).first()
    if exact_car:
        db.delete(exact_car)
        db.commit()
        return "Машина удалена"
    return "Машина не найдена"
