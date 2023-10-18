from pydantic import BaseModel


# Класс валидации для машин
class CarRegisterModel(BaseModel):
    car_name: str
    car_color: str
    car_body: str
