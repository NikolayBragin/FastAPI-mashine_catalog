from fastapi import APIRouter
from datetime import datetime

from database.carservice import add_car_db, get_car_db, delete_car_db

from car import CarRegisterModel

car_router = APIRouter(prefix='/car', tags=['Машины'])

# Добавить машину
@car_router.post('/add-car')
async def add_car(data: CarRegisterModel):
    # Переводим пайдентик в обычный словарь
    new_car_data = data.model_dump()
    result = add_car_db(**new_car_data)
    return {'status': 1, 'message': result}

# Получить машину
@car_router.get('/get-car')
async def get_car(car_id: int):
    result = get_car_db(car_id)
    return {'status': 1, 'message': result}


# Удалить машину
@car_router.delete('/delete-car')
async def delete_car(car_id: int):
    result = delete_car_db(car_id)
    return {'status': 1, 'message': result}
