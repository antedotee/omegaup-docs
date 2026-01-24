---
title: Idiomas Suportados
description: Linguagens de programação suportadas pelo omegaUp
icon: bootstrap/code-tags
---
# Idiomas Suportados

omegaUp oferece suporte a uma variedade de linguagens de programação para participação e prática em concursos. Esta página documenta cada idioma, sua versão e considerações específicas.

## Visão geral do idioma

| Idioma | Versão | Compilador/Intérprete | Extensão |
|----------|------------|----------|-----------|
| C | CCG 10+ | `gcc` | `.c` |
| C++ 11 | CCG 10+ | `g++` | `.cpp` |
| C++ 17 | CCG 10+ | `g++` | `.cpp` |
| C++20 | CCG 10+ | `g++` | `.cpp` |
| Java | OpenJDK 17+ | `javac` | `.java` |
| Pitão 3 | 3.10+ | `python3` | `.py` |
| Pitão 2 | 2.7 (legado) | `python2` | `.py` |
| Karel (Pascal) | Personalizado | - | `.kp` |
| Carlos (Java) | Personalizado | - | `.kj` |
| Rubi | 3.0+ | `ruby` | `.rb` |
| Pascal | Pascal grátis 3.2+ | `fpc` | `.pas` |
| Haskel | GHC 8.10+ | `ghc` | `.hs` |
| C# | Mono 6.12+ | `mcs` | `.cs` |
| Lua | 5.4+ | `lua` | `.lua` |

## Detalhes do idioma

###C

**Compilador**: GCC 10+  
**Padrão**: C11

```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", n * 2);
    return 0;
}
```
**Compilação**:
```bash
gcc -std=c11 -O2 -lm -o program program.c
```
**Notas**:
- Biblioteca matemática (`-lm`) vinculada automaticamente
- Nível de otimização `-O2` usado

---

### C++ (14/11/17/20)

**Compilador**: GCC 10+  
**Padrão Padrão**: C++17

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
**Compilação por versão**:
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
- `<bits/stdc++.h>` está disponível (inclui todos os cabeçalhos padrão)
- E/S rápida recomendada para entradas grandes
- C++17 inclui recursos úteis como ligações estruturadas, `if constexpr`
- C++20 inclui intervalos, conceitos, `std::format`

---

###Java

**Tempo de execução**: OpenJDK 17+

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
**Compilação**:
```bash
javac -encoding UTF-8 Main.java
```
**Execução**:
```bash
java -Xmx256m Main
```
**Notas**:
- A classe deve ser nomeada `Main`
- Codificação UTF-8 suportada
- Limite de memória passado via flag `-Xmx`
- Use `BufferedReader` para E/S mais rápida:

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

### Python3

**Versão**: 3.10+

```python
n = int(input())
print(n * 2)
```
**Execução**:
```bash
python3 program.py
```
**Notas**:
- Linguagens mais lentas que compiladas (~10-100x)
- Bom para problemas com limites de tempo soltos
- Use `sys.stdin` para E/S mais rápida:

```python
import sys
input = sys.stdin.readline

n = int(input())
print(n * 2)
```
**Bibliotecas disponíveis**:
- `numpy` - Não disponível
- `scipy` - Não disponível
- Somente biblioteca padrão

---

### Python 2 (legado)

**Versão**: 2.7

```python
n = int(raw_input())
print n * 2
```
**Notas**:
- Obsoleto, use Python 3
- Somente para problemas legados
- `raw_input()` em vez de `input()`
- `print` é uma instrução, não uma função

---

###Karel

Karel é uma linguagem simplificada para iniciantes, disponível em sintaxe Pascal e Java.

**Karel (sintaxe Pascal)**:
```pascal
iniciar-programa
    inicia-ejecucion
        mientras frente-libre hacer avanza;
        gira-izquierda;
    termina-ejecucion
finalizar-programa
```
**Karel (sintaxe Java)**:
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
- Conjunto de instruções limitado
- Mundo baseado em grade
- Usado para programação introdutória

