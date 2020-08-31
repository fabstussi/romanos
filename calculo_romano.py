from romanos_para_inteiros import romano_para_inteiro as rpi
from inteiros_para_romanos import inteiro_para_romano as ipr


class Calculos:

    def __init__(self, calculo: str):
        self._calculo = calculo.upper().replace(' ', '')

    def _desmonta_calculo(self, calculo: str):
        self.calculo = calculo
        self._v1 = ''
        self._v2 = ''
        self._s = '!'
        for i in self.calculo:
            if i not in '+-*/.:':
                self._v2 = (self._v2 + i)
            else:
                self._s = i
                self._v1 = self._v2
                self._v2 = ''
        if self._s == '!':
            self._v1 = '0'
        self._v1 = self._caracter_inteiro(self._v1)
        self._v2 = self._caracter_inteiro(self._v2)
        return self._v1, self._s, self._v2
    
    def fazer_calculo(self):
        self.v1, self.s, self.v2 = self._desmonta_calculo(self._calculo)
        if self.s == '+':
            self._resultado = self.v1 + self.v2
        elif self.s == '-':
            self._resultado = self.v1 - self.v2
        elif self.s in '*.':
            self._resultado = self.v1 * self.v2
        elif self.s in '/:':
            self._resultado = self.v1 / self.v2
        else:
            return 'Erro: não foi localizada operação matemática basica.'
        return self._inteiro(abs(int(self._resultado)))
    
    def _caracter_inteiro(self, v: str) -> int:
        try:
            v = int(v)
        except ValueError:
            v = self._romano(v)
        return v

    @staticmethod
    def _romano(r: str) -> int:
        v = rpi(r)
        return v

    @staticmethod
    def _inteiro(v: int) -> str:
        if v < 3999:
            r = ipr(v)
        else:
            r = 'Erro: o calculo não pode ser maior do que 3999'
        return f'{r} ({v})'
