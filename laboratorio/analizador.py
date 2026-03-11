# tokenizacion, formato y conversion de expresiones regulares a postfijo

# operadores: simbolos usados para operaciones en la regexp
operadores = {'|', '.', '*', '+', '?'}
# precedencia: prioridad de operadores para la conversion a postfijo
precedencia = {'|': 1, '.': 2, '*': 3, '+': 3, '?': 3}
# unarios: operadores que actuan sobre un solo operando
unarios = {'*', '+', '?'}


def esOperando(c):
    # devuelve True si el caracter es un operando (no un operador ni parentesis)
    return c not in operadores and c not in ('(', ')')


def necesitaConcat(prev, act):
    # determina si entre prev y act debe insertarse un operador de concatenacion
    if prev is None:
        # sin previo no se concatena
        return False
    # concatena cuando el anterior puede terminar un termino y el actual puede empezar uno
    return (esOperando(prev) or prev in unarios or prev == ')') and (esOperando(act) or act == '(')


def tokenizar(expr):
    # transforma la cadena de expresion en una lista de tokens
    toks = []
    i = 0
    # iteracion manual para respetar escapes (\)
    while i < len(expr):
        if expr[i] == '\\' and i + 1 < len(expr):
            # si hay un escape, tomar el siguiente caracter como literal
            toks.append(expr[i + 1])
            i += 2
        else:
            # cualquier otro caracter se añade tal cual
            toks.append(expr[i])
            i += 1
    return toks


def insertarConcat(toks):
    # inserta el operador explicito '.' donde sea necesario para concatenacion
    salida = []
    for i, t in enumerate(toks):
        salida.append(t)  # añadir token actual
        # si el siguiente token existe y se debe concatenar, insertar '.'
        if i + 1 < len(toks) and necesitaConcat(t, toks[i + 1]):
            salida.append('.')
    return salida


def aPostfijo(toks):
    # convierte la lista de tokens (con concatenaciones explicitas) a notacion postfija
    salida = []
    pila = []
    for t in toks:
        if t == '(':
            # abrir parentesis: empujar en pila
            pila.append(t)
        elif t == ')':
            # cerrar parentesis: vaciar la pila hasta el '(' correspondiente
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            if pila:
                pila.pop()  # eliminar el '(' de la pila
        elif t in precedencia:
            # si es un operador: aplicar reglas de precedencia usando la pila
            while pila and pila[-1] != '(' and pila[-1] in precedencia and precedencia[pila[-1]] >= precedencia[t]:
                salida.append(pila.pop())
            pila.append(t)
        else:
            # operando: añadir directamente a la salida
            salida.append(t)
    # vaciar lo que quede en pila
    while pila:
        salida.append(pila.pop())
    return salida


def obtenerAlfabeto(toks):
    # devuelve el alfabeto de simbolos (ordenado) excluyendo operadores, parentesis y marcador '#'
    return sorted({t for t in toks if t not in operadores and t not in ('(', ')', '#')})


def prepararExpresion(expr):
    # prepara la expresion: tokeniza, inserta concat, convierte a postfijo y obtiene el alfabeto
    toks = tokenizar(expr)
    conConcat = insertarConcat(toks)
    postfijo = aPostfijo(conConcat)
    alfa = obtenerAlfabeto(toks)
    return postfijo, alfa, conConcat
