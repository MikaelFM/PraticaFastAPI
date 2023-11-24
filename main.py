from fastapi import FastAPI
from typing import Optional

app = FastAPI()


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