from calculo_romano import Calculos

print('''Olá, esse é o Calculo romano.
Aqui você consegue fazer calculos das operações fundamentais.
Basta digitar a operação desejada completa.
Ex.: V + IV ou XV - IX ou X * II ou CXX / IV

Pode digitar em números naturais.
Ex.: 232 + 56

Ou ainda misturado
Ex.: MCMLXXIX + 41

Pode nem é preciso dar espaço entre os valores e o sinal
Ex.: XXXIV*V

Por fim pode substituir o asterisco "*" por ponto "." e a barra "/" por dois pontos ":" 
''')

resultado = Calculos(input('Digite um calculo com números romanos: '))
print(resultado.fazer_calculo())
