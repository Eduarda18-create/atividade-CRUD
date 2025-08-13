from app.database.connetion import get_db
from app.models.prova_model import ProvaModel

class ProvaRepository:
    
    def get_all_provas(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" SELECT p.id, p.data, p.peso, p.materia_id, m.nome
                         FROM prova p
                        JOIN materia m ON p.materia_id = m.id """)
        rows = cursor.fetchall()
        provas = []
        for row in rows:
            prova = ProvaModel(id=row[0], data=row[1], peso=row[2], materia_id=row[3])
            prova.materia_nome = row[4]
            provas.append(prova)
        return provas
    
    def get_prova_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" SELECT p.id, p.data, p.peso, p.materia_id, m.nome
                         FROM prova p
                        JOIN materia m ON p.materia_id = m.id
                        WHERE p.id = ? """, (id,))
        row = cursor.fetchone()
        if row:
            prova = ProvaModel(id=row[0], data=row[1], peso=row[2], materia_id=row[3])
            prova.materia_nome = row[4]
            return prova
        return None
    
    def create_prova(self, prova):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO prova (data, peso, materia_id) VALUES (?, ?, ?)', 
                       (prova.get_data(), prova.get_peso(), prova.get_materia_id()))
        connection.commit()
        
    def update_prova(self, prova):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute('UPDATE prova SET data = ?, peso = ?, materia_id = ? WHERE id = ?', 
                       (prova.get_data(), prova.get_peso(), prova.get_materia_id(), prova.get_id()))
        connection.commit()
        
    def delete_prova(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM prova WHERE id = ?', (id,))
        connection.commit()
        
    def get_provas_by_materia_id(self, materia_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" SELECT p.id, p.data, p.peso, p.materia_id, m.nome
                         FROM prova p
                        JOIN materia m ON p.materia_id = m.id
                        WHERE p.materia_id = ? """, (materia_id,))
        rows = cursor.fetchall()
        provas = []
        for row in rows:
            prova = ProvaModel(id=row[0], data=row[1], peso=row[2], materia_id=row[3])
            prova.materia_nome = row[4]
            provas.append(prova)
        return provas