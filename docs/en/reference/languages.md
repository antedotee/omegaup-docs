---
title: Supported Languages
description: Programming languages supported by omegaUp
icon: bootstrap/code-tags
---

# Supported Languages

omegaUp supports a variety of programming languages for contest participation and practice. This page documents each language, its version, and specific considerations.

## Language Overview

| Language | Version | Compiler/Interpreter | Extension |
|----------|---------|---------------------|-----------|
| C | GCC 10+ | `gcc` | `.c` |
| C++ 11 | GCC 10+ | `g++` | `.cpp` |
| C++ 17 | GCC 10+ | `g++` | `.cpp` |
| C++ 20 | GCC 10+ | `g++` | `.cpp` |
| Java | OpenJDK 17+ | `javac` | `.java` |
| Python 3 | 3.10+ | `python3` | `.py` |
| Python 2 | 2.7 (legacy) | `python2` | `.py` |
| Karel (Pascal) | Custom | - | `.kp` |
| Karel (Java) | Custom | - | `.kj` |
| Ruby | 3.0+ | `ruby` | `.rb` |
| Pascal | Free Pascal 3.2+ | `fpc` | `.pas` |
| Haskell | GHC 8.10+ | `ghc` | `.hs` |
| C# | Mono 6.12+ | `mcs` | `.cs` |
| Lua | 5.4+ | `lua` | `.lua` |

## Language Details

### C

**Compiler**: GCC 10+  
**Standard**: C11

```c
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", n * 2);
    return 0;
}
```

**Compilation**:
```bash
gcc -std=c11 -O2 -lm -o program program.c
```

**Notes**:
- Math library (`-lm`) automatically linked
- Optimization level `-O2` used

---

### C++ (11/14/17/20)

**Compiler**: GCC 10+  
**Default Standard**: C++17

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

**Compilation by version**:
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

**Notes**:
- `<bits/stdc++.h>` is available (includes all standard headers)
- Fast I/O recommended for large inputs
- C++17 includes useful features like structured bindings, `if constexpr`
- C++20 includes ranges, concepts, `std::format`

---

### Java

**Runtime**: OpenJDK 17+

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

**Compilation**:
```bash
javac -encoding UTF-8 Main.java
```

**Execution**:
```bash
java -Xmx256m Main
```

**Notes**:
- Class must be named `Main`
- UTF-8 encoding supported
- Memory limit passed via `-Xmx` flag
- Use `BufferedReader` for faster I/O:

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

### Python 3

**Version**: 3.10+

```python
n = int(input())
print(n * 2)
```

**Execution**:
```bash
python3 program.py
```

**Notes**:
- Slower than compiled languages (~10-100x)
- Good for problems with loose time limits
- Use `sys.stdin` for faster I/O:

```python
import sys
input = sys.stdin.readline

n = int(input())
print(n * 2)
```

**Available Libraries**:
- `numpy` - Not available
- `scipy` - Not available
- Standard library only

---

### Python 2 (Legacy)

**Version**: 2.7

```python
n = int(raw_input())
print n * 2
```

**Notes**:
- Deprecated, use Python 3
- Only for legacy problems
- `raw_input()` instead of `input()`
- `print` is a statement, not a function

---

### Karel

Karel is a simplified language for beginners, available in Pascal and Java syntax.

**Karel (Pascal syntax)**:
```pascal
iniciar-programa
    inicia-ejecucion
        mientras frente-libre hacer avanza;
        gira-izquierda;
    termina-ejecucion
finalizar-programa
```

**Karel (Java syntax)**:
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

**Notes**:
- Limited instruction set
- Grid-based world
- Used for introductory programming

---

### Ruby

**Version**: 3.0+

```ruby
n = gets.to_i
puts n * 2
```

**Execution**:
```bash
ruby program.rb
```

**Notes**:
- Similar performance to Python
- Rich standard library
- Good string manipulation

---

### Pascal

**Compiler**: Free Pascal 3.2+

```pascal
program Solution;
var
    n: integer;
begin
    readln(n);
    writeln(n * 2);
end.
```

**Compilation**:
```bash
fpc -O2 program.pas
```

**Notes**:
- Classical competitive programming language
- Fast compilation and execution
- Limited modern language features

---

### Haskell

**Compiler**: GHC 8.10+

```haskell
main :: IO ()
main = do
    n <- readLn :: IO Int
    print (n * 2)
```

**Compilation**:
```bash
ghc -O2 program.hs
```

**Notes**:
- Functional programming paradigm
- Lazy evaluation
- Good for mathematical problems
- Steeper learning curve

---

### C#

**Compiler**: Mono 6.12+

```csharp
using System;

class Program {
    static void Main() {
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine(n * 2);
    }
}
```

**Compilation**:
```bash
mcs program.cs
```

**Execution**:
```bash
mono program.exe
```

**Notes**:
- .NET compatible via Mono
- Good string and collection libraries
- Slightly slower than C++

---

### Lua

**Version**: 5.4+

```lua
local n = io.read("*n")
print(n * 2)
```

**Execution**:
```bash
lua program.lua
```

**Notes**:
- Lightweight scripting language
- Simple syntax
- Good for string manipulation

---

## Language Selection Guide

### By Problem Type

| Problem Type | Recommended | Alternative |
|--------------|-------------|-------------|
| Simple I/O | Python 3 | C++ |
| Tight time limit | C++ | C |
| String manipulation | Python 3 | Ruby |
| Mathematical | Python 3 | Haskell |
| Data structures | C++ | Java |
| Beginners | Karel | Python 3 |

### By Time Limit

| Time Limit | Recommended Languages |
|------------|----------------------|
| < 0.5s | C, C++ |
| 0.5s - 1s | C++, Java |
| 1s - 2s | C++, Java, Python 3 (simple) |
| > 2s | Any |

## I/O Performance Tips

### Fast I/O in C++

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

### Fast I/O in Java

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

### Fast I/O in Python

```python
import sys
input = sys.stdin.readline
print = sys.stdout.write

# For output, use print(str(x) + '\n')
```

## Compiler Flags

### Debug Compilation (Local)

```bash
# C++
g++ -std=c++17 -O2 -Wall -Wextra -Wshadow -g -fsanitize=address,undefined

# Java
javac -Xlint:all
```

### Production Compilation (Judge)

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

## Common Pitfalls

### Integer Overflow

| Language | int Range | Use for large numbers |
|----------|-----------|----------------------|
| C/C++ | -2³¹ to 2³¹-1 | `long long` |
| Java | -2³¹ to 2³¹-1 | `long` or `BigInteger` |
| Python | Unlimited | Built-in |

### Precision Issues

Floating point comparison:

```cpp
// Wrong
if (a == b)

// Correct
const double EPS = 1e-9;
if (abs(a - b) < EPS)
```

### Memory Limits

Stack size limits (recursion depth):

| Language | Default Stack | Solution |
|----------|--------------|----------|
| C++ | ~1MB | Use explicit stack |
| Java | ~1MB | Increase with `-Xss` |
| Python | ~1000 calls | `sys.setrecursionlimit()` |

## Related Documentation

- **[Runner Internals](../architecture/runner-internals.md)** - Execution details
- **[Verdicts](../features/verdicts.md)** - Understanding errors
- **[Problems API](../api/problems.md)** - Problem settings
