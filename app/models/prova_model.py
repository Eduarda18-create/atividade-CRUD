class ProvaModel:
    def __init__(self, id, data, peso, materia_id):
        self.__id = id
        self.__data = data
        self.__peso = peso
        self.__materia_id = materia_id
        
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_peso(self):
        return self.__peso
    
    def get_materia_id(self):
        return self.__materia_id

    def set_data(self, data):
        self.__data = data
        
    def set_peso(self, peso):
        self.__peso = peso
    
    def set_materia_id(self, materia_id):
        self.__materia_id = materia_id
    
    
    
    