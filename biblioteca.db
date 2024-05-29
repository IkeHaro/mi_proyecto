CREATE TABLE IF NOT EXISTS autores (
    id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nacionalidad TEXT
);

CREATE TABLE IF NOT EXISTS libros (
    id_libro INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    genero TEXT,
    id_autor INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);
