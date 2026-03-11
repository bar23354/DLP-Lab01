#visualizacion de la tabla de transiciones y detalles de la construccion

def mostrarTabla(afd):
    estados = afd['estados']
    alfa = afd['alfabeto']
    trans = afd['transiciones']
    acept = afd['estadosAceptacion']
    ini = afd['estadoInicial']

    anchoEst = max(len(e) for e in estados) + 4
    anchoCol = max(max((len(s) for s in alfa), default=3), 6) + 2

    enc = 'Estado'.ljust(anchoEst) + ''.join(s.center(anchoCol) for s in alfa) + '  Tipo'
    sep = '-' * len(enc)

    print('\n' + sep)
    print('  TABLA DE TRANSICIONES DEL AFD')
    print(sep)
    print(enc)
    print(sep)

    for est in estados:
        marca = ('->' if est == ini else '') + ('*' if est in acept else '')
        fila = (marca + est).ljust(anchoEst)
        fila += ''.join(trans.get(est, {}).get(s, '-').center(anchoCol) for s in alfa)
        tipo = ''
        if est == ini and est in acept:
            tipo = 'Inicio/Aceptacion'
        elif est == ini:
            tipo = 'Inicio'
        elif est in acept:
            tipo = 'Aceptacion'
        print(fila + '  ' + tipo)

    print(sep)
    print(f'  Total de estados: {len(estados)}')
    print(f'  Estados de aceptacion: {", ".join(sorted(acept, key=lambda x: int(x[1:])))}')
    print(f'  Alfabeto: {{{", ".join(alfa)}}}')
    print(sep + '\n')


def mostrarDetalle(hojas, afd):
    print('\n--- Detalle del calculo por posicion ---')
    print(f'{"Pos":<6}{"Simbolo":<10}{"SiguientePos"}')
    print('-' * 40)
    for hid in sorted(hojas.keys()):
        h = hojas[hid]
        sig = '{' + ', '.join(str(x) for x in sorted(h.siguientePos)) + '}'
        print(f'{hid:<6}{repr(h.valor):<10}{sig}')
    print()

    print('--- Conjuntos de posiciones por estado ---')
    conj = afd['conjuntos']
    for nom in sorted(conj.keys(), key=lambda x: int(x[1:])):
        pos = '{' + ', '.join(str(x) for x in sorted(conj[nom])) + '}'
        print(f'  {nom}: {pos}')
    print()
