class MateriaModel:
    def __init__(self, id, nome, professor, descricao):
        self.__id = id
        self.__nome = nome 
        self.__professor = professor
        self.__descricao = descricao
        
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_professor(self):
        return self.__professor
    def get_descricao(self):
        return self.__descricao
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def set_professor(self, professor):
        self.__professor = professor
        
    def set_descricao(self, descricao):
        self.__descricao = descricao
        
    
        
    