from models import Session, Empresa, Oferta, Candidato, Aplicacion

session = Session()

# Consultar y mostrar todas las empresas
empresas = session.query(Empresa).all()
print("Empresas:")
for empresa in empresas:
    print(f"ID: {empresa.empresa_id}, Nombre: {empresa.nombre}, Ubicación: {empresa.ubicacion}, Industria: {empresa.industria}")

# Consultar y mostrar todas las ofertas
ofertas = session.query(Oferta).all()
print("\nOfertas de Trabajo:")
for oferta in ofertas:
    print(f"ID: {oferta.oferta_id}, Título: {oferta.titulo}, Tipo de Empleo: {oferta.tipo_empleo}, Salario: {oferta.salario}, Empresa ID: {oferta.empresa_id}")

# Consultar y mostrar todos los candidatos
candidatos = session.query(Candidato).all()
print("\nCandidatos:")
for candidato in candidatos:
    print(f"ID: {candidato.candidato_id}, Nombre: {candidato.nombre}, Correo Electrónico: {candidato.correo_electronico}, Nivel de Experiencia: {candidato.nivel_experiencia}")

# Consultar y mostrar todas las aplicaciones
aplicaciones = session.query(Aplicacion).all()
print("\nAplicaciones:")
for aplicacion in aplicaciones:
    print(f"ID: {aplicacion.aplicacion_id}, Candidato ID: {aplicacion.candidato_id}, Oferta ID: {aplicacion.oferta_id}, Fecha de Aplicación: {aplicacion.fecha_aplicacion}")

session.close()
