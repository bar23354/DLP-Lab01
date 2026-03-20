# Laboratorio 02 - Conversion directa y minimizacion de AFD

Programa en consola para:

- ingresar una expresion regular
- construir el AFD por metodo directo
- minimizar el AFD
- mostrar tablas de transicion (directo y minimizado)
- comparar estados y transiciones
- validar cadenas con el AFD minimizado

## Alcance

- arbol sintactico aumentado
- calculo de `anulable`, `primeraPos`, `ultimaPos` y `siguientePos`
- construccion de AFD directo
- minimizacion
- simulacion de cadenas
- manejo de errores de expresiones invalidas

No incluye:

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

- Python
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
   - alfabeto
   - tabla del AFD directo
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

Caso ya minimo:

- Expresion: `a(b|c)*`
- Cadena aceptada: `acbc`
- Cadena rechazada: `ad`

Esperado:

- AFD directo y minimizado tienen la misma cantidad de estados
- AFD directo y minimizado tienen la misma cantidad de transiciones

Caso que se reduce:

- Expresion: `(a|b)*(aa|ab|ba|bb)`
- Cadena aceptada: `abba`
- Cadena rechazada: `a`

Esperado:

- el AFD minimizado tiene menos estados que el AFD directo
- el AFD minimizado tiene menos transiciones que el AFD directo

## Casos validados

Casos cubiertos por pruebas:

- AFD ya minimo
- AFD reducible por minimizacion
- equivalencia entre AFD directo y minimizado
- aceptacion y rechazo de cadenas
- soporte de `ε` y operadores escapados
- rechazo de expresiones invalidas (`a(`, `(a|b`, `a|`, `*a`, `\`, `()`)

## Video - Laboratorio 2

Enlace al video de Lab 2: [Laboratorio2.mp4](https://uvggt-my.sharepoint.com/:v:/r/personal/tox21276_uvg_edu_gt/Documents/Lab2.mp4?csf=1&web=1&e=D1TdTz&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)