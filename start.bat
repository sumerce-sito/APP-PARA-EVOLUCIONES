@echo off
echo ========================================
echo   FisioApp - Iniciando aplicacion...
echo ========================================
echo.

REM Verificar si existe el entorno virtual
if not exist "venv" (
    echo [*] Creando entorno virtual...
    python -m venv venv
    echo [OK] Entorno virtual creado
    echo.
)

REM Activar entorno virtual
echo [*] Activando entorno virtual...
call venv\Scripts\activate

REM Instalar/actualizar dependencias
echo [*] Instalando dependencias...
pip install -r requirements.txt --quiet
echo [OK] Dependencias instaladas
echo.

REM Verificar archivo .env
if not exist ".env" (
    echo [!] ADVERTENCIA: No se encontro el archivo .env
    echo [!] Copia .env.example a .env y configura tu API Key
    echo.
    pause
)

REM Ejecutar aplicacion
echo ========================================
echo   Iniciando FisioApp...
echo   La aplicacion se abrira en tu navegador
echo ========================================
echo.
streamlit run app.py

pause
