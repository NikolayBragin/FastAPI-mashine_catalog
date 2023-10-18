# в моделях только одна модель это клас кар +++
from sqlalchemy import Column, String, Integer

from database import Base


# Таблица машин
class Car(Base):
    __tablename__ = 'cars'
    car_id = Column(Integer, autoincrement=True, primary_key=True)
    car_name = Column(String)
    car_color = Column(String)
    car_body = Column(String)
