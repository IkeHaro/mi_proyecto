from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload
from models import Session, Empresa, Oferta, Candidato, Aplicacion

app = Flask(__name__)

@app.route('/')
def index():
    session = Session()
    empresas = session.query(Empresa).all()
    ofertas = session.query(Oferta).options(joinedload(Oferta.empresa)).all()
    session.close()
    return render_template('index.html', empresas=empresas, ofertas=ofertas)

@app.route('/add_empresa', methods=['GET', 'POST'])
def add_empresa():
    session = Session()
    if request.method == 'POST':
        nombre = request.form['nombre']
        ubicacion = request.form['ubicacion']
        industria = request.form['industria']
        codigo_postal = request.form['codigo_postal']
        representante = request.form['representante']
        numero_contacto = request.form['numero_contacto']
        nueva_empresa = Empresa(
            nombre=nombre,
            ubicacion=ubicacion,
            industria=industria,
            codigo_postal=codigo_postal,
            representante=representante,
            numero_contacto=numero_contacto
        )
        session.add(nueva_empresa)
        session.commit()
        session.close()
        return redirect(url_for('index'))
    empresas = session.query(Empresa).all()
    session.close()
    return render_template('add_empresa.html', empresas=empresas)

@app.route('/edit_empresa/<int:empresa_id>', methods=['GET', 'POST'])
def edit_empresa(empresa_id):
    session = Session()
    empresa = session.query(Empresa).get(empresa_id)
    if request.method == 'POST':
        empresa.nombre = request.form['nombre']
        empresa.ubicacion = request.form['ubicacion']
        empresa.industria = request.form['industria']
        empresa.codigo_postal = request.form['codigo_postal']
        empresa.representante = request.form['representante']
        empresa.numero_contacto = request.form['numero_contacto']
        session.commit()
        session.close()
        return redirect(url_for('index'))
    session.close()
    return render_template('edit_empresa.html', empresa=empresa)

@app.route('/delete_empresa', methods=['POST'])
def delete_empresa():
    empresa_id = request.form['empresa_id']
    session = Session()
    empresa = session.query(Empresa).get(empresa_id)
    if empresa:
        session.delete(empresa)
        session.commit()
    session.close()
    return redirect(url_for('add_empresa'))

@app.route('/add_oferta', methods=['GET', 'POST'])
def add_oferta():
    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo_empleo = request.form['tipo_empleo']
        salario = request.form['salario']
        empresa_id = request.form['empresa_id']
        session = Session()
        nueva_oferta = Oferta(
            titulo=titulo,
            tipo_empleo=tipo_empleo,
            salario=salario,
            empresa_id=empresa_id
        )
        session.add(nueva_oferta)
        session.commit()
        session.close()
        return redirect(url_for('index'))
    session = Session()
    empresas = session.query(Empresa).all()
    session.close()
    return render_template('add_oferta.html', empresas=empresas)

@app.route('/add_candidato', methods=['GET', 'POST'])
def add_candidato():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo_electronico = request.form['correo_electronico']
        nivel_experiencia = request.form['nivel_experiencia']
        session = Session()
        nuevo_candidato = Candidato(
            nombre=nombre,
            correo_electronico=correo_electronico,
            nivel_experiencia=nivel_experiencia
        )
        session.add(nuevo_candidato)
        session.commit()
        session.close()
        return redirect(url_for('index'))
    return render_template('add_candidato.html')

@app.route('/add_aplicacion', methods=['GET', 'POST'])
def add_aplicacion():
    session = Session()
    if request.method == 'POST':
        candidato_id = request.form['candidato_id']
        oferta_id = request.form['oferta_id']
        fecha_aplicacion = request.form['fecha_aplicacion']
        nueva_aplicacion = Aplicacion(
            candidato_id=candidato_id,
            oferta_id=oferta_id,
            fecha_aplicacion=fecha_aplicacion
        )
        session.add(nueva_aplicacion)
        session.commit()
        session.close()
        return redirect(url_for('index'))
    candidatos = session.query(Candidato).all()
    ofertas = session.query(Oferta).all()
    session.close()
    return render_template('add_aplicacion.html', candidatos=candidatos, ofertas=ofertas)

@app.route('/reporte')
def reporte():
    session = Session()
    resultados = session.query(
        Oferta.titulo,
        Oferta.tipo_empleo,
        Oferta.salario,
        Empresa.nombre.label('nombre_empresa'),
        Candidato.nombre.label('nombre_candidato')
    ).join(Empresa, Oferta.empresa_id == Empresa.empresa_id) \
     .join(Aplicacion, Oferta.oferta_id == Aplicacion.oferta_id) \
     .join(Candidato, Aplicacion.candidato_id == Candidato.candidato_id).all()
    
    session.close()
    return render_template('reporte.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
