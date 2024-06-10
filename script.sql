CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    descripcion TEXT,
    precio REAL NOT NULL CHECK (precio > 0),
    cantidad INTEGER NOT NULL CHECK (cantidad >= 0),
    categoria TEXT NOT NULL
);