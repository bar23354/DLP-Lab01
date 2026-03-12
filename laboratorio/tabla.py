# visualizacion de la tabla de transiciones y detalles de la construccion

from laboratorio.analizador import formatearSimbolo, formatearToken


def mostrarTabla(afd):
    estados = afd['estados']
    alfa = afd['alfabeto']
    trans = afd['transiciones']
    acept = afd['estadosAceptacion']
    ini = afd['estadoInicial']

    alfa_formateado = [formatearSimbolo(symbol) for symbol in alfa]
    anchoEst = max(len(estado) for estado in estados) + 4
    anchoCol = max(max((len(symbol) for symbol in alfa_formateado), default=3), 6) + 2

    enc = 'Estado'.ljust(anchoEst) + ''.join(symbol.center(anchoCol) for symbol in alfa_formateado) + '  Tipo'
    sep = '-' * len(enc)

    print('\n' + sep)
    print('  TABLA DE TRANSICIONES DEL AFD')
    print(sep)
    print(enc)
    print(sep)

    for estado in estados:
        marca = ('->' if estado == ini else '') + ('*' if estado in acept else '')
        fila = (marca + estado).ljust(anchoEst)
        for symbol in alfa:
            fila += trans.get(estado, {}).get(symbol, '-').center(anchoCol)

        if estado == ini and estado in acept:
            tipo = 'Inicio/Aceptacion'
        elif estado == ini:
            tipo = 'Inicio'
        elif estado in acept:
            tipo = 'Aceptacion'
        else:
            tipo = ''
        print(fila + '  ' + tipo)

    print(sep)
    print(f'  Total de estados: {len(estados)}')
    print(f'  Estados de aceptacion: {", ".join(sorted(acept, key=lambda estado: int(estado[1:])))}')
    print(f'  Alfabeto: {{{", ".join(alfa_formateado)}}}')
    print(sep + '\n')


def mostrarDetalle(hojas, afd):
    print('\n--- Detalle del calculo por posicion ---')
    print(f'{"Pos":<6}{"Simbolo":<10}{"SiguientePos"}')
    print('-' * 40)
    for hid in sorted(hojas.keys()):
        hoja = hojas[hid]
        siguiente = '{' + ', '.join(str(x) for x in sorted(hoja.siguientePos)) + '}'
        print(f'{hid:<6}{formatearToken(hoja.valor):<10}{siguiente}')
    print()

    print('--- Conjuntos de posiciones por estado ---')
    for nombre in sorted(afd['conjuntos'].keys(), key=lambda estado: int(estado[1:])):
        posiciones = '{' + ', '.join(str(x) for x in sorted(afd['conjuntos'][nombre])) + '}'
        print(f'  {nombre}: {posiciones}')
    print()
