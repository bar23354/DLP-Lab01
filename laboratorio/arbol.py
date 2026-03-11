# construccion del arbol sintactico y calculo de anulable, primeraPos, ultimaPos, siguientePos

# contador global para asignar ids a las hojas
_contadorHojas = 0


class Nodo:
    def __init__(self, valor, izq=None, der=None):
        # valor: simbolo del nodo ('|', '.', '*', '+', '?', o simbolo de hoja)
        self.valor = valor
        # hijos izquierdo y derecho (None si no aplica)
        self.izq = izq
        self.der = der
        # idHoja: numero unico para las hojas (None si no es hoja)
        self.idHoja = None
        # anulable: True si el subarbol puede generar la cadena vacia
        self.anulable = False
        # primeraPos / ultimaPos: conjuntos de posiciones (ids) de primeras/ultimas hojas
        self.primeraPos = set()
        self.ultimaPos = set()
        # siguientePos se calculara posteriormente para cada hoja
        self.siguientePos = set()


def _nuevoId():
    # genera un nuevo id para una hoja incrementando el contador global
    global _contadorHojas
    _contadorHojas += 1
    return _contadorHojas


def _crearNodoUnario(sym, hijo):
    # crea un nodo unario (por ejemplo '*', '+', '?') y copia propiedades del hijo
    n = Nodo(sym, hijo)
    # '*' y '?' siempre permiten la cadena vacia; '+' depende del hijo
    n.anulable = True if sym in ('*', '?') else hijo.anulable
    # primeras y ultimas posiciones se copian del unico hijo
    n.primeraPos = hijo.primeraPos.copy()
    n.ultimaPos = hijo.ultimaPos.copy()
    return n


def construirArbol(postfijo):
    # construye el arbol sintactico a partir de una lista en notacion postfija
    global _contadorHojas
    _contadorHojas = 0  # reiniciar contador antes de construir
    pila = []
    hojas = {}  # mapa idHoja -> nodo

    for sym in postfijo:
        if sym == '|':
            # operador alternacion: pop dos operandos (derecha, izquierda)
            der, izq = pila.pop(), pila.pop()
            n = Nodo('|', izq, der)
            # anulable si cualquiera de los lados es anulable
            n.anulable = izq.anulable or der.anulable
            # primera/ultima son union de ambos lados
            n.primeraPos = izq.primeraPos | der.primeraPos
            n.ultimaPos = izq.ultimaPos | der.ultimaPos
            pila.append(n)
        elif sym == '.':
            # concatenacion: pop derecha e izquierda
            der, izq = pila.pop(), pila.pop()
            n = Nodo('.', izq, der)
            # anulable si ambos lados son anulables
            n.anulable = izq.anulable and der.anulable
            # si el izquierdo es anulable, primeras incluyen las del derecho
            n.primeraPos = (izq.primeraPos | der.primeraPos) if izq.anulable else izq.primeraPos.copy()
            # si el derecho es anulable, ultimas incluyen las del izquierdo
            n.ultimaPos = (izq.ultimaPos | der.ultimaPos) if der.anulable else der.ultimaPos.copy()
            pila.append(n)
        elif sym in ('*', '+', '?'):
            # operadores unarios: aplicar sobre el ultimo elemento en la pila
            pila.append(_crearNodoUnario(sym, pila.pop()))
        else:
            # simbolo terminal (hoja): crear nodo hoja y asignar id
            n = Nodo(sym)
            n.idHoja = _nuevoId()
            n.primeraPos = {n.idHoja}
            n.ultimaPos = {n.idHoja}
            hojas[n.idHoja] = n
            pila.append(n)

    # devolver la raiz (ultimo elemento en pila) y el diccionario de hojas
    return (pila.pop() if pila else None), hojas


def _calcSiguientePos(nodo, hojas):
    # calcula recursivamente la siguientePos para las hojas usando las reglas del algoritmo
    if nodo is None:
        return
    # recorrer subarboles para asegurar que las pos del hijo esten calculadas
    _calcSiguientePos(nodo.izq, hojas)
    _calcSiguientePos(nodo.der, hojas)

    if nodo.valor == '.':
        # para concatenacion: cada posicion en la ultimaPos del izquierdo
        # tiene como siguientePos todas las posiciones en la primeraPos del derecho
        for p in nodo.izq.ultimaPos:
            hojas[p].siguientePos |= nodo.der.primeraPos
    elif nodo.valor in ('*', '+'):
        # para cierre o mas veces: cada posicion en la ultimaPos del nodo
        # tiene como siguientePos todas las posiciones en la primeraPos del mismo nodo
        for p in nodo.ultimaPos:
            hojas[p].siguientePos |= nodo.primeraPos


def construirArbolDirecto(postfijo):
    # construye el arbol aumentado (añade '#', '.') y calcula siguientePos
    raiz, hojas = construirArbol(postfijo + ['#', '.'])
    _calcSiguientePos(raiz, hojas)
    return raiz, hojas
