import sqlite3

# Conectar a la base de datos
def conectar_db():
    conn = sqlite3.connect('biblioteca.db')
    return conn

# Inicializar las tablas
def inicializar_tablas():
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS autores (
        id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        nacionalidad TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS libros (
        id_libro INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        genero TEXT,
        id_autor INTEGER,
        FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
    )''')
    
    conn.commit()
    conn.close()

# Registrar autor
def registrar_autor(nombre, nacionalidad):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)', (nombre, nacionalidad))
    conn.commit()
    conn.close()

# Registrar libro
def registrar_libro(titulo, genero, id_autor):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO libros (titulo, genero, id_autor) VALUES (?, ?, ?)', (titulo, genero, id_autor))
    conn.commit()
    conn.close()

# Modificar libro
def modificar_libro(id_libro, nuevo_titulo, nuevo_genero, nuevo_id_autor):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE libros
    SET titulo = ?, genero = ?, id_autor = ?
    WHERE id_libro = ?
    ''', (nuevo_titulo, nuevo_genero, nuevo_id_autor, id_libro))
    conn.commit()
    conn.close()

# Borrar libro
def borrar_libro(id_libro):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM libros WHERE id_libro = ?', (id_libro,))
    conn.commit()
    conn.close()

# Generar reporte
def generar_reporte():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT libros.titulo, libros.genero, autores.nombre AS autor, autores.nacionalidad
    FROM libros
    JOIN autores ON libros.id_autor = autores.id_autor
    ''')
    reporte = cursor.fetchall()
    conn.close()
    return reporte

# Inicializar la base de datos
inicializar_tablas()

# Ejemplos de uso
registrar_autor('Gabriel García Márquez', 'Colombiano')
registrar_libro('Cien Años de Soledad', 'Realismo Mágico', 1)
modificar_libro(1, 'Cien Años de Soledad (Edición Revisada)', 'Realismo Mágico', 1)
borrar_libro(1)
reporte = generar_reporte()
for fila in reporte:
    print(fila)
