# Expresiones para video - Lab 2

Este archivo deja un guion corto para la grabacion de la demostracion.

## Objetivo del video

Para cada expresion:

1. ingresar la expresion regular
2. mostrar la tabla del AFD directo
3. mostrar la tabla del AFD minimizado
4. comparar estados y transiciones
5. validar una cadena aceptada con el AFD minimizado
6. validar una cadena rechazada con el AFD minimizado

## Expresion 1 - AFD ya minimo

- Expresion: `a(b|c)*`
- Cadena aceptada: `acbc`
- Cadena rechazada: `ad`

Lo que deben remarcar:

- el AFD directo ya es minimo
- la minimizacion no cambia cantidad de estados
- la minimizacion no cambia cantidad de transiciones

## Expresion 2 - AFD reducible

- Expresion: `(a|b)*(aa|ab|ba|bb)`
- Cadena aceptada: `abba`
- Cadena rechazada: `a`

Lo que deben remarcar:

- el AFD directo no es minimo
- el AFD minimizado reduce estados
- el AFD minimizado reduce transiciones

## Orden sugerido para grabar

1. Ejecutar `python main.py`
2. Ingresar la expresion 1
3. Mostrar tabla directa
4. Mostrar tabla minimizada
5. Explicar que no hay reduccion
6. Validar la cadena aceptada
7. Validar la cadena rechazada
8. Repetir con la expresion 2
9. Explicar la reduccion de estados y transiciones

## Nota

Con estas dos expresiones se cumplen los dos casos que pide el enunciado de Lab 2:

- un AFD que ya era minimo
- un AFD que si se reduce al aplicar minimizacion
