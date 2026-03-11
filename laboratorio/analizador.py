#tokenizacion, formato y conversion de expresiones regulares a postfijo

operadores = {'|', '.', '*', '+', '?'}
precedencia = {'|': 1, '.': 2, '*': 3, '+': 3, '?': 3}
unarios = {'*', '+', '?'}


def esOperando(c):
    return c not in operadores and c not in ('(', ')')


def necesitaConcat(prev, act):
    if prev is None:
        return False
    return (esOperando(prev) or prev in unarios or prev == ')') and (esOperando(act) or act == '(')


def tokenizar(expr):
    toks = []
    i = 0
    while i < len(expr):
        if expr[i] == '\\' and i + 1 < len(expr):
            toks.append(expr[i + 1])
            i += 2
        else:
            toks.append(expr[i])
            i += 1
    return toks


def insertarConcat(toks):
    salida = []
    for i, t in enumerate(toks):
        salida.append(t)
        if i + 1 < len(toks) and necesitaConcat(t, toks[i + 1]):
            salida.append('.')
    return salida


def aPostfijo(toks):
    salida = []
    pila = []
    for t in toks:
        if t == '(':
            pila.append(t)
        elif t == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            if pila:
                pila.pop()
        elif t in precedencia:
            while pila and pila[-1] != '(' and pila[-1] in precedencia and precedencia[pila[-1]] >= precedencia[t]:
                salida.append(pila.pop())
            pila.append(t)
        else:
            salida.append(t)
    while pila:
        salida.append(pila.pop())
    return salida


def obtenerAlfabeto(toks):
    return sorted({t for t in toks if t not in operadores and t not in ('(', ')', '#')})


def prepararExpresion(expr):
    toks = tokenizar(expr)
    conConcat = insertarConcat(toks)
    postfijo = aPostfijo(conConcat)
    alfa = obtenerAlfabeto(toks)
    return postfijo, alfa, conConcat
