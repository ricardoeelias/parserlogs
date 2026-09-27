# Log Parser (parser_log_wfile.py)

Un script en Python diseñado para **analizar archivos de registro (logs)** de forma rápida y eficiente a través de la terminal. El script inspecciona el archivo .log pasado como argumento línea por línea para clasificar los tipos de mensajes y detectar posibles errores de formato en las fechas.

## 🚀 Características

* **Clasificación automática:** Cuenta y calcula el porcentaje de mensajes de tipo `INFO`, `WARNING` y `ERROR`.
* **Detección de errores de formato:** Identifica cuántas líneas no cumplen con el patrón de fecha esperado para la sección de fecha del incidente (`YYYY-MM-DD`).
* **Eficiencia en memoria:** Lee el archivo línea por línea, lo que permite procesar logs de gran tamaño sin saturar la memoria RAM.

## 📋 Prerrequisitos

* **Python 3.x** instalado en tu sistema.
* No requiere la instalación de librerías externas (utiliza módulos nativos como `os`, `re`, `sys` y `collections`).

## 🛠️ Estructura del Proyecto

Para que el script funcione correctamente, asegúrate de colocar tus archivos de log dentro de una carpeta llamada `logs/` en el mismo directorio del script:

```text
.
├── parser_log_wfile.py
└── logs/
    └── tu_archivo.log
```

## 💻 Modo de Uso

Ejecuta el script desde tu terminal pasando únicamente el **nombre del archivo** (este debe estar almacenado dentro de la carpeta `logs/`):

```bash
python parser_log_wfile.py <nombre_archivo.log>
```

### Ejemplo Práctico:

```bash
python parser_log_wfile.py messages.log
```

### Archivos incluidos para probar funcionamiento:
--- Archivos .log dentro del folder o carpeta logs/ ---
  - messages.log
  - test.log
---

**Salida esperada en consola:**
```text
--- Análisis finalizado para: logs/messages.log ---
Total de mensajes procesados: 1550
Mal formateados: 12

Desglose por tipo:
  - INFO: 1200 (77.4%)
  - WARNING: 250 (16.1%)
  - ERROR: 100 (6.5%)
```

## 📝 Formato de Log Soportado

El script busca las siguientes estructuras en cada línea:
1. **Tipo de mensaje:** Al inicio de la línea con el formato `[INFO]`, `[WARNING]` o `[ERROR]`.
2. **Fecha:** Espacio seguido de la fecha en formato ` YYYY-MM-DD - ` (ej. ` 2026-09-25 - `).

## 📄 Reflexión técnica

* **Partes sugeridas por IA:** 
1. **Librerías o bibliotecas de Python:** entre las librerías internas de Python se han utilizado os (manejo de argumentos desde línea de comandos), re (expresioner regulares) y sys y la colección Counter.
2. **Estructura de control** with dentro de la que se usarán funciones para manejo de archivos, específicamente fopen.
3. **Detección de patrones** la sentencia match de Python para contabilizar el número de mensajes INFO, WARNING y ERROR dentro del archivo de logs.
* **Se detectó e implementó** mediante la sentencia condicional if el patrón para detectar si está presente el patrón de fecha dentro de las líneas de mensajes del archivo de logs.
* **Lo aprendido:** Utilización de Copilot para ingresar prompts comoo herramienta de apoyo a la tarea de programación.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Siéntete libre de usarlo, modificarlo y distribuirlo.
