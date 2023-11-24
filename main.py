from fastapi import FastAPI

app = FastAPI()


@app.get("/quadrados")
def quadrados(max : int):
   quadrados = []
   for i in range(1, max+1):
       quadrados.append(i**2)
  
   return {
       "max" : max,
       "quadrados" : quadrados
   }
