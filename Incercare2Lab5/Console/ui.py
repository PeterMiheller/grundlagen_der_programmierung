from Controller.logik import *
from Modelle.bestellungs_modelle import Kunden
class Console:
    def __init__(self,controller:Controller):
        self.controller=controller

    def menu(self):
        return """
        1- Add Kunde
        2- Print Kunde
        4- Exit   
        """
    def run(self):
        while True:
            print(self.menu())
            opt= int(input('Opt='))
            if opt==1:
                id = int(input('Id='))
                name=input('Name=')
                adresse=input('Adresse=')
                self.controller.repo.add(Kunden( id,name, adresse))
            if opt==2:
                kunden=self.controller.repo.load()
                print(kunden)
                print('')
                for line in kunden:
                    for el in line:
                        print(el)



            if opt==4:
                break

