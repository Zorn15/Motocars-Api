from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    country = Column(String(100))
    logo_url = Column(String(500))

    cars = relationship("Car", back_populates="brand", cascade="all, delete-orphan")


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey("brands.id", ondelete="CASCADE"), nullable=False)
    model = Column(String(150), nullable=False)
    year = Column(Integer, nullable=False)
    mileage = Column(Integer, default=0)
    price = Column(Numeric(12, 2), nullable=False)
    fuel_type = Column(String(50), default="Gasolina")
    transmission = Column(String(50), default="Automático")
    description = Column(Text)
    whatsapp = Column(String(20))
    image_url = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    brand = relationship("Brand", back_populates="cars")
    images = relationship("CarImage", back_populates="car", cascade="all, delete-orphan", order_by="CarImage.position")


class CarImage(Base):
    __tablename__ = "car_images"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id", ondelete="CASCADE"), nullable=False)
    image_url = Column(Text, nullable=False)
    position = Column(Integer, default=0)

    car = relationship("Car", back_populates="images")
