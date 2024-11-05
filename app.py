from flask import Flask, render_template, request, redirect, url_for
from backend.models import ProblemaVeicular
from backend.database import session
import os

app = Flask(__name__, 
            template_folder='backend/templates', 
            static_folder='backend/static')

@app.route('/')
def index():
    problemas = session.query(ProblemaVeicular).all()
    return render_template('index.html', problemas=problemas)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        problema = request.form['problema']
        sintoma = request.form['sintoma']
        causa = request.form['causa']
        solucao = request.form['solucao']

        new_problem = ProblemaVeicular(
            problema=problema,
            sintoma=sintoma,
            causa=causa,
            solucao=solucao
        )
        session.add(new_problem)
        session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    problema = session.query(ProblemaVeicular).filter_by(id=id).first()
    if request.method == 'POST':
        problema.problema = request.form['problema']
        problema.sintoma = request.form['sintoma']
        problema.causa = request.form['causa']
        problema.solucao = request.form['solucao']

        session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', problema=problema)

@app.route('/delete/<int:id>')
def delete_web(id):
    problema = session.query(ProblemaVeicular).filter_by(id=id).first()
    session.delete(problema)
    session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
