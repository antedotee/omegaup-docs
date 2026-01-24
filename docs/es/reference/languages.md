---
title: Idiomas admitidos
description: Lenguajes de programación soportados por omegaUp
icon: bootstrap/code-tags
---
# Idiomas admitidos

omegaUp admite una variedad de lenguajes de programación para participar y practicar en concursos. Esta página documenta cada idioma, su versión y consideraciones específicas.

## Descripción general del idioma

| Idioma | Versión | Compilador/Intérprete | Ampliación |
|----------|---------|---------------------|-----------|
| C | CCG 10+ | `gcc` | `.c` |
| C++ 11 | CCG 10+ | `g++` | `.cpp` |
| C++ 17 | CCG 10+ | `g++` | `.cpp` |
| C++ 20 | CCG 10+ | `g++` | `.cpp` |
| Java | OpenJDK 17+ | `javac` | `.java` |
| Pitón 3 | 3.10+ | `python3` | `.py` |
| Pitón 2 | 2.7 (heredado) | `python2` | `.py` |
| Karel (Pascal) | Personalizado | - | `.kp` |
| Karel (Java) | Personalizado | - | `.kj` |
| Rubí | 3.0+ | `ruby` | `.rb` |
| Pascal | Pascal gratuito 3.2+ | `fpc` | `.pas` |
| Haskel | GHC 8.10+ | `ghc` | `.hs` |
| C# | Mono 6.12+ | `mcs` | `.cs` |
| Lúa | 5.4+ | `lua` | `.lua` |

## Detalles del idioma

### C

**Compilador**: GCC 10+  
**Estándar**: C11

```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", n * 2);
    return 0;
}
```
**Compilación**:
```bash
gcc -std=c11 -O2 -lm -o program program.c
```
**Notas**:
- Biblioteca de matemáticas (`-lm`) vinculada automáticamente
- Nivel de optimización `-O2` utilizado

---

### C++ (14/11/17/20)

**Compilador**: GCC 10+  
**Estándar predeterminado**: C++17

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    cout << n * 2 << '\n';
    return 0;
}
```
**Recopilación por versión**:
```bash
# C++11
g++ -std=c++11 -O2 -lm -o program program.cpp

# C++14
g++ -std=c++14 -O2 -lm -o program program.cpp

# C++17 (default)
g++ -std=c++17 -O2 -lm -o program program.cpp

# C++20
g++ -std=c++20 -O2 -lm -o program program.cpp
```
**Notas**:
- `<bits/stdc++.h>` está disponible (incluye todos los cabezales estándar)
- E/S rápida recomendada para entradas grandes
- C++17 incluye funciones útiles como enlaces estructurados, `if constexpr`
- C++20 incluye rangos, conceptos, `std::format`

---

###Java

**Tiempo de ejecución**: OpenJDK 17+

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(n * 2);
    }
}
```
**Compilación**:
```bash
javac -encoding UTF-8 Main.java
```
**Ejecución**:
```bash
java -Xmx256m Main
```
**Notas**:
- La clase debe llamarse `Main`
- Codificación UTF-8 compatible
- Límite de memoria superado mediante el indicador `-Xmx`
- Utilice `BufferedReader` para E/S más rápidas:

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedOutputStream(System.out));
        
        int n = Integer.parseInt(br.readLine());
        pw.println(n * 2);
        pw.flush();
    }
}
```
---

### Pitón 3

**Versión**: 3.10+

```python
n = int(input())
print(n * 2)
```
**Ejecución**:
```bash
python3 program.py
```
**Notas**:
- Más lento que los lenguajes compilados (~10-100x)
- Bueno para problemas con límites de tiempo flexibles.
- Utilice `sys.stdin` para E/S más rápidas:

```python
import sys
input = sys.stdin.readline

n = int(input())
print(n * 2)
```
**Bibliotecas disponibles**:
- `numpy` - No disponible
- `scipy` - No disponible
- Sólo biblioteca estándar

---

### Python 2 (heredado)

**Versión**: 2.7

```python
n = int(raw_input())
print n * 2
```
**Notas**:
- En desuso, use Python 3
- Sólo para problemas heredados
- `raw_input()` en lugar de `input()`
- `print` es una declaración, no una función

---

### Karel

Karel es un lenguaje simplificado para principiantes, disponible en sintaxis Pascal y Java.

**Karel (sintaxis de Pascal)**:
```pascal
iniciar-programa
    inicia-ejecucion
        mientras frente-libre hacer avanza;
        gira-izquierda;
    termina-ejecucion
