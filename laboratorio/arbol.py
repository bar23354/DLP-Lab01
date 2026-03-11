#construccion del arbol sintactico y calculo de anulable, primeraPos, ultimaPos, siguientePos

_contadorHojas = 0


class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der
        self.idHoja = None
        self.anulable = False
        self.primeraPos = set()
        self.ultimaPos = set()
        self.siguientePos = set()


def _nuevoId():
    global _contadorHojas
    _contadorHojas += 1
    return _contadorHojas


def _crearNodoUnario(sym, hijo):
    n = Nodo(sym, hijo)
    n.anulable = True if sym in ('*', '?') else hijo.anulable
    n.primeraPos = hijo.primeraPos.copy()
    n.ultimaPos = hijo.ultimaPos.copy()
    return n


def construirArbol(postfijo):
    global _contadorHojas
    _contadorHojas = 0
    pila = []
    hojas = {}

    for sym in postfijo:
        if sym == '|':
            der, izq = pila.pop(), pila.pop()
            n = Nodo('|', izq, der)
            n.anulable = izq.anulable or der.anulable
            n.primeraPos = izq.primeraPos | der.primeraPos
            n.ultimaPos = izq.ultimaPos | der.ultimaPos
            pila.append(n)
        elif sym == '.':
            der, izq = pila.pop(), pila.pop()
            n = Nodo('.', izq, der)
            n.anulable = izq.anulable and der.anulable
            n.primeraPos = (izq.primeraPos | der.primeraPos) if izq.anulable else izq.primeraPos.copy()
            n.ultimaPos = (izq.ultimaPos | der.ultimaPos) if der.anulable else der.ultimaPos.copy()
            pila.append(n)
        elif sym in ('*', '+', '?'):
            pila.append(_crearNodoUnario(sym, pila.pop()))
        else:
            n = Nodo(sym)
            n.idHoja = _nuevoId()
            n.primeraPos = {n.idHoja}
            n.ultimaPos = {n.idHoja}
            hojas[n.idHoja] = n
            pila.append(n)

    return (pila.pop() if pila else None), hojas


def _calcSiguientePos(nodo, hojas):
    if nodo is None:
        return
    _calcSiguientePos(nodo.izq, hojas)
    _calcSiguientePos(nodo.der, hojas)

    if nodo.valor == '.':
        for p in nodo.izq.ultimaPos:
            hojas[p].siguientePos |= nodo.der.primeraPos
    elif nodo.valor in ('*', '+'):
        for p in nodo.ultimaPos:
            hojas[p].siguientePos |= nodo.primeraPos


def construirArbolDirecto(postfijo):
    raiz, hojas = construirArbol(postfijo + ['#', '.'])
    _calcSiguientePos(raiz, hojas)
    return raiz, hojas
