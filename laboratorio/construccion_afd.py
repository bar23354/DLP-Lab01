#construccion directa del AFD a partir del arbol sintactico aumentado

def construirAfd(raiz, hojas, alfabeto):
    idMarcador = next(hid for hid, h in hojas.items() if h.valor == '#')
    inicial = frozenset(raiz.primeraPos)

    nombresEstados = {inicial: 'S0'}
    porProcesar = [inicial]
    trans = {}
    aceptacion = set()
    cont = 1

    if idMarcador in inicial:
        aceptacion.add('S0')

    while porProcesar:
        actual = porProcesar.pop(0)
        nomActual = nombresEstados[actual]
        trans.setdefault(nomActual, {})

        for sym in alfabeto:
            nuevo = set()
            for pos in actual:
                if hojas[pos].valor == sym:
                    nuevo |= hojas[pos].siguientePos
            if not nuevo:
                continue

            nuevoFs = frozenset(nuevo)
            if nuevoFs not in nombresEstados:
                nom = 'S' + str(cont)
                nombresEstados[nuevoFs] = nom
                cont += 1
                porProcesar.append(nuevoFs)
                if idMarcador in nuevoFs:
                    aceptacion.add(nom)

            trans[nomActual][sym] = nombresEstados[nuevoFs]

    return {
        'estados': sorted(nombresEstados.values(), key=lambda x: int(x[1:])),
        'alfabeto': alfabeto,
        'transiciones': trans,
        'estadoInicial': 'S0',
        'estadosAceptacion': aceptacion,
        'conjuntos': {v: k for k, v in nombresEstados.items()}
    }