finalizar-programa
```
**Karel (sintaxis Java)**:
```java
class program {
    program() {
        while (frontIsClear()) {
            move();
        }
        turnLeft();
    }
}
```
**Notas**:
- Conjunto de instrucciones limitado
- Mundo basado en red
- Utilizado para programación introductoria.

---

### rubí

**Versión**: 3.0+

```ruby
n = gets.to_i
puts n * 2
```
**Ejecución**:
```bash
ruby program.rb
```
**Notas**:
- Rendimiento similar a Python
- Biblioteca estándar rica
- Buena manipulación de cuerdas

---

### Pascal

**Compilador**: Pascal 3.2+ gratuito

```pascal
program Solution;
var
    n: integer;
begin
    readln(n);
    writeln(n * 2);
end.
```
**Compilación**:
```bash
fpc -O2 program.pas
```
**Notas**:
- Lenguaje de programación competitivo clásico.
- Rápida compilación y ejecución.
- Funciones limitadas del lenguaje moderno.

---

### Haskel

**Compilador**: GHC 8.10+

```haskell
main :: IO ()
main = do
    n <- readLn :: IO Int
    print (n * 2)
```
**Compilación**:
```bash
ghc -O2 program.hs
```
**Notas**:
- Paradigma de programación funcional
- Evaluación perezosa
- Bueno para problemas matemáticos.
- Curva de aprendizaje más pronunciada

---

###C#

**Compilador**: Mono 6.12+

```csharp
using System;

class Program {
    static void Main() {
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine(n * 2);
    }
}
```
**Compilación**:
```bash
mcs program.cs
```
**Ejecución**:
```bash
mono program.exe
```
**Notas**:
- Compatible con .NET a través de Mono
- Buenas bibliotecas de cuerdas y colecciones.
- Ligeramente más lento que C++

---

### lua

**Versión**: 5.4+

```lua
local n = io.read("*n")
print(n * 2)
```
**Ejecución**:
```bash
lua program.lua
```
**Notas**:
- Lenguaje de scripting ligero
- Sintaxis simple
- Bueno para manipulación de cuerdas

---

## Guía de selección de idioma

### Por tipo de problema

| Tipo de problema | Recomendado | Alternativa |
|--------------|-------------|-------------|
| E/S sencillas | Pitón 3 | C++ |
| Límite de tiempo ajustado | C++ | C |
| Manipulación de cadenas | Pitón 3 | Rubí |
| Matemática | Pitón 3 | Haskel |
| Estructuras de datos | C++ | Java |
| Principiantes | Karel | Pitón 3 |

### Por límite de tiempo

| Límite de tiempo | Idiomas recomendados |
|------------|----------------------|
| < 0,5 s | C, C++ |
| 0,5s - 1s | C++, Java |
| 1s - 2s | C++, Java, Python 3 (sencillo) |
| > 2s | Cualquiera |

## Consejos de rendimiento de E/S

### E/S rápida en C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Your code here
    return 0;
}
```
### E/S rápida en Java

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // Your code here
    }
}
```
### E/S rápida en Python

```python
import sys
input = sys.stdin.readline
print = sys.stdout.write

# For output, use print(str(x) + '\n')
```
## Banderas del compilador

### Compilación de depuración (local)

```bash
# C++
g++ -std=c++17 -O2 -Wall -Wextra -Wshadow -g -fsanitize=address,undefined

# Java
javac -Xlint:all
```
### Compilación de producción (juez)

```bash
# C++
g++ -std=c++17 -O2 -lm

# C
gcc -std=c11 -O2 -lm

# Pascal
fpc -O2

# Haskell
ghc -O2
```
## Errores comunes

### Desbordamiento de enteros

| Idioma | rango entero | Uso para números grandes |
|----------|-----------|----------------------|
| C/C++ | -2³¹ a 2³¹-1 | `long long` |
| Java | -2³¹ a 2³¹-1 | `long` o `BigInteger` |
| Pitón | Ilimitado | Incorporado |

### Problemas de precisión

Comparación de coma flotante:

```cpp
// Wrong
if (a == b)

// Correct
const double EPS = 1e-9;
if (abs(a - b) < EPS)
```
### Límites de memoria

Límites de tamaño de pila (profundidad de recursividad):

| Idioma | Pila predeterminada | Solución |
|----------|--------------|----------|
| C++ | ~1MB | Utilice pila explícita |
| Java | ~1MB | Aumentar con `-Xss` |
| Pitón | ~1000 llamadas | `sys.setrecursionlimit()` |

## Documentación relacionada

- **[Runner Internals](../architecture/runner-internals.md)** - Detalles de ejecución
- **[Veredictos](../features/verdicts.md)** - Comprender los errores
- **[API de problemas](../api/problems.md)** - Configuración de problemas
