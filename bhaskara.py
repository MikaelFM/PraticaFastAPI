from pydantic import BaseModel
import cmath

class Bhaskara(BaseModel):
    a : int
    b : int
    c : int

    def getEquacao(self):
        a = self.a if self.a >= 0 else f"-{abs(self.a)}"
        b = f" + {self.b}" if self.b >= 0 else f" - {abs(self.b)}"
        c = f" + {self.c}" if self.c >= 0 else f" - {abs(self.c)}"
        return f"{a}x²{b}x{c}"
    
    def getResult(self):
        delta = cmath.sqrt(self.b**2 - 4*self.a*self.c)
        x1 = (-self.b + delta) / (2*self.a)
        x2 = (-self.b - delta) / (2*self.a)
        return x1, x2