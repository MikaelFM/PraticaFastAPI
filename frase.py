from pydantic import BaseModel
from collections import Counter
import re

class Frase(BaseModel):
    frase : str

    def contar(self, tupleOfCount):
        string = self.frase.lower()
        count = 0
        for i in tupleOfCount: 
            if i in string: 
                count += string.count(i) 
        return count 
    
    def count(self):
        vogais = self.contar('aeiouáéíóúãõâêîôûàèìòùäëïöü')
        consoantes = self.contar('bcçdfghjklmnpqrstvwxyz')
        espacos = self.contar(' ')
        outros = (len(self.frase)) - vogais - consoantes - espacos
        return vogais, consoantes, espacos, outros
