-- Datos iniciales para MotorsCars

INSERT INTO brands (name, country, logo_url) VALUES
('Tesla', 'Estados Unidos', ''),
('Toyota', 'Japón', ''),
('BMW', 'Alemania', ''),
('Audi', 'Alemania', ''),
('Ford', 'Estados Unidos', ''),
('Honda', 'Japón', ''),
('Mercedes-Benz', 'Alemania', ''),
('Porsche', 'Alemania', '')
ON CONFLICT (name) DO NOTHING;

INSERT INTO cars (brand_id, model, year, mileage, price, fuel_type, transmission, description, whatsapp, image_url) VALUES
(1, 'Model S Plaid', 2023, 12000, 89900.00, 'Eléctrico', 'Automático', 'Doble motor tracción integral. Condición impecable, un solo dueño.', '573001234567', ''),
(1, 'Model 3 Long Range', 2022, 20000, 42000.00, 'Eléctrico', 'Automático', 'Gran autonomía y rendimiento. Capacidad de conducción autónoma.', '573009876543', ''),
(2, 'Camry XSE', 2023, 8000, 32500.00, 'Gasolina', 'Automático', 'Edición deportiva con asientos de cuero y techo panorámico.', '573005551234', ''),
(2, 'RAV4 Hybrid', 2022, 15000, 35000.00, 'Híbrido', 'Automático', 'Excelente rendimiento de combustible, equipado con tecnología.', NULL, ''),
(3, 'M5 Competition', 2022, 8500, 104500.00, 'Gasolina', 'Automático', 'Azul Marina Bay Metálico. Paquete M Sport completo.', '573112223344', ''),
(3, '3 Series M Sport', 2021, 18500, 45000.00, 'Gasolina', 'Automático', 'Azul Portimao. Un solo dueño, historial completo de servicio.', NULL, ''),
(4, 'R8 V10', 2020, 15000, 148000.00, 'Gasolina', 'Automático', 'Coupé Performance Quattro. Condición impresionante.', '573203334455', ''),
(4, 'A4 Premium', 2023, 5000, 41000.00, 'Gasolina', 'Automático', 'Motor turbo, tablero virtual, sonido premium.', NULL, ''),
(5, 'Mustang GT', 2023, 3000, 55000.00, 'Gasolina', 'Manual', 'Motor V8 5.0L. Paquete de rendimiento listo para pista.', '573154445566', ''),
(6, 'Civic Type R', 2023, 2000, 44000.00, 'Gasolina', 'Manual', 'Blanco Championship. El hatchback deportivo definitivo.', '573186667788', ''),
(7, 'E450 4MATIC', 2021, 24000, 62000.00, 'Gasolina', 'Automático', 'Sedán de lujo 4MATIC. Sonido premium Harman Kardon.', NULL, ''),
(8, '911 Carrera S', 2022, 9000, 135000.00, 'Gasolina', 'Automático', 'Transmisión PDK, paquete sport chrono. Impecable.', '573217778899', '');
