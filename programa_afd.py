#programa principal: menu interactivo para conversion directa de regex a AFD

import sys

from laboratorio.analizador import formatearSimbolo, formatearTokens, prepararExpresion
from laboratorio.arbol import construirArbolDirecto
from laboratorio.construccion_afd import construirAfd
from laboratorio.simulador import simularAfd
from laboratorio.tabla import mostrarTabla, mostrarDetalle


def procesarRegex(expresion):
    print(f'\nExpresion regular: {expresion}')
    postfijo, alfa, infijo = prepararExpresion(expresion)
    print(f'Con concatenacion explicita: {" ".join(formatearTokens(infijo))}')
    print(f'Postfijo: {" ".join(formatearTokens(postfijo))}')
    print(f'Alfabeto: {{{", ".join(formatearSimbolo(symbol) for symbol in alfa)}}}')

    raiz, hojas = construirArbolDirecto(postfijo)
    afd = construirAfd(raiz, hojas, alfa)
    mostrarDetalle(hojas, afd)
    mostrarTabla(afd)
    return afd


def validarCadena(afd):
    cadena = input('Ingrese la cadena a validar: ')
    resultado, recorrido = simularAfd(afd, cadena)
    print(f'  Cadena: "{cadena}"')
    print(f'  Recorrido: {" -> ".join(recorrido)}')
    print(f'  Resultado: {"ACEPTADA" if resultado else "RECHAZADA"}')
    return resultado


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')

    print('=' * 55)
    print('  Conversion Directa de Expresion Regular a AFD')
    print('=' * 55)
    print('Operadores: | (union)  * (Kleene)  + (positiva)  ? (opcional)  () (agrupacion)  \\ (escape)')

    while True:
        print('\n' + '-' * 55)
        opcion = input('[1] Nueva expresion  [2] Salir : ').strip()

        if opcion == '1':
            expresion = input('Expresion regular: ').strip()
            if not expresion:
                print('Error: expresion vacia.')
                continue
            try:
                afd = procesarRegex(expresion)
            except Exception as e:
                print(f'Error: {e}')
                continue

            while True:
                sub = input('\n  [a] Validar cadena  [b] Ver tabla  [c] Volver : ').strip().lower()
                if sub == 'a':
                    validarCadena(afd)
                elif sub == 'b':
                    mostrarTabla(afd)
                elif sub == 'c':
                    break

        elif opcion == '2':
            print('Finalizado.')
            break


if __name__ == '__main__':
    main()
