# Laboratorio 01 - Conversion directa de expresion regular a AFD

Este proyecto implementa la parte actual del laboratorio:

- ingreso de una expresion regular
- construccion directa de un AFD a partir de la expresion
- generacion de la tabla de transiciones
- simulacion del AFD para validar cadenas

No se usa `re` ni otra libreria de expresiones regulares. Toda la logica es propia.

## Estado actual

Para el alcance de esta entrega, la parte de conversion directa a AFD y simulacion ya esta funcional.

Hoy el proyecto permite:

- construir el arbol sintactico aumentado
- calcular `anulable`, `primeraPos`, `ultimaPos` y `siguientePos`
- construir el AFD directo
- mostrar la tabla de transiciones
- validar si una cadena es aceptada o rechazada
- manejar errores comunes en expresiones regulares invalidas
- soportar escapes de operadores y el simbolo `e` griega `ε`

Fuera de alcance por ahora:

- clases de caracteres tipo `[]`
- sintaxis Yalex/Yapar dentro de `laboratorio`
- minimizacion del AFD

## Estructura principal

- [`main.py`](C:\Users\djlop\OneDrive\DIEGO\UVG\2026\primer semestre\Diseño de Lenguajes de Programación\DLP-Lab01\main.py): menu interactivo principal
- [`programa_afd.py`](C:\Users\djlop\OneDrive\DIEGO\UVG\2026\primer semestre\Diseño de Lenguajes de Programación\DLP-Lab01\programa_afd.py): entrada alternativa con el mismo flujo
- [`laboratorio/analizador.py`](C:\Users\djlop\OneDrive\DIEGO\UVG\2026\primer semestre\Diseño de Lenguajes de Programación\DLP-Lab01\laboratorio\analizador.py): tokenizacion, validacion, concatenacion explicita y postfijo
- [`laboratorio/arbol.py`](C:\Users\djlop\OneDrive\DIEGO\UVG\2026\primer semestre\Diseño de Lenguajes de Programación\DLP-Lab01\laboratorio\arbol.py): arbol directo y `siguientePos`
- [`laboratorio/construccion_afd.py`](C:\Users\djlop\OneDrive\DIEGO\UVG\2026\primer semestre\Diseño de Lenguajes de Programación\DLP-Lab01\laboratorio\construccion_afd.py): construccion del AFD
- [`laboratorio/simulador.py`](C:\Users\djlop\OneDrive\DIEGO\UVG\2026\primer semestre\Diseño de Lenguajes de Programación\DLP-Lab01\laboratorio\simulador.py): simulacion del AFD
- [`laboratorio/tabla.py`](C:\Users\djlop\OneDrive\DIEGO\UVG\2026\primer semestre\Diseño de Lenguajes de Programación\DLP-Lab01\laboratorio\tabla.py): detalle por posicion y tabla de transiciones
- [`tests/`](C:\Users\djlop\OneDrive\DIEGO\UVG\2026\primer semestre\Diseño de Lenguajes de Programación\DLP-Lab01\tests): pruebas unitarias e integracion con `pytest`

## Operadores soportados

- Union: `|`
- Concatenacion: implicita, el programa inserta `.` internamente
- Cerradura de Kleene: `*`
- Cerradura positiva: `+`
- Opcional: `?`
- Agrupacion: `(` y `)`
- Escape: `\` para tratar un operador como literal, por ejemplo `\*`, `\|`, `\(`, `\)`
- Epsilon: `ε`

Notas:

- `ε` representa cadena vacia
- `\ε` representa el simbolo literal `ε`

## Requisitos

- Python 3
- `pytest` para correr la suite de pruebas

## Como ejecutarlo

Desde la carpeta raiz del proyecto:

```bash
python main.py
```

O bien:

```bash
python programa_afd.py
```

## Flujo de uso

1. Ejecutar `python main.py`
2. Elegir opcion `1`
3. Ingresar una expresion regular
4. El programa muestra:
   - expresion con concatenacion explicita
   - expresion en postfijo
   - alfabeto detectado
   - detalle de `siguientePos`
   - conjuntos de posiciones por estado
   - tabla de transiciones del AFD
5. Luego se puede:
   - validar una cadena
   - volver a mostrar la tabla
   - regresar al menu principal

## Ejemplos recomendados para la demo

Estas expresiones ya estan cubiertas por la implementacion actual:

- `a(b|c)*`
- `ab+c?`
- `(a|b)*c+d?`

Tambien se pueden mostrar estos casos utiles:

- `a?`
- `ε`
- `a\*b`
- `(a|ε)b`

Ejemplos de cadenas:

- Para `a(b|c)*`
  - aceptada: `acbc`
  - rechazada: `ad`
- Para `ab+c?`
  - aceptada: `abbc`
  - rechazada: `ac`
- Para `(a|b)*c+d?`
  - aceptada: `bbccd`
  - rechazada: `ab`

## Como correr los tests

Desde la raiz del proyecto:

```bash
pytest -q
```

La suite actual incluye:

- pruebas unitarias del analizador
- pruebas del arbol y del AFD
- pruebas de integracion del pipeline completo
- regresiones para escapes, `ε` y expresiones invalidas

## Casos validados

Se validaron automaticamente, entre otros, los siguientes casos:

- construccion correcta del pipeline para expresiones validas
- aceptacion y rechazo de cadenas
- soporte de `ε`
- soporte de operadores escapados como literales
- rechazo de expresiones invalidas como:
  - `a(`
  - `(a|b`
  - `a|`
  - `*a`
  - `\`
  - `()`

## Conclusion

Para lo que pide actualmente el ejercicio, esta parte ya esta cubierta:

- expresion regular de entrada
- construccion del AFD por metodo directo
- tabla de transiciones
- validacion de cadenas con el AFD

La base tambien quedo organizada para futuras entregas, sin depender del codigo mezclado en `temp`.
