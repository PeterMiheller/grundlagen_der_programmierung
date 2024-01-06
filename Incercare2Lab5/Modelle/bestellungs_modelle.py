class Kunden:
    def __init__(self,id:int,name:str,adresse:str):
        self.id=id
        self.name=name
        self.adresse=adresse

    def __repr__(self):
        return f'Id:{self.id}, Name:{self.name}, Adresse:{self.adresse}'

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.adresse == other.adresse