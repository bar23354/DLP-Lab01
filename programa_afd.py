#programa principal: menu interactivo para conversion directa de regex a AFD

import sys

from laboratorio.analizador import formatearSimbolo, formatearTokens, prepararExpresion
from laboratorio.arbol import construirArbolDirecto
from laboratorio.construccion_afd import construirAfd
from laboratorio.minimizacion import minimizarAfd
from laboratorio.simulador import simularAfd
from laboratorio.tabla import mostrarComparacion, mostrarDetalle, mostrarDetalleMinimizacion, mostrarTabla


def procesarRegex(expresion):
    print(f'\nExpresion regular: {expresion}')
    postfijo, alfa, infijo = prepararExpresion(expresion)
    print(f'Con concatenacion explicita: {" ".join(formatearTokens(infijo))}')
    print(f'Postfijo: {" ".join(formatearTokens(postfijo))}')
    print(f'Alfabeto: {{{", ".join(formatearSimbolo(symbol) for symbol in alfa)}}}')

    raiz, hojas = construirArbolDirecto(postfijo)
    afd_directo = construirAfd(raiz, hojas, alfa)
    afd_minimizado = minimizarAfd(afd_directo)
    mostrarDetalle(hojas, afd_directo, titulo='AFD directo')
    mostrarTabla(afd_directo, titulo='AFD DIRECTO')
    mostrarDetalleMinimizacion(afd_minimizado)
    mostrarTabla(afd_minimizado, titulo='AFD MINIMIZADO')
    mostrarComparacion(afd_directo, afd_minimizado)
    return afd_directo, afd_minimizado


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
                afd_directo, afd_minimizado = procesarRegex(expresion)
            except Exception as e:
                print(f'Error: {e}')
                continue

            while True:
                sub = input(
                    '\n  [a] Validar con AFD minimizado  [b] Ver tabla directa  '
                    '[c] Ver tabla minimizada  [d] Ver comparacion  [e] Volver : '
                ).strip().lower()
                if sub == 'a':
                    validarCadena(afd_minimizado)
                elif sub == 'b':
                    mostrarTabla(afd_directo, titulo='AFD DIRECTO')
                elif sub == 'c':
                    mostrarTabla(afd_minimizado, titulo='AFD MINIMIZADO')
                elif sub == 'd':
                    mostrarComparacion(afd_directo, afd_minimizado)
                elif sub == 'e':
                    break

        elif opcion == '2':
            print('Finalizado.')
            break


if __name__ == '__main__':
    main()
