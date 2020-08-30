def romano_para_inteiro(s: str) -> int:
    s = s.upper()
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if s not in romanos:
        return 0
    resp = 0
    for index, valor in enumerate(s[:len(s) - 1]):
        if romanos[s[index]] >= romanos[s[index + 1]]:
            resp += romanos[valor]
        else:
            resp -= romanos[valor]
    resp += romanos[s[len(s) - 1]]
    return resp
