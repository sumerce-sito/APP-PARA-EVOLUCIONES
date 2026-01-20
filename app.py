import streamlit as st
import pandas as pd
from pathlib import Path
import google.generativeai as genai
from datetime import datetime
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de la página
st.set_page_config(
    page_title="FisioApp - Evoluciones Profesionales",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    /* Fuente personalizada */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header principal */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.1rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* Tarjetas de categorías */
    .category-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        border: 1px solid rgba(102, 126, 234, 0.1);
        transition: all 0.3s ease;
    }
    
    .category-card:hover {
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.15);
        transform: translateY(-2px);
    }
    
    .category-title {
        color: #667eea;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        border-bottom: 2px solid #667eea;
        padding-bottom: 0.5rem;
    }
    
    /* Pills de selección */
    .stButton > button {
        border-radius: 25px;
        border: 1px solid rgba(102, 126, 234, 0.3);
        padding: 0.5rem 1.2rem;
        transition: all 0.2s ease;
        background: white;
        color: #333;
        font-weight: 500;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-color: transparent;
        transform: scale(1.05);
    }
    
    /* Panel lateral de selecciones */
    .selection-panel {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        min-height: 400px;
        box-shadow: inset 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Items seleccionados */
    .selected-item {
        background: white;
        padding: 0.8rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        animation: fadeIn 0.3s ease-out;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Badges de número */
    .item-number {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 50%;
        width: 28px;
        height: 28px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        font-size: 0.85rem;
        margin-right: 0.5rem;
    }
    
    /* Área de chat */
    .chat-container {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        min-height: 500px;
    }
    
    /* Mensajes del chat */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
    }
    
    .ai-message {
        background: #f8f9fa;
        color: #333;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    
    /* Botones de acción */
    .action-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    .action-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(102, 126, 234, 0.4);
    }
    
    /* Configuración de sidebar */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Success/Error messages */
    .stSuccess {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 8px;
    }
    
    .stError {
        background-color: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 1rem;
        border-radius: 8px;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar session state
if 'selected_items' not in st.session_state:
    st.session_state.selected_items = []
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'current_evolution' not in st.session_state:
    st.session_state.current_evolution = ""
if 'api_key' not in st.session_state:
    st.session_state.api_key = os.getenv('GOOGLE_API_KEY', '')

# Función para cargar datos del CSV
@st.cache_data
def load_data():
    """Carga los datos desde el CSV"""
    csv_path = Path(__file__).parent / "EJERCICIOS MODALIDADES EJERCICIOS.csv"
    
    # Datos de respaldo por si falla la carga
    fallback_data = {
        "Modalidades térmicas": ["Calor húmedo", "Parafina", "Paquete frío", "Baños con hielo", 
                                 "Ultrasonido", "Contrastes: caliente - fría", 
                                 "Hidroterapia platon Agua Caliente", 
                                 "Hidroterapia platon Agua Fría", "Infrarrojo"],
        "Modalidades mecánicas": ["Escalerilla de dedos", "Sistema de poleas", "Rueda náutica", 
                                  "Bastón", "Balonterapia", "Rollo terapéutico", "Balancín de puyas",
                                  "Balancín de puyas mano", "Disco de madera", "Disco de giros",
                                  "Ejercitador de dedos (digiflex)", "Plastilina terapéutica",
                                  "Bandas elásticas", "Pesas", "Elíptica", "Bicicleta estática",
                                  "Sistema de pedales", "Balancín de madera", "Patín de madera",
                                  "Balancín de puyas pie", "Escalera de dos pasos", "Barras paralelas",
                                  "Caminadora"],
        "Modalidades eléctricas": ["TENS", "EMS"],
        "Acondicionamiento físico y técnicas": ["Isométricos", "Isotónicos", "Resistidos (autocarga)",
                                                "Cadena cinética abierta (CCA)",
                                                "Cadena cinética cerrada (CCC)",
                                                "Marcha (Descargas de peso)", "Balanceo",
                                                "Propiocepción", "Equilibrio",
                                                "Estiramientos musculares (flexibilidad)",
                                                "Técnica de Codman", "Técnica de McKenzie",
                                                "Técnica de Williams", "Técnica de Klapp",
                                                "Otra técnica"],
        "Masoterapia e higiene postural": ["Higiene postural", "Masaje manual sedativo",
                                            "Masaje manual depletivo", "Masaje manual relajante",
                                            "Vibromasaje"],
        "Posicionamiento": ["Sedente", "Sentado", "Bípedo", "Decúbito supino", "Decúbito prono",
                           "Decúbito lateral derecho", "Decúbito lateral izquierdo",
                           "Carga unipodal", "Cuadrúpedo"],
        "Segmento corporal": ["Miembros superiores", "Miembros inferiores", "Espalda alta",
                             "Espalda media", "Espalda baja"]
    }
    
    try:
        if csv_path.exists():
            df = pd.read_csv(csv_path, sep=';', encoding='utf-8')
            data = {}
            for _, row in df.iterrows():
                category = row['categoria']
                item = row['item']
                if category not in data:
                    data[category] = []
                if item not in data[category]:
                    data[category].append(item)
            return data if data else fallback_data
        else:
            return fallback_data
    except Exception as e:
        st.warning(f"⚠️ No se pudo cargar el CSV: {e}. Usando datos de respaldo.")
        return fallback_data

def add_item(item):
    """Añade un item a la selección"""
    if item not in st.session_state.selected_items:
        st.session_state.selected_items.append(item)
        st.rerun()

def remove_item(index):
    """Elimina un item de la selección"""
    if 0 <= index < len(st.session_state.selected_items):
        st.session_state.selected_items.pop(index)
        st.rerun()

def clear_selection():
    """Limpia toda la selección"""
    st.session_state.selected_items = []
    st.rerun()

def get_selected_text():
    """Obtiene el texto formateado de la selección"""
    if not st.session_state.selected_items:
        return ""
    return "\n".join([f"{i+1}. {item}" for i, item in enumerate(st.session_state.selected_items)])

def generate_evolution_with_ai(selected_text, api_key):
    """Genera la evolución fisioterapéutica usando Gemini AI"""
    try:
        # Configurar la API de Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-flash-latest')
        
        # Prompt optimizado para generar evoluciones fisioterapéuticas
        prompt = f"""Eres un fisioterapeuta profesional experto. 

Basándote en las siguientes técnicas, ejercicios y modalidades aplicadas durante la sesión fisioterapéutica:

{selected_text}

GENERA una evolución fisioterapéutica profesional, clara y coherente que incluya:

1. Estado inicial del paciente (puedes inferirlo de las técnicas aplicadas)
2. Descripción detallada de las intervenciones realizadas
3. Respuesta del paciente durante la sesión
4. Estado del paciente al finalizar la sesión
5. Debe estar redactada en MAYÚSCULAS (como es estándar en muchas historias clínicas)
6. Debe ser un texto continuo, profesional y técnicamente correcto
7. Debe terminar con "SIN COMPLICACIONES AL TERMINAR LA SESIÓN" o una frase similar apropiada

IMPORTANTE: 
- Redacta como si fuera una nota real de evolución fisioterapéutica
- Usa terminología profesional y técnica
- Sé específico en las descripciones
- Mantén un tono profesional y objetivo
- No uses formato de lista, debe ser un párrafo continuo
"""
        
        # Generar la respuesta
        response = model.generate_content(prompt)
        
        return response.text
        
    except Exception as e:
        return f"❌ Error al generar la evolución: {str(e)}\n\nPor favor verifica tu API Key de Google AI."

# Header principal
st.markdown("""
<div class="main-header">
    <h1>🏥 FisioApp - Generador de Evoluciones</h1>
    <p>Sistema profesional para la elaboración rápida y estandarizada de evoluciones fisioterapéuticas</p>
</div>
""", unsafe_allow_html=True)

# Sidebar - Configuración
with st.sidebar:
    st.markdown("## ⚙️ Configuración")
    
    # API Key de Google AI
    st.markdown("### 🔑 API Key de Google AI")
    api_key_input = st.text_input(
        "Ingresa tu API Key",
        value=st.session_state.api_key,
        type="password",
        help="Obtén tu API key en https://makersuite.google.com/app/apikey"
    )
    
    if api_key_input != st.session_state.api_key:
        st.session_state.api_key = api_key_input
    
    if st.button("💾 Guardar API Key", use_container_width=True):
        st.success("✅ API Key guardada correctamente")
    
    st.markdown("---")
    
    # Información
    st.markdown("### 📋 Información")
    st.info("""
    **Cómo usar:**
    
    1️⃣ Selecciona ejercicios y técnicas
    
    2️⃣ Copia el texto generado
    
    3️⃣ Usa el chatbot de IA para generar la evolución
    """)
    
    st.markdown("---")
    
    # Estadísticas
    st.markdown("### 📊 Estadísticas")
    st.metric("Items seleccionados", len(st.session_state.selected_items))
    st.metric("Evoluciones generadas", len([msg for msg in st.session_state.chat_history if msg['role'] == 'assistant']))

# Tabs principales
tab1, tab2 = st.tabs(["📝 Selector de Terapias", "🤖 Generador de Evolución"])

# TAB 1: Selector de Terapias
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🎯 Selecciona las intervenciones realizadas")
        st.caption("Haz clic en los elementos para agregarlos a tu selección")
        
        # Cargar datos
        data = load_data()
        
        # Renderizar categorías
        for category, items in data.items():
            with st.expander(f"**{category}**", expanded=True):
                # Crear grid de botones
                cols = st.columns(3)
                for idx, item in enumerate(items):
                    with cols[idx % 3]:
                        if st.button(
                            item,
                            key=f"btn_{category}_{item}",
                            use_container_width=True,
                            type="secondary"
                        ):
                            add_item(item)
    
    with col2:
        st.markdown("### 📋 Tu Selección")
        
        if st.session_state.selected_items:
            # Mostrar items seleccionados
            for idx, item in enumerate(st.session_state.selected_items):
                col_item, col_remove = st.columns([4, 1])
                with col_item:
                    st.markdown(f"""
                    <div class="selected-item">
                        <span><span class="item-number">{idx + 1}</span>{item}</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col_remove:
                    if st.button("❌", key=f"remove_{idx}", help="Eliminar"):
                        remove_item(idx)
            
            st.markdown("---")
            
            # Mostrar texto para copiar
            st.markdown("#### 📄 Texto a copiar:")
            selected_text = get_selected_text()
            st.code(selected_text, language=None)
            
            # Botones de acción
            col_copy, col_clear = st.columns(2)
            with col_copy:
                if st.button("📋 Copiar Texto", use_container_width=True, type="primary"):
                    st.success("✅ Texto copiado al portapapeles")
                    st.info("💡 Ahora ve a la pestaña 'Generador de Evolución' para crear la nota fisioterapéutica")
            
            with col_clear:
                if st.button("🗑️ Limpiar Todo", use_container_width=True, type="secondary"):
                    clear_selection()
        else:
            st.info("👆 Aún no has seleccionado nada.\n\nHaz clic en los elementos de la izquierda para agregarlos.")

# TAB 2: Generador de Evolución con IA
with tab2:
    st.markdown("### 🤖 Generador Automático de Evolución Fisioterapéutica")
    
    # Verificar API Key
    if not st.session_state.api_key:
        st.warning("⚠️ Por favor configura tu API Key de Google AI en el panel lateral para usar esta funcionalidad.")
        st.markdown("""
        **Cómo obtener tu API Key:**
        
        1. Visita [Google AI Studio](https://makersuite.google.com/app/apikey)
        2. Inicia sesión con tu cuenta de Google
        3. Crea una nueva API key
        4. Copia la key y pégala en el campo de configuración del panel lateral
        """)
    else:
        # Área de generación
        col_gen1, col_gen2 = st.columns([2, 1])
        
        with col_gen1:
            st.markdown("#### 📝 Texto seleccionado:")
            if st.session_state.selected_items:
                selected_text = get_selected_text()
                st.code(selected_text, language=None)
            else:
                st.warning("⚠️ No hay items seleccionados. Ve a la pestaña 'Selector de Terapias' para seleccionar intervenciones.")
        
        with col_gen2:
            st.markdown("#### ⚡ Acción")
            if st.button("🚀 Generar Evolución con IA", use_container_width=True, type="primary", disabled=len(st.session_state.selected_items) == 0):
                if st.session_state.selected_items:
                    with st.spinner("🔄 Generando evolución fisioterapéutica..."):
                        selected_text = get_selected_text()
                        evolution = generate_evolution_with_ai(selected_text, st.session_state.api_key)
                        
                        # Guardar en historial
                        st.session_state.chat_history.append({
                            'role': 'user',
                            'content': selected_text,
                            'timestamp': datetime.now()
                        })
                        st.session_state.chat_history.append({
                            'role': 'assistant',
                            'content': evolution,
                            'timestamp': datetime.now()
                        })
                        st.session_state.current_evolution = evolution
                        st.rerun()
        
        st.markdown("---")
        
        # Mostrar evolución generada
        if st.session_state.current_evolution:
            st.markdown("#### 📄 Evolución Generada:")
            
            st.markdown(f"""
            <div class="ai-message">
                {st.session_state.current_evolution}
            </div>
            """, unsafe_allow_html=True)
            
            # Botones de acción para la evolución
            col_a1, col_a2, col_a3 = st.columns(3)
            
            with col_a1:
                if st.button("📋 Copiar Evolución", use_container_width=True):
                    st.success("✅ Evolución copiada al portapapeles")
            
            with col_a2:
                # Botón de descarga
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                st.download_button(
                    label="💾 Descargar como TXT",
                    data=st.session_state.current_evolution,
                    file_name=f"evolucion_fisio_{timestamp}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            with col_a3:
                if st.button("🔄 Nueva Evolución", use_container_width=True):
                    st.session_state.current_evolution = ""
                    st.rerun()
        
        # Historial de chat
        if len(st.session_state.chat_history) > 0:
            st.markdown("---")
            st.markdown("#### 📜 Historial de Evoluciones")
            
            with st.expander("Ver historial completo", expanded=False):
                for idx in range(0, len(st.session_state.chat_history), 2):
                    if idx + 1 < len(st.session_state.chat_history):
                        user_msg = st.session_state.chat_history[idx]
                        ai_msg = st.session_state.chat_history[idx + 1]
                        
                        st.markdown(f"**🕐 {user_msg['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}**")
                        
                        st.markdown("**Intervenciones:**")
                        st.code(user_msg['content'], language=None)
                        
                        st.markdown("**Evolución generada:**")
                        st.info(ai_msg['content'])
                        
                        st.markdown("---")
                
                if st.button("🗑️ Limpiar Historial", use_container_width=True):
                    st.session_state.chat_history = []
                    st.session_state.current_evolution = ""
                    st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>🏥 <strong>FisioApp</strong> - Sistema profesional de evoluciones fisioterapéuticas</p>
    <p style='font-size: 0.85rem;'>Desarrollado para optimizar el tiempo clínico y mejorar la calidad del registro</p>
</div>
""", unsafe_allow_html=True)
