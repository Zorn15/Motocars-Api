from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Brand, Car
from app.schemas import BrandCreate, BrandResponse, CarResponse

router = APIRouter(prefix="/api/brands", tags=["brands"])


@router.get("", response_model=List[BrandResponse])
def list_brands(db: Session = Depends(get_db)):
    return db.query(Brand).order_by(Brand.name).all()


@router.post("", response_model=BrandResponse, status_code=201)
def create_brand(brand: BrandCreate, db: Session = Depends(get_db)):
    existing = db.query(Brand).filter(Brand.name == brand.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Brand already exists")
    db_brand = Brand(**brand.model_dump())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


@router.delete("/{brand_id}", status_code=204)
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    db.delete(brand)
    db.commit()


@router.get("/{brand_id}/cars", response_model=List[CarResponse])
def list_cars_by_brand(brand_id: int, db: Session = Depends(get_db)):
    brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    cars = db.query(Car).filter(Car.brand_id == brand_id).order_by(Car.created_at.desc()).all()
    return cars
