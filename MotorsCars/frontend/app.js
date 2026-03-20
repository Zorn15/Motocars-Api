// MotorsCars - Cliente API
const API_URL = "/api";

// --- Funciones auxiliares de Fetch ---

async function apiFetch(path, options = {}) {
  const res = await fetch(`${API_URL}${path}`, {
    headers: { "Content-Type": "application/json", ...options.headers },
    ...options,
  });
  if (res.status === 204) return null;
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: "Error desconocido" }));
    throw new Error(err.detail || res.statusText);
  }
  return res.json();
}

// --- API de Marcas ---

function getBrands() {
  return apiFetch("/brands");
}

function createBrand(data) {
  return apiFetch("/brands", { method: "POST", body: JSON.stringify(data) });
}

function deleteBrand(id) {
  return apiFetch(`/brands/${id}`, { method: "DELETE" });
}

function getCarsByBrand(brandId) {
  return apiFetch(`/brands/${brandId}/cars`);
}

// --- API de Autos ---

function getCars() {
  return apiFetch("/cars");
}

function getCar(id) {
  return apiFetch(`/cars/${id}`);
}

function createCar(data) {
  return apiFetch("/cars", { method: "POST", body: JSON.stringify(data) });
}

function updateCar(id, data) {
  return apiFetch(`/cars/${id}`, { method: "PUT", body: JSON.stringify(data) });
}

function deleteCar(id) {
  return apiFetch(`/cars/${id}`, { method: "DELETE" });
}

// --- Funciones de interfaz ---

function showToast(message, type = "success") {
  const toast = document.createElement("div");
  const bg = type === "error" ? "bg-red-600" : "bg-green-600";
  toast.className = `fixed top-4 right-4 z-[100] ${bg} text-white px-6 py-3 rounded-xl shadow-lg font-medium text-sm transition-opacity duration-300`;
  toast.textContent = message;
  document.body.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = "0";
    setTimeout(() => toast.remove(), 300);
  }, 2500);
}

function formatPrice(price) {
  return new Intl.NumberFormat("es-CO", { style: "currency", currency: "COP", maximumFractionDigits: 0 }).format(price);
}

function formatMileage(km) {
  if (km >= 1000) return `${(km / 1000).toFixed(1)}k km`;
  return `${km} km`;
}
