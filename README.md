## Conversión directa de expresión regular a AFD

Este Laboratorio 01 implementa el **método directo** para construir un **autómata finito determinista (AFD)** a partir de una **expresión regular**, genera la **tabla de transición de estados** y permite **validar cadenas** usando el AFD construido.

No se utilizan librerías de expresiones regulares (`re` u otras); toda la conversión y simulación se realiza manualmente.

---

## Requisitos que cumple el laboratorio

- **Ingreso de expresión regular**:  
  El programa principal (`main.py` / `programa_afd.py`) pide al usuario una expresión regular por consola.

- **Construcción del AFD por método directo**:  
  - `laboratorio/analizador.py`: tokeniza la expresión, inserta concatenación explícita y la convierte a postfijo.  
  - `laboratorio/arbol.py`: construye el árbol sintáctico, calcula `anulable`, `primeraPos`, `ultimaPos` y `siguientePos` (algoritmo directo por posiciones).  
  - `laboratorio/construccion_afd.py`: a partir del árbol aumentado con `#` construye directamente el AFD (conjuntos de posiciones → estados `S0, S1, ...`).

- **Generación de tabla de transición**:  
  - `laboratorio/tabla.py`: muestra en consola la **tabla de transiciones del AFD**, indicando estado inicial, estados de aceptación y alfabeto.

- **Validación de cadenas con el AFD**:  
  - `laboratorio/simulador.py`: simula el recorrido del AFD sobre una cadena dada.  
  - `main.py`: permite ingresar cadenas, ver el recorrido de estados y decide si son **ACEPTADAS** o **RECHAZADAS**.

- **Operadores soportados**:
  - Unión: `|`
  - Concatenación: implícita (el analizador inserta `.` internamente)
  - Cerradura de Kleene: `*`
  - Cerradura positiva: `+`
  - Opcional: `?`
  - Agrupación: `(` `)`
  - Escape: `\` para usar un carácter literal (por ejemplo `\*`, `\|`, `\?`, etc.)

- **Sin librerías de regex**:  
  Se ha verificado que en el código **no se importa `re` ni ninguna otra librería de expresiones regulares**; toda la lógica es propia.

---

## Estructura del proyecto

- `main.py` / `programa_afd.py`: programa principal, menú interactivo.
- `laboratorio/analizador.py`: tokenización, inserción de concatenación y conversión a notación postfija.
- `laboratorio/arbol.py`: construcción del árbol sintáctico y cálculo de `siguientePos`.
- `laboratorio/construccion_afd.py`: construcción del AFD mediante el método directo por posiciones.
- `laboratorio/tabla.py`: impresión de la tabla de transición y detalle de conjuntos de posiciones.
- `laboratorio/simulador.py`: simulación del AFD sobre una cadena.

---

## Ejecución

1. Asegurarse de tener **Python 3** instalado.
2. Abrir una terminal en la carpeta del proyecto (`DLP-Lab01`).
3. Ejecutar:

```bash
python main.py
```

o bien:

```bash
python programa_afd.py
```

Según el archivo que se utilice como entrada principal.

---

## Uso del programa

Al ejecutar `main.py` se muestra un menú:

- **[1] Nueva expresión**: permite ingresar una expresión regular.
- **[2] Salir**: termina el programa.

Flujo típico:

1. Elegir opción **1**.
2. Ingresar la **expresión regular** (por ejemplo: `a(b|c)*d+?`).
   - El programa mostrará:
     - Expresión con concatenación explícita.
     - Forma en postfijo.
     - Alfabeto detectado.
     - Detalle de `siguientePos` y conjuntos de posiciones por estado.
     - Tabla de transición del AFD resultante.
3. Luego aparece un submenú:
   - **[a] Validar cadena**: permite ingresar una cadena y muestra:
     - La cadena ingresada.
     - El recorrido de estados del AFD.
     - Si la cadena es **ACEPTADA** o **RECHAZADA**.
   - **[b] Ver tabla**: vuelve a mostrar la tabla de transiciones del AFD actual.
   - **[c] Volver**: regresar al menú principal para ingresar otra expresión o salir.

---

## Ejemplos de expresiones para la demostración

Se requieren **al menos tres expresiones regulares** donde, en conjunto, aparezcan todos los operadores `|`, concatenación implícita, `*`, `+`, `?`.

Algunas posibles expresiones de ejemplo:

- **Expresión 1** (usa unión y `*`):
  - `a(b|c)*`

- **Expresión 2** (usa concatenación, `+` y `?`):
  - `ab+c?`

- **Expresión 3** (usa todos los operadores y agrupación):
  - `(a|b)*c+d?`

Para cumplir con el requisito del enunciado, durante la demostración:

- **Ingresar y validar** una cadena que **sí** pertenezca al lenguaje de cada expresión.
- **Ingresar y validar** una cadena que **no** pertenezca al lenguaje de alguna expresión.
- Mostrar la **tabla de transición** del AFD para al menos una de las expresiones (el programa ya lo hace automáticamente).

---

## Notas sobre la implementación

- La concatenación es **implícita** en la expresión del usuario; internamente el analizador inserta el operador `.` donde corresponde.
- El método directo se implementa siguiendo el enfoque por **posiciones** (`primeraPos`, `ultimaPos`, `siguientePos`) y luego construyendo el AFD como autómata de subconjuntos de posiciones.
- El marcador `#` se añade automáticamente al final de la expresión interna para identificar los **estados de aceptación**.

---

## Créditos

Proyecto desarrollado como laboratorio de **Diseño de Lenguajes de Programación** para la construcción directa de AFD a partir de expresiones regulares.