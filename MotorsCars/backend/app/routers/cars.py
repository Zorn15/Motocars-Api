from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from app.database import get_db
from app.models import Car, Brand, CarImage
from app.schemas import CarCreate, CarUpdate, CarResponse

router = APIRouter(prefix="/api/cars", tags=["cars"])


@router.get("", response_model=List[CarResponse])
def list_cars(db: Session = Depends(get_db)):
    return db.query(Car).options(joinedload(Car.brand), joinedload(Car.images)).order_by(Car.created_at.desc()).all()


@router.get("/{car_id}", response_model=CarResponse)
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(Car).options(joinedload(Car.brand), joinedload(Car.images)).filter(Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return car


@router.post("", response_model=CarResponse, status_code=201)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    brand = db.query(Brand).filter(Brand.id == car.brand_id).first()
    if not brand:
        raise HTTPException(status_code=400, detail="Marca no encontrada")

    car_data = car.model_dump(exclude={"images"})
    db_car = Car(**car_data)
    db.add(db_car)
    db.flush()

    if car.images:
        for i, url in enumerate(car.images[:10]):
            db.add(CarImage(car_id=db_car.id, image_url=url, position=i))
        if not db_car.image_url:
            db_car.image_url = car.images[0]

    db.commit()
    db.refresh(db_car)
    return db.query(Car).options(joinedload(Car.brand), joinedload(Car.images)).filter(Car.id == db_car.id).first()


@router.put("/{car_id}", response_model=CarResponse)
def update_car(car_id: int, car_data: CarUpdate, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Auto no encontrado")

    update_dict = car_data.model_dump(exclude_unset=True)
    images_list = update_dict.pop("images", None)

    if "brand_id" in update_dict:
        brand = db.query(Brand).filter(Brand.id == update_dict["brand_id"]).first()
        if not brand:
            raise HTTPException(status_code=400, detail="Marca no encontrada")

    for key, value in update_dict.items():
        setattr(car, key, value)

    if images_list is not None:
        db.query(CarImage).filter(CarImage.car_id == car_id).delete()
        for i, url in enumerate(images_list[:10]):
            db.add(CarImage(car_id=car_id, image_url=url, position=i))
        if images_list:
            car.image_url = images_list[0]

    db.commit()
    db.refresh(car)
    return db.query(Car).options(joinedload(Car.brand), joinedload(Car.images)).filter(Car.id == car.id).first()


@router.delete("/{car_id}", status_code=204)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    db.delete(car)
    db.commit()
