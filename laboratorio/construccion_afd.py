# construccion directa del AFD a partir del arbol sintactico aumentado


def construirAfd(raiz, hojas, alfabeto):
    # buscar el id de la hoja marcador '#' que indica aceptacion
    idMarcador = next(hid for hid, h in hojas.items() if h.valor == '#')
    # el estado inicial es el conjunto congelado de primeraPos de la raiz
    inicial = frozenset(raiz.primeraPos)

    # mapeo conjunto de posiciones -> nombre de estado ('S0', 'S1', ...)
    nombresEstados = {inicial: 'S0'}
    # lista de conjuntos por procesar en el algoritmo de subconjuntos
    porProcesar = [inicial]
    trans = {}  # transiciones: nombreEstado -> {simbolo: nombreEstadoDestino}
    aceptacion = set()  # nombres de estados de aceptacion
    cont = 1  # contador para asignar nuevos nombres de estados

    # si el marcador esta en el conjunto inicial, marcar S0 como aceptacion
    if idMarcador in inicial:
        aceptacion.add('S0')

    # bucle principal: procesar cada conjunto de posiciones
    while porProcesar:
        actual = porProcesar.pop(0)  # obtener primer conjunto por procesar
        nomActual = nombresEstados[actual]  # nombre del estado actual
        trans.setdefault(nomActual, {})  # asegurar entrada en diccionario de trans

        for sym in alfabeto:
            # construir el conjunto de posiciones alcanzables con el simbolo sym
            nuevo = set()
            for pos in actual:
                # si la hoja en esa posicion tiene el simbolo buscado
                if hojas[pos].valor == sym:
                    # agregar sus posiciones siguientes al conjunto nuevo
                    nuevo |= hojas[pos].siguientePos
            if not nuevo:
                # si no hay transicion para este simbolo, continuar
                continue

            # usar frozenset para poder usar el conjunto como clave en el diccionario
            nuevoFs = frozenset(nuevo)
            if nuevoFs not in nombresEstados:
                # crear un nuevo nombre de estado para este conjunto
                nom = 'S' + str(cont)
                nombresEstados[nuevoFs] = nom
                cont += 1
                porProcesar.append(nuevoFs)
                # si el conjunto contiene el marcador, es estado de aceptacion
                if idMarcador in nuevoFs:
                    aceptacion.add(nom)

            # registrar la transicion desde el estado actual con simbolo sym
            trans[nomActual][sym] = nombresEstados[nuevoFs]

    # retornar la estructura del automata: estados, alfabeto, transiciones, etc.
    return {
        'estados': sorted(nombresEstados.values(), key=lambda x: int(x[1:])),
        'alfabeto': alfabeto,
        'transiciones': trans,
        'estadoInicial': 'S0',
        'estadosAceptacion': aceptacion,
        'conjuntos': {v: k for k, v in nombresEstados.items()}
    }
