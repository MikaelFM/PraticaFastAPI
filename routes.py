from typing import Optional
from bhaskara import Bhaskara
from app import app

@app.get("/quadrados")
def quadrados(max : Optional[int] = 5):
   quadrados = []
   for i in range(1, max+1):
       quadrados.append(i**2)
  
   return {
       "max" : max,
       "quadrados" : quadrados
   }

@app.get("/tabuada/{num}")
def tabuada(num : int, start : Optional[int] = 1, end : Optional[int] = 10):
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
   x1, x2 = equacao.getResult()
   print(x1)
   return {
       "eq" : equacao.getEquacao(),
       "x1" : x1.real,
       "x2" : x2.real
   }