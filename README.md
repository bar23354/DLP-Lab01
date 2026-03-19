# Laboratorio 02 - Conversion directa y minimizacion de AFD

Este proyecto implementa la parte actual del curso para:

- ingresar una expresion regular
- construir el AFD por metodo directo
- minimizar el AFD resultante
- mostrar la tabla de transiciones del AFD directo
- mostrar la tabla de transiciones del AFD minimizado
- comparar cantidad de estados y transiciones
- validar cadenas usando el AFD minimizado

No se usa `re` ni otra libreria de expresiones regulares.

## Estado actual

La base activa del proyecto esta en [`laboratorio`](./laboratorio) y ya cubre lo principal de Lab 1 y Lab 2.

Hoy el proyecto permite:

- construir el arbol sintactico aumentado
- calcular `anulable`, `primeraPos`, `ultimaPos` y `siguientePos`
- construir el AFD directo
- minimizar el AFD
- mostrar ambas tablas
- comparar estados y transiciones entre ambos automatas
- validar cadenas con el AFD minimizado
- manejar errores comunes en expresiones regulares invalidas
- soportar escapes de operadores y `ε`

Fuera de alcance por ahora:

- clases de caracteres tipo `[]`
- sintaxis Yalex/Yapar dentro de `laboratorio`
- interfaz grafica

## Estructura principal

- [`main.py`](./main.py): menu interactivo principal
- [`programa_afd.py`](./programa_afd.py): entrada alternativa
- [`laboratorio/analizador.py`](./laboratorio/analizador.py): tokenizacion, validacion, concatenacion explicita y postfijo
- [`laboratorio/arbol.py`](./laboratorio/arbol.py): arbol directo y `siguientePos`
- [`laboratorio/construccion_afd.py`](./laboratorio/construccion_afd.py): construccion del AFD directo
- [`laboratorio/minimizacion.py`](./laboratorio/minimizacion.py): minimizacion y metricas
- [`laboratorio/simulador.py`](./laboratorio/simulador.py): simulacion del AFD
- [`laboratorio/tabla.py`](./laboratorio/tabla.py): tablas, detalles y comparacion
- [`tests/`](./tests): pruebas unitarias e integracion con `pytest`

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
   - detalle de `siguientePos` y conjuntos del AFD directo
   - tabla del AFD directo
   - detalle de estados del AFD minimizado
   - tabla del AFD minimizado
   - comparacion de estados y transiciones
5. Luego se puede:
   - validar una cadena con el AFD minimizado
   - volver a ver la tabla directa
   - volver a ver la tabla minimizada
   - volver a ver la comparacion
   - regresar al menu principal

## Como correr los tests

Desde la raiz del proyecto:

```bash
pytest -q
```

La suite actual cubre:

- analizador
- arbol y AFD directo
- minimizacion
- equivalencia entre AFD directo y minimizado
- integracion del pipeline completo
- errores de expresiones invalidas
- edge cases con `ε`, escapes y automatas ya minimos

## Expresiones recomendadas para la demo de Lab 2

Caso que ya es minimo:

- Expresion: `a(b|c)*`
- Cadena aceptada: `acbc`
- Cadena rechazada: `ad`

Comportamiento esperado:

- AFD directo y minimizado tienen la misma cantidad de estados
- AFD directo y minimizado tienen la misma cantidad de transiciones

Caso que si se reduce:

- Expresion: `(a|b)*(aa|ab|ba|bb)`
- Cadena aceptada: `abba`
- Cadena rechazada: `a`

Comportamiento esperado:

- el AFD minimizado tiene menos estados que el AFD directo
- el AFD minimizado tiene menos transiciones que el AFD directo

## Casos validados

Se validaron automaticamente, entre otros, los siguientes casos:

- AFD que ya es minimo
- AFD que si se reduce con minimizacion
- aceptacion y rechazo de cadenas en AFD directo y minimizado
- soporte de `ε`
- soporte de operadores escapados como literales
- rechazo de expresiones invalidas como:
  - `a(`
  - `(a|b`
  - `a|`
  - `*a`
  - `\`
  - `()`

## Video - Laboratorio 2

Enlace al video de Lab 2: [Laboratorio2.mp4](https://uvggt-my.sharepoint.com/:v:/r/personal/tox21276_uvg_edu_gt/Documents/Lab2.mp4?csf=1&web=1&e=D1TdTz&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

## Conclusion

Para lo que pide actualmente Lab 2, esta base ya esta orientada a:

- expresion regular de entrada
- construccion del AFD por metodo directo
- minimizacion del AFD
- tabla del AFD directo
- tabla del AFD minimizado
- comparacion de estados y transiciones
- validacion de cadenas con el AFD minimizado
