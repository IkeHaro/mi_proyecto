from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload
from models import Session, Empresa, Oferta

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
    if request.method == 'POST':
        nombre = request.form['nombre']
        ubicacion = request.form['ubicacion']
        industria = request.form['industria']
        codigo_postal = request.form['codigo_postal']
        representante = request.form['representante']
        numero_contacto = request.form['numero_contacto']
        session = Session()
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
    return render_template('add_empresa.html')

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

if __name__ == '__main__':
    app.run(debug=True)
