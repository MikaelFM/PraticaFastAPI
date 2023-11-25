import re
from typing import Optional
from bhaskara import Bhaskara
from frase import Frase
from app import app

@app.get("/quadrados")
def quadrados(max : Optional[int] = 5):
   if not isinstance(max, int):
      return "O valor de 'max' deve ser um número inteiro."
   if max <= 0:
      return "Por Favor, informe um número 'max' maior que 0."

   quadrados = []
   for i in range(1, max+1):
       quadrados.append(i**2)
  
   return { 
       "max" : max,
       "quadrados" : quadrados
   }


@app.get("/tabuada/{num}")
def tabuada(num : int, start : Optional[int] = 1, end : Optional[int] = 10):
   if not isinstance(num, int):
      return "O valor de 'num' deve ser um número inteiro."
   if not isinstance(start, int):
      return "O valor de 'start' deve ser um número inteiro."
   if not isinstance(end, int):
      return "O valor de 'end' deve ser um número inteiro."
   if start > end:
      return "O número 'start' não pode ser maior que o 'end'"

   tabuada = []
   for i in range(start, end+1):
       tabuada.append(num*i)
  
   return {
       "num" : num,
       "start" : start,
       "end" : end,
       "tabuada" : tabuada
   }

@app.post("/bhaskara")
def bhaskara(equacao : Bhaskara):
   if not isinstance(equacao, Bhaskara):
      return "O valor de 'equacao' deve ter valores válidos"
   if equacao.a == 0:
      return "O coeficiente 'a' não pode ser igual a 0."

   x1, x2 = equacao.getResult()
   return {
       "eq" : equacao.getEquacao(),
       "x1" : x1.real,
       "x2" : x2.real
   }

@app.post("/conta")
def conta(frase : Frase):
   if not isinstance(frase, Frase):
      return "O valor de 'frase' deve ser uma frase válida"

   vogais, consoantes, espacos, outros = frase.count()
   return {
       "frase": frase.frase,
       "vogais": vogais,
       "consoantes": consoantes,
       "espacos": espacos,
       "outros": outros
   }
