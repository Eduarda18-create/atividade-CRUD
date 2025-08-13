from app.models.prova_model import ProvaModel
from app.repository.prova_repository import ProvaRepository

class ProvaService:
    def __init__(self):
        self.prova_repository = ProvaRepository()
        
    def get_all_provas(self):
        return self.prova_repository.get_all_provas()
    
    def get_prova_by_id(self, id):
        return self.prova_repository.get_prova_by_id(id)
    
    def create_prova(self, prova):
        if prova.get_id() is not None:
            raise ValueError("O id da prova deve ser None para criação.")
        if not prova.get_data() or not prova.get_peso() or not prova.get_materia_id():
            raise ValueError("Data, peso e matéria são obrigatórios para criação de uma prova.")
        self.prova_repository.create_prova(prova)
        
    def update_prova(self, prova):
        if prova.get_id() is None:
            raise ValueError("O id da prova não pode ser None para atualização.")
        if not prova.get_data() or not prova.get_peso() or not prova.get_materia_id():
            raise ValueError("Data, peso e matéria são obrigatórios para atualização de uma prova.")
        self.prova_repository.update_prova(prova)
        
    def delete_prova(self, id):
        if id is None:
            raise ValueError("O id da prova não pode ser None para exclusão.")
        self.prova_repository.delete_prova(id)