from app.repository.materia_repository import MateriaRepository
from app.models.materia_model import MateriaModel
from app.repository.prova_repository import ProvaRepository

class MateriaService:
    def __init__(self):
        self.materia_repository = MateriaRepository()
        self.prova_repository = ProvaRepository()
        
    def get_all_materias(self):
        return self.materia_repository.get_all_materias()
    
    def get_materia_by_id(self, id):
        return self.materia_repository.get_materia_by_id(id)
    
    def create_materia(self, materia):
        if materia.get_id() is not None:
            raise ValueError("O id da matéria deve ser None para criação.")
        if not materia.get_nome() or not materia.get_professor():
            raise ValueError("Nome e professor são obrigatórios para criação de uma matéria.")
        
        # Validação nome da matéria
        if materia.get_nome().isdigit() or len(materia.get_nome()) < 3:
            raise ValueError("O nome da matéria não pode ser apenas numérico e deve ter pelo menos 3 caracteres.")
        
        # Validação nome do professor
        if materia.get_professor().isdigit() or len(materia.get_professor()) < 3:
            raise ValueError("O nome do professor não pode ser apenas numérico e deve ter pelo menos 3 caracteres.")
        
        self.materia_repository.create_materia(materia)


    def update_materia(self, materia):
        if materia.get_id() is None:
            raise ValueError("O id da matéria não pode ser None para atualização.")
        if not materia.get_nome() or not materia.get_professor():
            raise ValueError("Nome e professor são obrigatórios para atualização de uma matéria.")
        
        # Validação nome da matéria
        if materia.get_nome().isdigit() or len(materia.get_nome()) < 3:
            raise ValueError("O nome da matéria não pode ser apenas numérico e deve ter pelo menos 3 caracteres.")
        
        # Validação nome do professor
        if materia.get_professor().isdigit() or len(materia.get_professor()) < 3:
            raise ValueError("O nome do professor não pode ser apenas numérico e deve ter pelo menos 3 caracteres.")
        
        self.materia_repository.update_materia(materia)

    
    def delete_materia(self, id):
        if id is None:
            raise ValueError("O id da matéria não pode ser None para exclusão.")
        provas = self.prova_repository.get_provas_by_materia_id(id)
        if provas:
            raise ValueError("Não é possível excluir a matéria porque existem provas associadas a ela.")
        self.materia_repository.delete_materia(id)