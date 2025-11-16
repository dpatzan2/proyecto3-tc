# Proyecto 3 - Simulador de Máquinas de Turing para Cifrado César

**Teoría de la Computación 2025**  
**Universidad del Valle de Guatemala**

#### **Miembros del equipo**
**Diego Patzan, Roberto Najera, Luis Gonzalez**  

---

## Descripción del Proyecto

Este proyecto implementa dos Máquinas de Turing en Python para:
1. **Encriptar** mensajes usando el cifrado César: `E(x) = (x + k) mod 26`
2. **Decriptar** mensajes usando el descifrado César: `D(x) = (x - k) mod 26`

El cifrado César es una técnica de sustitución donde cada letra del mensaje se desplaza un número fijo de posiciones en el alfabeto.

---

## Estructura del Proyecto

```
proyecto3/
│
├── main.py                          # Programa principal
├── src/
│   ├── turing_machine.py            # Clase base de Máquina de Turing
│   ├── caesar_encrypt.py            # MT para encriptación
│   └── caesar_decrypt.py            # MT para decriptación
├── config/
│   ├── encrypt_config.json          # Configuración MT encriptación
│   └── decrypt_config.json          # Configuración MT decriptación
├── examples/
│   ├── ejemplo1_entrada.txt         # Ejemplo 1 del PDF
│   ├── ejemplo2_entrada.txt         # Ejemplo 2 del PDF
│   └── ejemplo3_entrada.txt         # Ejemplo 3 del PDF
├── README.md                        # Este archivo
└── Proyecto3.pdf                    # Especificación del proyecto
```

---

## Requisitos

- **Python 3.7 o superior**
- No requiere librerías externas (solo módulos estándar de Python)

---

## Instalación y Ejecución

### 1. Clonar o descargar el proyecto

```bash
cd proyecto3
```

### 2. Ejecutar el programa principal

```bash
python3 main.py
```

### 3. Usar el menú interactivo

El programa ofrece las siguientes opciones:
1. Encriptar mensaje
2. Decriptar mensaje
3. Ejecutar ejemplos del proyecto (del PDF)
4. Ejecutar pruebas adicionales
5. Salir

---

## Formato de Entrada

Los mensajes deben seguir el formato: `llave#MENSAJE`

### Llave
- **Numérica**: Un número del 1 al 27 (ejemplo: `3#MENSAJE`)
- **Alfabética**: Una letra A-Z (ejemplo: `D#MENSAJE`, donde D=3)

#### Tabla de Conversión Letra → Número:
```
A = 0    H = 7    O = 14   V = 21
B = 1    I = 8    P = 15   W = 22
C = 2    J = 9    Q = 16   X = 23
D = 3    K = 10   R = 17   Y = 24
E = 4    L = 11   S = 18   Z = 25
F = 5    M = 12   T = 19
G = 6    N = 13   U = 20
```

**Ejemplos:**
- Llave `D` = desplazamiento de 3 posiciones
- Llave `N` = desplazamiento de 13 posiciones (ROT13)
- Llave `Z` = desplazamiento de 25 posiciones

### Mensaje
- Solo letras A-Z (se convierten automáticamente a mayúsculas)
- Los espacios se preservan
- La puntuación se mantiene sin cambios

### Ejemplos de Entrada Válida

