from app.database.connetion import get_db
from app.models.materia_model import MateriaModel

class MateriaRepository:
    
    def get_all_materias(self):
        connetion = get_db()
        cursor = connetion.cursor()
        cursor.execute('SELECT * FROM materia')
        materias = cursor.fetchall()
        return [MateriaModel(*materia) for materia in materias]
    
    def get_materia_by_id(self, id):
        connetion = get_db()
        cursor = connetion.cursor()
        cursor.execute('SELECT * FROM materia WHERE id = ?', (id,))
        materia = cursor.fetchone()
        if materia:
            return MateriaModel(*materia)
        return None
    
    def create_materia(self, materia):
        connetion = get_db()
        cursor = connetion.cursor()
        cursor.execute('INSERT INTO materia (nome, professor, descricao) VALUES (?, ?, ?)', 
                       (materia.get_nome(), materia.get_professor(), materia.get_descricao()))
        connetion.commit()
        
    def update_materia(self, materia):
        connetion = get_db()
        cursor = connetion.cursor()
        cursor.execute('UPDATE materia SET nome = ?, professor = ?, descricao = ? WHERE id = ?', 
                       (materia.get_nome(), materia.get_professor(), materia.get_descricao(), materia.get_id()))
        connetion.commit()
        
    def delete_materia(self, id):
        connetion = get_db()
        cursor = connetion.cursor()
        cursor.execute('DELETE FROM materia WHERE id = ?', (id,))
        connetion.commit()