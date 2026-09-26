# Script: parser_log_wfile.py
import os
import re
import sys
from collections import Counter

# 1. Validar que se haya proporcionado el nombre del archivo como argumento
if len(sys.argv) < 2:
    print("Error: Debes proporcionar el nombre del archivo de log.")
    print("Uso: python analizar_log.py <nombre_archivo.log>")
    sys.exit(1)

# Obtener el nombre del archivo desde el primer argumento de la línea de comandos
nombre_archivo = sys.argv[1]

# Construir la ruta hacia la carpeta 'logs/'
ruta_archivo = os.path.join("logs", nombre_archivo)

# Verificar si el archivo realmente existe en la carpeta logs/
if not os.path.exists(ruta_archivo):
    print(f"Error: El archivo '{ruta_archivo}' no existe.")
    sys.exit(1)

# 2.1 Expresión regular (re) para detectar las cadenas requeridas
log_pattern = re.compile(r"^\[(INFO|ERROR|WARNING)]", re.IGNORECASE)
# 2.2 Expresión regular (re) para detectar las cadenas requeridas
date_pattern = re.compile(r"\s{1}\d{4}-\d{2}-\d{2}\s{1}-\s{1}")

conteo = Counter()
total_mensajes = 0  # Variable para el total acumulado de mensajes
total_sin_fecha = 0  # Variable para contabilizar líneas mal formateadas (sin fecha)

# 3. Lectura e inspección del archivo línea por línea
with open(ruta_archivo, "r", encoding="utf-8") as file:
    for line in file:
        # Verificar el tipo de mensaje (INFO, WARNING o ERROR) y contabilizarlo
        match = log_pattern.search(line)
        if match:
            tipo_coincidencia = match.group(1)
            conteo[tipo_coincidencia] += 1

        # Verficar y Contabilizar líneas mal formateadas (sin fecha)
        if not date_pattern.search(line):
            total_sin_fecha += 1
            
        total_mensajes += 1  # Incrementar el total de mensajes encontrados en cada iteración de nueva línea del archivo

# 4. Mostrar resultados y métricas
print(f"--- Análisis finalizado para: {ruta_archivo} ---")
print(f"Total de mensajes procesados: {total_mensajes}")
print(f"Mal formateados: {total_sin_fecha}\n")

print("Desglose por tipo:")
for tipo, cantidad in conteo.items():
    porcentaje = (cantidad / total_mensajes * 100) if total_mensajes > 0 else 0
    print(f"  - {tipo}: {cantidad} ({porcentaje:.1f}%)")