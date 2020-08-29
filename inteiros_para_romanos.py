def inteiro_para_romano(i: int) -> str:
    if 0 > i > 3999:
        return 'Erro: valor máximo é 3999'
    romanos = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    resp = ''
    resto = valor_a_verificar = 0
    while i > 0:
        parametro_para_resto = 10**(len(str(i)) - 1)
        resto = abs(i % parametro_para_resto)
        valor_a_verificar = i - resto
        if valor_a_verificar == parametro_para_resto:
            resp = (resp + romanos[parametro_para_resto])
        while valor_a_verificar > parametro_para_resto:
            if valor_a_verificar == parametro_para_resto * 9 or valor_a_verificar == parametro_para_resto * 5 or valor_a_verificar == parametro_para_resto * 4:
                resp = (resp + romanos[valor_a_verificar])
                valor_a_verificar = parametro_para_resto
            elif valor_a_verificar > parametro_para_resto * 5:
                resp = (resp + romanos[parametro_para_resto * 5])
                valor_a_verificar -= parametro_para_resto * 5
                if valor_a_verificar == parametro_para_resto:
                    resp = (resp + romanos[parametro_para_resto])
            else:
                resp = (resp + romanos[parametro_para_resto])
                valor_a_verificar -= parametro_para_resto
                if valor_a_verificar == parametro_para_resto:
                    resp = (resp + romanos[parametro_para_resto])
        i = resto
    return resp