---

### Rubi

**Versão**: 3.0+

```ruby
n = gets.to_i
puts n * 2
```
**Execução**:
```bash
ruby program.rb
```
**Notas**:
- Desempenho semelhante ao Python
- Rica biblioteca padrão
- Boa manipulação de cordas

---

### Pascal

**Compilador**: Pascal 3.2+ grátis

```pascal
program Solution;
var
    n: integer;
begin
    readln(n);
    writeln(n * 2);
end.
```
**Compilação**:
```bash
fpc -O2 program.pas
```
**Notas**:
- Linguagem de programação competitiva clássica
- Compilação e execução rápida
- Recursos limitados de linguagem moderna

---

### Haskel

**Compilador**: GHC 8.10+

```haskell
main :: IO ()
main = do
    n <- readLn :: IO Int
    print (n * 2)
```
**Compilação**:
```bash
ghc -O2 program.hs
```
**Notas**:
- Paradigma de programação funcional
- Avaliação preguiçosa
- Bom para problemas matemáticos
- Curva de aprendizado mais acentuada

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
**Compilação**:
```bash
mcs program.cs
```
**Execução**:
```bash
mono program.exe
```
**Notas**:
- Compatível com .NET via Mono
- Boas bibliotecas de strings e coleções
- Um pouco mais lento que C++

---

### Lua

**Versão**: 5.4+

```lua
local n = io.read("*n")
print(n * 2)
```
**Execução**:
```bash
lua program.lua
```
**Notas**:
- Linguagem de script leve
- Sintaxe simples
- Bom para manipulação de strings

---

## Guia de seleção de idioma

### Por tipo de problema

| Tipo de problema | Recomendado | Alternativa |
|--------------|-------------|-------------|
| E/S simples | Pitão 3 | C++ |
| Prazo apertado | C++ | C |
| Manipulação de strings | Pitão 3 | Rubi |
| Matemática | Pitão 3 | Haskel |
| Estruturas de dados | C++ | Java |
| Iniciantes | Karel | Pitão 3 |

### Por limite de tempo

| Limite de tempo | Idiomas recomendados |
|------------|----------------------|
| <0,5s | C, C++ |
| 0,5s - 1s | C++, Java |
| 1s - 2s | C++, Java, Python 3 (simples) |
| > 2s | Qualquer |

## Dicas de desempenho de E/S

### E/S rápida em C++

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
### E/S rápida em Java

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
### E/S rápida em Python

```python
import sys
input = sys.stdin.readline
print = sys.stdout.write

# For output, use print(str(x) + '\n')
```
## Sinalizadores do compilador

### Compilação de depuração (local)

```bash
# C++
g++ -std=c++17 -O2 -Wall -Wextra -Wshadow -g -fsanitize=address,undefined

# Java
javac -Xlint:all
```
### Compilação de Produção (Juiz)

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
## Armadilhas Comuns

### Estouro de número inteiro

| Idioma | Intervalo interno | Use para números grandes |
|----------|-----------|-----------|
| C/C++ | -2³¹ a 2³¹-1 | `long long` |
| Java | -2³¹ a 2³¹-1 | `long` ou `BigInteger` |
| Pitão | Ilimitado | Integrado |

### Problemas de precisão

Comparação de ponto flutuante:

```cpp
// Wrong
if (a == b)

// Correct
const double EPS = 1e-9;
if (abs(a - b) < EPS)
```
### Limites de memória

Limites de tamanho de pilha (profundidade de recursão):

| Idioma | Pilha padrão | Solução |
|----------|-------------|----------|
| C++ | ~1MB | Use pilha explícita |
| Java | ~1MB | Aumente com `-Xss` |
| Pitão | ~1000 chamadas | `sys.setrecursionlimit()` |

## Documentação Relacionada

- **[Runner Internals](../architecture/runner-internals.md)** - Detalhes de execução
- **[Veredictos](../features/verdicts.md)** - Noções básicas sobre erros
- **[API de problemas](../api/problems.md)** - Configurações de problemas
