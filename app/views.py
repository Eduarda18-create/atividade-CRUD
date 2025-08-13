from app import app
from app.models.prova_model import ProvaModel
from app.models.materia_model import MateriaModel
from app.service.prova_service import ProvaService
from app.service.materia_service import MateriaService
from flask import render_template, request, url_for, redirect

prova_service = ProvaService()
materia_service = MateriaService()

@app.route('/')
def index():
    return redirect(url_for('list_materias'))

@app.route('/materias')
def list_materias():
    materias = materia_service.get_all_materias()
    return render_template('materia/list.html', materias=materias)

@app.route('/materias/novo', methods=['GET', 'POST'])
def create_materia():
    if request.method == 'POST':
        nome = request.form['nome']
        professor = request.form['professor']
        descricao = request.form['descricao']
        materia_service.create_materia(MateriaModel(id=None, nome=nome, professor=professor, descricao=descricao))
        return redirect(url_for('list_materias'))
    return render_template('materia/form.html')
        

@app.route('/materias/editar/<int:id>', methods=['GET', 'POST'])
def edit_materia(id):
    materia = materia_service.get_materia_by_id(id)
    if request.method == 'POST':
        materia_service.update_materia(MateriaModel(
            id=materia.get_id(),
            nome=request.form['nome'],
            professor=request.form['professor'],
            descricao=request.form['descricao']
        ))
        return redirect(url_for('list_materias'))
    return render_template('materia/form.html', materia=materia)
        
        
@app.route('/materias/excluir/<int:id>')
def delete_materia(id):
    materia_service.delete_materia(id)
    return redirect(url_for('list_materias'))

@app.route('/provas')
def list_provas():
    provas = prova_service.get_all_provas()
    return render_template('prova/list.html', provas=provas)

@app.route('/provas/novo', methods=['GET', 'POST'])
def create_prova():
    print(request.form)
    if request.method == 'POST':
        materia_id = request.form['materia_id']
        data = request.form['data']
        peso = request.form['peso']
        prova = ProvaModel(id=None, data=data, peso=peso, materia_id=materia_id)
        try:
            prova_service.create_prova(prova)
            return redirect(url_for('list_provas'))
        except ValueError as e:
            return render_template('prova/form.html', error=str(e), prova=prova)
    materias = materia_service.get_all_materias()
    return render_template('prova/form.html', materias=materias)

@app.route('/provas/editar/<int:id>', methods=['GET', 'POST'])
def edit_prova(id):
    prova = prova_service.get_prova_by_id(id)
    if request.method == 'POST':
        prova.set_data(request.form['data'])
        prova.set_peso(request.form['peso'])
        prova.set_materia_id(request.form['materia_id'])
        try:
            prova_service.update_prova(prova)
            return redirect(url_for('list_provas'))
        except ValueError as e:
            return render_template('prova/form.html', error=str(e), prova=prova)
    materias = materia_service.get_all_materias()
    return render_template('prova/form.html', prova=prova, materias=materias)

@app.route('/provas/excluir/<int:id>')
def delete_prova(id):
    prova_service.delete_prova(id)
    return redirect(url_for('list_provas'))

