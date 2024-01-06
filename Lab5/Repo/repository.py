import pickle
from abc import ABC
from Modelle.bestellungs_modelle import *


class DataRepo(ABC):
    def __init__(self, filename):
        self.filename = filename
        self.list = []

    def save(self):
        f = open(self.filename, 'ab')
        pickle.dump(self.list, f)
        f.close()

    def load(self):
        f = open(self.filename, 'rb')
        self.list = pickle.load(f)
        f.close()
        return self.list

    def read(self, filename):
        f = open(self.filename, 'r')
        for line in f:
            for el in line.strip().split():
                print(el)
        f.close()

    def write(self, string):
        f = open(self.filename, 'w')
        f.write(string)
        f.close()

    def convert_to_string(self, list):
        result = map(lambda x: str(x), list)
        joined_elements = ','.join(result)
        f = open(self.filename, 'w')
        f.write(joined_elements)
        f.close()

    # def convert_from_string(self):
    #     objects_list = []
    #     with open(filename, 'r') as file:
    #         lines = file.readlines()
    #         for line in lines:
    #             obj = Gericht(line.strip())
    #             objects_list.append(obj)
    #
    #     return objects_list


class CookedDishRepo:
    def __init__(self):
        self.filename = 'speisekarte.data'
        self.gericht = []

    def add(self, neues_gericht):
        self.gericht.append(neues_gericht)
        self.save()

    def save(self):
        f = open(self.filename, 'ab')
        pickle.dump(self.gericht, f)
        f.close()



    def load(self):
        with open(self.filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    self.gericht.append(obj)
                except EOFError:
                    break
        return self.gericht

    def find_dish(self, selected_dish):
        gerichte = self.load()
        for dishes in gerichte:
            found_dish = list(filter(lambda d: selected_dish.lower() in d.name.lower(), dishes))
            if found_dish:
                return found_dish


class DrinkRepo:
    def __init__(self):
        self.filename = 'speisekarte.data'
        self.getränk = []

    def add(self, neues_getränk):
        self.getränk.append(neues_getränk)
        self.save()

    def save(self):
        f = open(self.filename, 'ab')
        pickle.dump(self.getränk, f)
        f.close()


    def load(self):
        with open(self.filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    self.getränk.append(obj)
                except EOFError:
                    break
        return self.getränk

    def find_drink(self, selected_drink):
        getränke = self.load()
        for drinks in getränke:
            found_drink = list(filter(lambda d: selected_drink.lower() in d.name.lower(),drinks))
            if found_drink:
                return found_drink


class CustomerRepo:
    def __init__(self):
        self.filename = 'kunden.data'
        self.kunden = []


    def add(self, neue_kunde):
        self.kunden.append(neue_kunde)
        self.save()

    def load(self):
        with open(self.filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    self.kunden.append(obj)
                except EOFError:
                    break
        return self.kunden

    def save(self):
        f = open(self.filename, 'ab')
        pickle.dump(self.kunden, f)
        f.close()

    def delete(self, nume_de_sters):
        kunden = []
        with open(self.filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    kunden.append(obj)
                except EOFError:
                    break

        for customer in kunden:
            for k in customer:
                if k == nume_de_sters:
                    kunden.remove(k)
        f = open(self.filename, 'wb')
        for k in kunden:
            pickle.dump(k, f)
        f.close()

    def aktualisieren(self, nume_actualizat, new_id, new_adress, kunde_actualizat):
        k=[]
        with open(self.filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    k.append(obj)
                except EOFError:
                    break
        if kunde_actualizat in k:
            new_kunde = [Kunde(new_id, nume_actualizat, new_adress)]
            index = k.index(kunde_actualizat)
            k[index] = new_kunde
        f = open(self.filename, 'wb')
        for i in k:
            pickle.dump(i, f)
        f.close()
    def find_customer(self, search_string):
        kunden = self.load()
        for customers in kunden:
            found_customers = list(filter(lambda customer: search_string.lower() in customer.name.lower()
                                                           or search_string.lower() in customer.adresse.lower(),
                                          customers))
            if found_customers:
                return found_customers


class OrderRepo(DataRepo):
    def __init__(self, filename):
        DataRepo.__init__(self, filename)
        self.filename = 'orders.data'
        self.orders = []

    def add(self, neue_speise):
        self.orders.append(neue_speise)
        f = open(self.filename, 'ab')
        pickle.dump(self.orders, f)
        f.close()

    def calculate_total_cost(self,gericht, getränk):
        return gericht.preis+getränk.preis

    def generate_bill(self,gericht, getränk, kunde):

        rechnung = f'\n===== Rechnung =====\nKunde: {kunde.name}\nAdresse: {kunde.adresse}\nBestellte Gerichte: \n'
        rechnung += f"{gericht.name}: {gericht.portionsgröße} Gramm - {gericht.preis} Euro\n"
        rechnung += f"\nBestellte Getränke:\n"
        rechnung += f"{getränk.name}: {getränk.portionsgröße} Liter - {getränk.preis} Euro\n"
        rechnung += f'\nGesamtkosten:{self.calculate_total_cost(gericht, getränk)} Euro\n'
        rechnung+= f"===================="
        return rechnung
