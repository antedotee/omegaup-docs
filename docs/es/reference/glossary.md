---
title: Glosario
description: Terminología y definiciones utilizadas en omegaUp
icon: bootstrap/book
---
# Glosario

Referencia completa de términos y definiciones utilizados en toda la documentación de omegaUp y la plataforma.

---

## Términos generales

### omegaArriba
La plataforma de programación educativa que ayuda a los estudiantes a mejorar sus habilidades de programación a través de problemas de práctica, concursos y cursos.

### Problema
Un desafío de programación que consta de un planteamiento del problema, especificaciones de entrada/salida, restricciones y casos de prueba. Los problemas son la unidad central de contenido de omegaUp.

### Concurso
Una competición de programación cronometrada donde los participantes resuelven una serie de problemas. Los concursos tienen horarios de inicio y finalización definidos, reglas de puntuación y pueden incluir características como participación virtual.

### Curso
Una ruta de aprendizaje estructurada que contiene tareas con problemas, organizadas por temas. Los cursos incluyen seguimiento del progreso y plazos.

### Envío (Ejecutar)
Código enviado por un usuario para resolver un problema. Cada envío se compila, se ejecuta frente a casos de prueba y se le asigna un veredicto.

### Arena
La interfaz del concurso donde los participantes resuelven problemas durante las competiciones. Proporciona un marcador en tiempo real, un editor de código y un sistema de envío.

---

## Roles de usuario

### Concursante/Participante
Un usuario que participa en un concurso o practica problemas.

### Planteador de problemas
Un usuario que crea problemas a omegaUp. Los planteadores de problemas definen declaraciones, casos de prueba y validadores.

### Organizador del concurso
Un usuario que crea y gestiona concursos. Puede agregar problemas, administrar participantes y configurar los ajustes del concurso.

### Administrador del curso
Un usuario que administra cursos, asigna problemas, realiza un seguimiento del progreso de los estudiantes y revisa los envíos.

### Asistente de enseñanza (TA)
Un ayudante del curso que puede proporcionar revisiones de código y responder aclaraciones de los estudiantes.

### Administrador del sistema (administrador de sistemas)
Un usuario con acceso administrativo completo a la plataforma omegaUp.

---

## Términos técnicos

### Calificador
El microservicio Go que gestiona la cola de envío y coordina la evaluación. El calificador recibe envíos desde la interfaz, los asigna a los corredores y almacena los resultados.

### Corredor
Una instancia de servicio que compila y ejecuta código enviado por el usuario en un entorno limitado seguro. Varios corredores pueden operar en paralelo para manejar la carga de envío.

### Minicárcel
La zona de pruebas de Linux utilizada para la ejecución segura de código, bifurcada de Chrome OS. Proporciona aislamiento de procesos, filtrado de llamadas al sistema y límites de recursos.

### Servidor Git
El servicio que gestiona repositorios de problemas utilizando Git. Proporciona control de versiones, gestión de sucursales y servicio de contenido para problemas.

### Locutor
El servidor WebSocket que ofrece actualizaciones en tiempo real a los clientes, incluidos cambios en el marcador, notificaciones de veredictos y aclaraciones.

### DAO (objeto de acceso a datos)
Clases PHP que manejan interacciones de bases de datos. Los DAO proporcionan métodos para operaciones CRUD en tablas de bases de datos.

### VO (objeto de valor)
Clases PHP que se asignan a tablas de bases de datos. Los VO representan registros de bases de datos individuales con propiedades escritas.

### MVC (Modelo-Vista-Controlador)
El patrón arquitectónico utilizado en la aplicación PHP de omegaUp. Los controladores manejan la lógica empresarial, los DAO/VO manejan los datos y las plantillas manejan la presentación.

### Controlador
Clases PHP que implementan puntos finales API y lógica empresarial. Ubicado en `frontend/server/src/Controllers/`.

---

## Veredictos

### CA (Aceptado)
La solución produce resultados correctos para todos los casos de prueba y pasa dentro de los límites de recursos.

### PA (Parcialmente aceptado)
La solución pasa algunos, pero no todos, los casos de prueba. Se utiliza con problemas de puntuación parcial.

### WA (respuesta incorrecta)
La solución produce resultados incorrectos para uno o más casos de prueba.

### TLE (límite de tiempo excedido)
La solución superó el límite de tiempo en uno o más casos de prueba.

### MLE (límite de memoria excedido)
La solución superó el límite de memoria durante la ejecución.

### RTE (Error de tiempo de ejecución)
La solución falló durante la ejecución (por ejemplo, falla de segmentación, división por cero, desbordamiento de pila).

### CE (Error de compilación)
El código no se pudo compilar. Causas comunes: errores de sintaxis, inclusiones faltantes, discrepancias de tipos.

### JE (Error del juez)
Se produjo un error interno durante la evaluación. Normalmente indica un problema con los datos de prueba o el validador.

### OLE (límite de salida excedido)
La solución produjo demasiada producción y superó el límite permitido.

---

## Puntuación del concurso

### Estilo IOI
Modelo de puntuación donde cada caso de prueba otorga puntos parciales. La puntuación final es la suma de puntos de todos los casos de prueba.

