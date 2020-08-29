from romanos_para_inteiros import romano_para_inteiro as rpi
from inteiros_para_romanos import inteiro_para_romano as ipr

class Calculos:

    def __init__(self, calculo: str):
        self._calculo = calculo.upper().replace(' ', '')

    def _desmonta_calculo(self, calculo: str):
        self.calculo = calculo
        self._v1 = ''
        self._v2 = ''
        self._s = ''
        for i in self.calculo:
            if not i in '+-*/':
                self._v2 = (self._v2 + i)
            else:
                self._s = i
                self._v1 = self._caracter_inteiro(self._v2)
                self._v2 = ''
        self._v2 = self._caracter_inteiro(self._v2)
        return self._v1, self._s, self._v2
    
    def fazer_calculo(self):
        self.v1, self.s, self.v2 = self._desmonta_calculo(self._calculo)
        if self.s == '+':
            self._resultado = self.v1 + self.v2
            return self._inteiro(self._resultado)
        elif self.s == '-':
            self._resultado = self.v1 + self.v2
            return self._inteiro(self._resultado)
        elif self.s == '*':
            self._resultado = self.v1 + self.v2
            return self._inteiro(self._resultado)
        elif self.s == '/':
            self._resultado = self.v1 + self.v2
            return self._inteiro(self._resultado)
        else:
            return f'Erro: {self.s} não pertence as 4 operações fundamentais '
    
    def _caracter_inteiro(self, v: str) -> int:
        print(v.isnumeric)
        if v.isnumeric:
            v = int(v)
        else:
            v = self.romano(v)
        return v

    def _romano(r: str) -> int:
        v = rpi(r.upper())
        return v
    
    def _inteiro(v: int) -> str:
        r = ipr(v)
        return r