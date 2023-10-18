# три роута +++
# получить машину (пост) +++
# добавить машину (гет) +++
# удалить машину (делете) +++
#
# в сервисе тоже будет орин сервис = кар_сервис (внутри три функции: удалить добавить получить)
# в моделях только одна модель это клас кар +++

from fastapi import FastAPI

from car.car_api import car_router

# Создать базу данных
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

# Регистрация компонента
app.include_router(car_router)
