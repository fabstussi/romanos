from calculo_romano import Calculos

print('''Olá, esse é o Calculo romano.
Aqui você consegue fazer calculos das operações fundamentais.
basta digitar a operação desejada completa.
Ex.: V + IV ou XV - IX ou X * II ou CXX / IV''')

resultado = Calculos(input('Digite um calculo com números romanos: '))
print(resultado.fazer_calculo())