```
3#ROMA NO FUE CONSTRUIDA EN UN DIA
D#ROMA NO FUE CONSTRUIDA EN UN DIA
13#ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

---

## Ejemplos de Uso

### Ejemplo 1: Encriptación con llave numérica

**Entrada:**
```
3#ROMA NO FUE CONSTRUIDA EN UN DIA
```

**Salida:**
```
URPD QR IXH FRQVWUXLGD HQ XQ GLD
```

### Ejemplo 2: Encriptación con llave alfabética

**Entrada:**
```
D#ROMA NO FUE CONSTRUIDA EN UN DIA
```

**Salida:**
```
URPD QR IXH FRQVWUXLGD HQ XQ GLD
```

### Ejemplo 3: Decriptación

**Entrada:**
```
3#URPD QR IXH FRQVWUXLGD HQ XQ GLD
```

**Salida:**
```
ROMA NO FUE CONSTRUIDA EN UN DIA
```

---

## Implementación Técnica

### Máquina de Turing Base (`turing_machine.py`)

La clase `TuringMachine` implementa un simulador genérico con las operaciones básicas:
- **Cambiar de estado**: Transición entre estados
- **Sustituir símbolo**: Escribir en la cinta
- **Mover cabezal**: Izquierda (L) o Derecha (R)

#### Componentes principales:
- `Q`: Conjunto de estados
- `Σ`: Alfabeto de entrada (A-Z, dígitos, espacios)
- `Γ`: Alfabeto de cinta (incluye símbolos auxiliares)
- `q₀`: Estado inicial
- `F`: Estados de aceptación
- `δ`: Función de transición

### Máquina de Encriptación (`caesar_encrypt.py`)

Implementa el algoritmo: **E(x) = (x + k) mod 26**

**Proceso:**
1. Lee la llave del inicio de la cadena
2. Convierte la llave (numérica o alfabética) a valor numérico
3. Procesa cada carácter del mensaje
4. Aplica el desplazamiento César
5. Mantiene espacios y puntuación sin cambios

### Máquina de Decriptación (`caesar_decrypt.py`)

Implementa el algoritmo: **D(x) = (x - k) mod 26**

**Proceso:**
1. Lee la llave del inicio de la cadena
2. Procesa cada carácter del mensaje cifrado
3. Aplica el desplazamiento inverso
4. Recupera el mensaje original

### Nota sobre Operaciones Aritméticas

El proyecto respeta la restricción de que las Máquinas de Turing solo pueden realizar operaciones básicas. Las operaciones aritméticas (suma, resta, módulo) se implementan mediante:
- Representación posicional de números
- Transiciones de estado que simulan aritmética básica
- Tablas de transición generadas para cada llave específica

---

## Configuración de las Máquinas

Los archivos JSON en `config/` definen la estructura formal de las MT:

```json
{
  "states": ["q_init", "q_process", "q_accept"],
  "input_alphabet": ["A", "B", "C", ..., "Z", "#", "0-9"],
  "tape_alphabet": ["A", "B", "C", ..., "Z", "#", "_", "|", "X"],
  "initial_state": "q_init",
  "accept_states": ["q_accept"],
  "transitions": [...]
}
```

---

## Pruebas y Validación

### Ejecutar Ejemplos del Proyecto

Opción 3 del menú ejecuta automáticamente los 4 ejemplos del PDF del proyecto.

### Ejecutar Pruebas Adicionales

Opción 4 del menú ejecuta casos de prueba adicionales:
- Desplazamientos pequeños (k=1)
- Desplazamientos grandes (k=25)
- ROT13 (k=13)
- Alfabeto completo
- Frases académicas

### Verificación

Cada prueba verifica que:
```
Mensaje Original → Encriptar → Decriptar → Mensaje Original
```

---

## Ejecución desde Línea de Comandos

Para ejecutar los ejemplos directamente:

```bash
# Encriptar
python3 -c "from src.caesar_encrypt import create_encrypt_machine; m = create_encrypt_machine(); print(m.encrypt('3#ROMA NO FUE CONSTRUIDA EN UN DIA'))"

# Decriptar
python3 -c "from src.caesar_decrypt import create_decrypt_machine; m = create_decrypt_machine(); print(m.decrypt('3#URPD QR IXH FRQVWUXLGD HQ XQ GLD'))"
```



---

## Limitaciones y Consideraciones

1. **Alfabeto**: Solo procesa letras A-Z (26 letras)
2. **Espacios**: Se preservan en el texto cifrado
3. **Puntuación**: Se mantiene sin cambios
4. **Mayúsculas/Minúsculas**: Todo se convierte a mayúsculas
5. **Rendimiento**: Optimizado para mensajes de longitud razonable


---

## Referencias

- Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). *Introduction to Automata Theory, Languages, and Computation*
- Sipser, M. (2012). *Introduction to the Theory of Computation*
- Material del curso de Teoría de la Computación 2025




