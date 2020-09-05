from romanos_para_inteiros import romano_para_inteiro as rpi
from inteiros_para_romanos import inteiro_para_romano as ipr


class Calculos:

    def __init__(self, calculo: str):
        self._calculo = calculo.upper().replace(' ', '')

    def _desmonta_calculo(self, calculo: str):
        calculo = calculo
        v1 = ''
        v2 = ''
        s = '!'
        for i in calculo:
            if i not in '+-*/.:':
                v2 = (v2 + i)
            else:
                s = i
                v1 = v2
                v2 = ''
        if s == '!':
            v1 = '0'
        v1 = self._caracter_inteiro(v1)
        v2 = self._caracter_inteiro(v2)
        return v1, s, v2
    
    def fazer_calculo(self):
        v1, s, v2 = self._desmonta_calculo(self._calculo)
        if s == '+':
            resultado = v1 + v2
        elif s == '-':
            resultado = v1 - v2
        elif s in '*.':
            resultado = v1 * v2
        elif s in '/:':
            resultado = v1 / v2
        else:
            return 'Erro: não foi localizada operação matemática basica.'
        return self._inteiro(abs(int(resultado)))
    
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
