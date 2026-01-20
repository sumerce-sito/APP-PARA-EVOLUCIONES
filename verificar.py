"""
Script de verificación para FisioApp
Verifica que todas las dependencias estén instaladas correctamente
"""

print("="*60)
print("  🏥 FISIOAPP - VERIFICACIÓN DEL SISTEMA")
print("="*60)
print()

# Verificar Python
import sys
print(f"✓ Python versión: {sys.version.split()[0]}")

# Verificar dependencias
try:
    import streamlit as st
    print(f"✓ Streamlit versión: {st.__version__}")
except ImportError as e:
    print(f"✗ Error con Streamlit: {e}")

try:
    import pandas as pd
    print(f"✓ Pandas versión: {pd.__version__}")
except ImportError as e:
    print(f"✗ Error con Pandas: {e}")

try:
    import google.generativeai as genai
    print(f"✓ Google Generative AI: Instalado")
except ImportError as e:
    print(f"✗ Error con Google Generative AI: {e}")

# Verificar archivos necesarios
import os
from pathlib import Path

print()
print("Archivos del proyecto:")
files_to_check = [
    "app.py",
    "requirements.txt",
    "EJERCICIOS MODALIDADES EJERCICIOS.csv",
    ".env.example",
    "README.md"
]

for file in files_to_check:
    if Path(file).exists():
        print(f"✓ {file}")
    else:
        print(f"✗ {file} - NO ENCONTRADO")

# Verificar .env
print()
if Path(".env").exists():
    print("✓ Archivo .env configurado")
    print("  → Recuerda verificar que tu API Key esté correcta")
else:
    print("⚠ Archivo .env NO encontrado")
    print("  → Copia .env.example a .env y configura tu API Key")
    print("  → O ingresa la API Key desde el panel lateral de la app")

print()
print("="*60)
print("  VERIFICACIÓN COMPLETADA")
print("="*60)
print()
print("Para iniciar la aplicación, ejecuta:")
print("  streamlit run app.py")
print()
print("O haz doble clic en: start.bat")
print()
