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
