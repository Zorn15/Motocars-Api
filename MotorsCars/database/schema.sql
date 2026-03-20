-- Esquema de Base de Datos MotorsCars
-- PostgreSQL

CREATE TABLE IF NOT EXISTS brands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(100),
    logo_url VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS cars (
    id SERIAL PRIMARY KEY,
    brand_id INTEGER NOT NULL REFERENCES brands(id) ON DELETE CASCADE,
    model VARCHAR(150) NOT NULL,
    year INTEGER NOT NULL CHECK (year >= 1900 AND year <= 2030),
    mileage INTEGER DEFAULT 0 CHECK (mileage >= 0),
    price NUMERIC(12, 2) NOT NULL CHECK (price >= 0),
    fuel_type VARCHAR(50) DEFAULT 'Gasolina',
    transmission VARCHAR(50) DEFAULT 'Automático',
    description TEXT,
    whatsapp VARCHAR(20),
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS car_images (
    id SERIAL PRIMARY KEY,
    car_id INTEGER NOT NULL REFERENCES cars(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    position INTEGER DEFAULT 0
);

-- Índices para mejorar el rendimiento de consultas
CREATE INDEX IF NOT EXISTS idx_cars_brand_id ON cars(brand_id);
CREATE INDEX IF NOT EXISTS idx_cars_year ON cars(year);
CREATE INDEX IF NOT EXISTS idx_car_images_car_id ON car_images(car_id);
