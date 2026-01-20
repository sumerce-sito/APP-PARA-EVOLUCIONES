# 🏥 FisioApp - Generador de Evoluciones Fisioterapéuticas

![FisioApp](https://img.shields.io/badge/FisioApp-v1.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red)

## 📋 Descripción

**FisioApp** es una aplicación web profesional diseñada para consultorios de fisioterapia que permite:

✅ **Selección rápida** de ejercicios, técnicas terapéuticas y frases clínicas mediante clics  
✅ **Organización automática** del texto en un orden lógico y clínico  
✅ **Generación inteligente** de evoluciones fisioterapéuticas usando IA (Google Gemini)  
✅ **Ahorro de tiempo** en la redacción de notas clínicas  
✅ **Estandarización** del registro fisioterapéutico  

## 🎯 Objetivo

Reducir el tiempo de redacción de evoluciones fisioterapéuticas de **15-20 minutos a menos de 2 minutos**, manteniendo la calidad profesional y consistencia del registro clínico.

## 🚀 Características

### Módulo 1: Selector de Terapias
- ✨ Interfaz intuitiva con 7 categorías de intervenciones
- 🎨 Diseño moderno y responsivo
- 📋 Selección por clics con vista previa en tiempo real
- 🗑️ Eliminación individual o limpieza total
- 📄 Generación automática de texto formateado

### Módulo 2: Generador de Evolución con IA
- 🤖 Integración con Google Gemini AI
- ✍️ Generación automática de notas profesionales
- 📜 Historial de evoluciones generadas
- 💾 Descarga de evoluciones en formato TXT
- 📋 Función de copiado al portapapeles

## 📦 Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Cuenta de Google para obtener API Key

### Paso 1: Clonar o descargar el proyecto

```bash
cd "d:/CONSULTORIO/DOCUMENTOS IMPORTANTES/APP PARA EVOLUCIONES"
```

### Paso 2: Crear entorno virtual (recomendado)

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar API Key de Google AI

1. Visita [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API key
4. Copia el archivo `.env.example` a `.env`:
   ```bash
   copy .env.example .env
   ```
5. Edita `.env` y añade tu API key:
   ```
   GOOGLE_API_KEY=tu_api_key_aqui
   ```

## 🎮 Uso

### Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Flujo de trabajo

1. **Configurar API Key** (primera vez):
   - En el panel lateral, ingresa tu Google AI API Key
   - Haz clic en "Guardar API Key"

2. **Seleccionar intervenciones** (Pestaña 1):
   - Navega por las categorías (Modalidades térmicas, mecánicas, eléctricas, etc.)
   - Haz clic en las intervenciones realizadas durante la sesión
   - Los items se agregarán al panel derecho en orden de selección
   - Puedes eliminar items individualmente o limpiar todo

3. **Generar evolución** (Pestaña 2):
   - Verifica las intervenciones seleccionadas
   - Haz clic en "🚀 Generar Evolución con IA"
   - La IA generará una nota profesional en segundos
   - Copia o descarga la evolución generada

4. **Gestionar historial**:
   - Revisa evoluciones anteriores en el historial
   - Descarga cualquier evolución como archivo TXT
   - Limpia el historial cuando lo necesites

## 📂 Estructura del proyecto

```
APP PARA EVOLUCIONES/
├── app.py                              # Aplicación principal de Streamlit
├── EJERCICIOS MODALIDADES EJERCICIOS.csv  # Base de datos de intervenciones
├── EVOLUCIONES.txt                     # Ejemplos de evoluciones
├── index.html                          # Versión HTML original (legacy)
├── requirements.txt                    # Dependencias de Python
├── .env.example                        # Ejemplo de configuración
├── .env                                # Configuración real (no subir a Git)
└── README.md                           # Este archivo
```

## 🎨 Categorías de Intervenciones

La aplicación incluye las siguientes categorías:

1. **Modalidades térmicas**: Calor húmedo, parafina, crioterapia, etc.
2. **Modalidades mecánicas**: Poleas, bandas elásticas, pesas, equipos, etc.
3. **Modalidades eléctricas**: TENS, EMS
4. **Acondicionamiento físico y técnicas**: Ejercicios terapéuticos, técnicas especiales
5. **Masoterapia e higiene postural**: Masajes terapéuticos, educación postural
6. **Posicionamiento**: Posiciones para intervención
7. **Segmento corporal**: Áreas anatómicas tratadas

## 🔧 Personalización

### Agregar nuevas intervenciones

Edita el archivo `EJERCICIOS MODALIDADES EJERCICIOS.csv`:

```csv
categoria;item
Modalidades térmicas;Nueva modalidad térmica
Acondicionamiento físico y técnicas;Nuevo ejercicio
```

### Modificar el prompt de IA

En `app.py`, busca la función `generate_evolution_with_ai()` y modifica el `prompt` según tus necesidades específicas.

## 🐛 Solución de problemas

### Error: "No se pudo cargar el CSV"
- Verifica que el archivo `EJERCICIOS MODALIDADES EJERCICIOS.csv` existe
- Verifica que está en formato UTF-8
- La app usará datos de respaldo automáticamente

### Error: "Error al generar la evolución"
- Verifica que tu API Key de Google AI es correcta
- Verifica tu conexión a internet
- Asegúrate de que la API Key tiene permisos activos

### La aplicación no se ejecuta
- Verifica que instalaste todas las dependencias: `pip install -r requirements.txt`
- Verifica tu versión de Python: `python --version` (debe ser 3.8+)

## 📊 Ventajas de FisioApp

| Aspecto | Método Tradicional | Con FisioApp |
|---------|-------------------|--------------|
| ⏱️ **Tiempo por evolución** | 15-20 minutos | 1-2 minutos |
| 📝 **Consistencia** | Variable | Estandarizada |
| 🎯 **Calidad técnica** | Depende del profesional | Siempre profesional |
| 📋 **Formato** | Manual | Automático |
| 💾 **Registro** | Disperso | Centralizado |

## 🔐 Seguridad y Privacidad

- ⚠️ **No subas tu archivo `.env` a repositorios públicos**
- 🔒 Tu API Key es personal y confidencial
- 💾 Los datos de pacientes no se almacenan en la nube (solo localmente)
- 🌐 Las consultas a la IA son encriptadas (HTTPS)

## 📈 Roadmap

Funcionalidades planeadas para futuras versiones:

- [ ] Base de datos de pacientes
- [ ] Plantillas personalizables
- [ ] Exportación a PDF
- [ ] Integración con sistemas de historia clínica (HCE)
- [ ] Modo offline con modelos locales
- [ ] Autenticación de usuarios
- [ ] Reportes y estadísticas
- [ ] Aplicación móvil

## 🤝 Contribuciones

Este es un proyecto privado para uso interno del consultorio. Si deseas sugerir mejoras, contacta al administrador.

## 📄 Licencia

Uso privado - Consultorio de Fisioterapia

## 👨‍⚕️ Soporte

Para soporte o consultas sobre la aplicación, contacta al equipo de desarrollo.

---

**Desarrollado con ❤️ para profesionales de la fisioterapia**

FisioApp v1.0 - 2026
