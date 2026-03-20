# MotorsCars - Documentación de API

**URL Base:** `http://localhost:8000/api`

**Documentación Interactiva (Swagger):** `http://localhost:8000/docs`

---

## Marcas (Brands)

### GET /api/brands
Listar todas las marcas.

**Respuesta:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "Tesla",
    "country": "Estados Unidos",
    "logo_url": ""
  }
]
```

### POST /api/brands
Crear una nueva marca.

**Cuerpo de la petición:**
```json
{
  "name": "Chevrolet",
  "country": "Estados Unidos",
  "logo_url": null
}
```

**Respuesta:** `201 Created`
```json
{
  "id": 9,
  "name": "Chevrolet",
  "country": "Estados Unidos",
  "logo_url": null
}
```

**Errores:**
- `400` - La marca ya existe

### DELETE /api/brands/{id}
Eliminar una marca y todos sus autos (cascada).

**Respuesta:** `204 No Content`

**Errores:**
- `404` - Marca no encontrada

### GET /api/brands/{id}/cars
Listar todos los autos de una marca específica.

**Respuesta:** `200 OK`
```json
[
  {
    "id": 1,
    "brand_id": 1,
    "model": "Model S Plaid",
    "year": 2023,
    "mileage": 12000,
    "price": 89900.0,
    "fuel_type": "Eléctrico",
    "transmission": "Automático",
    "description": "Doble motor tracción integral. Condición impecable.",
    "whatsapp": "573001234567",
    "image_url": "",
    "created_at": "2026-03-16T10:00:00",
    "brand": {
      "id": 1,
      "name": "Tesla",
      "country": "Estados Unidos",
      "logo_url": ""
    }
  }
]
```

**Errores:**
- `404` - Marca no encontrada

---

## Autos (Cars)

### GET /api/cars
Listar todos los autos con información de la marca.

**Respuesta:** `200 OK`
```json
[
  {
    "id": 1,
    "brand_id": 1,
    "model": "Model S Plaid",
    "year": 2023,
    "mileage": 12000,
    "price": 89900.0,
    "fuel_type": "Eléctrico",
    "transmission": "Automático",
    "description": "Doble motor tracción integral.",
    "whatsapp": "573001234567",
    "image_url": "",
    "created_at": "2026-03-16T10:00:00",
    "brand": {
      "id": 1,
      "name": "Tesla",
      "country": "Estados Unidos",
      "logo_url": ""
    }
  }
]
```

### GET /api/cars/{id}
Obtener un auto por su ID.

**Respuesta:** `200 OK` (mismo formato, objeto individual)

**Errores:**
- `404` - Auto no encontrado

### POST /api/cars
Crear una nueva publicación de auto.

**Cuerpo de la petición:**
```json
{
  "brand_id": 3,
  "model": "X5 M",
  "year": 2023,
  "mileage": 5000,
  "price": 95000.00,
  "fuel_type": "Gasolina",
  "transmission": "Automático",
  "description": "Completamente equipado.",
  "whatsapp": "573001234567",
  "image_url": null
}
```

**Respuesta:** `201 Created`

**Errores:**
- `400` - Marca no encontrada

### PUT /api/cars/{id}
Actualizar un auto existente. Solo enviar los campos a actualizar.

**Cuerpo de la petición:**
```json
{
  "price": 90000.00,
  "mileage": 6000
}
```

**Respuesta:** `200 OK`

**Errores:**
- `404` - Auto no encontrado
- `400` - Marca no encontrada (si se actualiza brand_id)

### DELETE /api/cars/{id}
Eliminar una publicación de auto.

**Respuesta:** `204 No Content`

**Errores:**
- `404` - Auto no encontrado

---

## Formato de Errores

Todos los errores retornan JSON:
```json
{
  "detail": "Mensaje de error aquí"
}
```

## Códigos de Estado HTTP

| Código | Significado |
|--------|-------------|
| 200 | Éxito |
| 201 | Creado |
| 204 | Eliminado (sin contenido) |
| 400 | Petición incorrecta |
| 404 | No encontrado |
| 422 | Error de validación |
| 500 | Error del servidor |
