from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# -- Esquemas de Marca --

class BrandBase(BaseModel):
    name: str
    country: Optional[str] = None
    logo_url: Optional[str] = None


class BrandCreate(BrandBase):
    pass


class BrandResponse(BrandBase):
    id: int

    class Config:
        from_attributes = True


# -- Esquemas de Imagen --

class CarImageBase(BaseModel):
    image_url: str
    position: int = 0


class CarImageResponse(CarImageBase):
    id: int

    class Config:
        from_attributes = True


# -- Esquemas de Auto --

class CarBase(BaseModel):
    brand_id: int
    model: str
    year: int
    mileage: Optional[int] = 0
    price: float
    fuel_type: Optional[str] = "Gasolina"
    transmission: Optional[str] = "Automático"
    description: Optional[str] = None
    whatsapp: Optional[str] = None
    image_url: Optional[str] = None


class CarCreate(CarBase):
    images: Optional[List[str]] = None


class CarUpdate(BaseModel):
    brand_id: Optional[int] = None
    model: Optional[str] = None
    year: Optional[int] = None
    mileage: Optional[int] = None
    price: Optional[float] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None
    description: Optional[str] = None
    whatsapp: Optional[str] = None
    image_url: Optional[str] = None
    images: Optional[List[str]] = None


class CarResponse(CarBase):
    id: int
    created_at: Optional[datetime] = None
    brand: Optional[BrandResponse] = None
    images: List[CarImageResponse] = []

    class Config:
        from_attributes = True
