"""
Script de verificación para FisioApp
Verifica que todas las dependencias estén instaladas correctamente
"""
import sys
import os
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("="*60)
print("  🏥 FISIOAPP - VERIFICACIÓN DEL SISTEMA")
print("="*60)
print()

# Verificar Python
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
    from google import genai
    print("✓ Google GenAI SDK (google-genai): Instalado")
except ImportError:
    try:
        import google.generativeai as genai
        print("✓ Google Generative AI (legacy): Instalado")
    except ImportError as e:
        print(f"✗ Error con Google GenAI SDK: {e}")

# Verificar archivos necesarios
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
    from dotenv import load_dotenv
    load_dotenv()
    key = os.getenv("GOOGLE_API_KEY", "")
    if key and not key.startswith("tu_api_key"):
        print(f"  → API Key detectada en .env: {key[:8]}...")
    else:
        print("  ⚠️ El archivo .env existe pero requiere una API Key válida")
        print("  → Obtén tu clave en https://aistudio.google.com/")
else:
    print("⚠️ Archivo .env NO encontrado")
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

