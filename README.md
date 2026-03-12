# Laboratorio 01 - Conversion directa de expresion regular a AFD

Diego Lopez #23747
Jennifer Toxcon #21276
Roberto Barreda #23354

### VIDEO: https://uvggt-my.sharepoint.com/:v:/g/personal/bar23354_uvg_edu_gt/IQCg4thh7dhQR7QW2jdnh1i-ASE2x7gNW8zekyacpMGvQbg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=3uMfPJ

Este proyecto implementa:

- ingreso de una expresion regular
- construccion directa de un AFD a partir de la expresion
- generacion de la tabla de transiciones
- simulacion del AFD para validar cadenas

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