### Estilo CIPC
Modelo de puntuación donde los problemas valen la misma puntuación (normalmente 1). Se agrega tiempo de penalización por envíos incorrectos.

### Penalización
Deducción basada en el tiempo o en la presentación en concursos estilo ICPC. Normalmente 20 minutos por envío incorrecto.

### Congelación del marcador
Periodo previo al final del concurso en el que el marcador deja de actualizarse públicamente, generando suspenso por los resultados finales.

### Concurso virtual
Simulando un concurso pasado en condiciones de tiempo originales. Permite practicar con concursos históricos.

---

## Componentes del problema

### Declaración
La descripción del problema, incluida la tarea, el formato de entrada/salida, las restricciones y los ejemplos.

### Caso de prueba
Un par de datos de entrada y resultados esperados utilizados para evaluar los envíos.

### Grupo de prueba
Una colección de casos de prueba relacionados, a menudo con puntos compartidos. Se utiliza para la puntuación de subtareas.

### Validador
Un programa que verifica el resultado de la solución, especialmente para problemas con múltiples respuestas válidas.

### Problema interactivo
Un problema donde la solución debe interactuar con un programa juez a través de E/S estándar.

### Generador
Un programa que crea casos de prueba, generalmente para entradas grandes o aleatorias.

### Subtarea
Un subconjunto de casos de prueba con restricciones específicas, que permite un crédito parcial por soluciones más simples.

---

## Configuración de problemas

### Límite de tiempo
Tiempo máximo de ejecución permitido por caso de prueba, en segundos (por ejemplo, 1,0 s, 2,0 s).

### Límite de memoria
Memoria máxima que puede utilizar la solución, en bytes o megabytes (por ejemplo, 256 MB).

### Límite de salida
El tamaño máximo de salida de la solución evita la impresión infinita.

### Tipo de validador
Cómo se compara la salida: `token-caseless`, `token-numeric`, `literal` o `custom`.

### Visibilidad del problema
Nivel de acceso: `private` (solo propietario), `public` (cualquiera) o específico del concurso.

---

## Términos de API

### Punto final
Una URL de API específica que maneja una operación particular (por ejemplo, `/api/Problem/create/`).

### Solicitar parámetro
Datos enviados a un punto final de API, ya sea en la cadena de consulta de URL o en el cuerpo de la solicitud.

### Respuesta
Datos JSON devueltos por un punto final de API, incluido el estado y los datos solicitados.

### Token de autenticación
La cookie `ouat` que identifica y autentica a los usuarios para solicitudes de API.

### Limitación de velocidad
Restricción de la frecuencia de llamadas a la API para evitar abusos. Los límites varían según el punto final.

---

## Términos de infraestructura

### Redis
Almacén de datos en memoria que se utiliza para el almacenamiento de sesiones, el almacenamiento en caché y la mensajería en tiempo real.

### ConejoMQ
Cola de mensajes utilizada para el procesamiento de tareas asincrónicas, como la generación de certificados.

### PHP-FPM
PHP FastCGI Process Manager que maneja el procesamiento de solicitudes PHP.

### Nginx
Servidor web y proxy inverso que enruta las solicitudes a los servicios backend apropiados.

### acoplador
Plataforma de contenerización utilizada para entornos de desarrollo e implementación.

---

## Términos de desarrollo

### PR (solicitud de extracción)
Un cambio de código propuesto enviado para revisión antes de fusionarse con la base de código principal.

### CI (Integración continua)
Pruebas automatizadas que se ejecutan en cada cambio de código para garantizar la calidad.

### Linter
Herramienta que verifica el código en busca de estilo y posibles errores (por ejemplo, ESLint, Psalm).

### Migración
Script de cambio de esquema de base de datos que actualiza la estructura de la base de datos.

### Accesorio
Datos de prueba utilizados para configurar un estado conocido para la prueba.

---

## Abreviaturas

| Abreviatura | Término completo |
|--------------|-----------|
| API | Interfaz de programación de aplicaciones |
| CRUD | Crear, leer, actualizar, eliminar |
| CSRF | Falsificación de solicitudes entre sitios |
| DAO | Objeto de acceso a datos |
| GSoC | Verano de código de Google |
| CIPC | Concurso Internacional de Programación Universitaria |
| IIO | Olimpiada Internacional de Informática |
| JSON | Notación de objetos JavaScript |
| JWT | Ficha web JSON |
| MVC | Modelo-Vista-Controlador |
| DESCANSO | Transferencia de Estado Representacional |
| SQL | Lenguaje de consulta estructurado |
| TLS | Seguridad de la capa de transporte |
| Voz | Objeto de valor |
| WS | WebSocket |
| XSS | Secuencias de comandos entre sitios |

---

## Documentación relacionada

- **[Descripción general de la arquitectura](../architecture/index.md)** - Arquitectura del sistema
- **[Referencia de API](../api/index.md)** - Documentación de API
- **[Veredictos](../features/verdicts.md)** - Información detallada del veredicto
- **[Guías de desarrollo](../development/index.md)** - Recursos para desarrolladores
