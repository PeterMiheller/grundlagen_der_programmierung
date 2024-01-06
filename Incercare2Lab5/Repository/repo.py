import pickle
import os
class Kundenrepo:
    def __init__(self,filename):
        self.kunden = []
        self.filename = filename
        # if os.path.exists(self.filename):
        #     self.load()


    def add(self, kunde):
        self.kunden.append(kunde)
        self.save()

    def save(self):
        f= open(self.filename,'ab')
        pickle.dump(self.kunden,f)
        f.close()


    # def load(self):
    #     f = open(self.filename, 'rb')
    #     self.kunden=pickle.load(f)
    #     f.close()
    #     return self.kunden
    def load(self):
        with open(self.filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    self.kunden.append(obj)
                except EOFError:
                    break
        return self.kunden

    def find(self,name):
        for kunde in self.kunden:
            if kunde.name == name:
                return kunde
        return None