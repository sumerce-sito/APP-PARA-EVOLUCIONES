import google.generativeai as genai

# API Key actualizada
api_key = "AIzaSyAC0_Sler1c43IBE_0dXGehys85GKTgXjs"

print(f"API Key: {api_key[:15]}...")

# Configurar API
genai.configure(api_key=api_key)

print("\n=== Probando modelos actuales ===\n")

# Probar con los modelos ACTUALES disponibles
test_models = [
    'gemini-flash-latest',
    'gemini-pro-latest',
    'gemini-2.5-flash-preview-09-2025',
]

working_model = None
for model_name in test_models:
    try:
        print(f"Probando: {model_name}...")
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Di solo 'OK' como respuesta")
        print(f"✅ {model_name}: FUNCIONA")
        print(f"   Respuesta: {response.text}\n")
        working_model = model_name
        break  # Si funciona, salir del loop
    except Exception as e:
        print(f"❌ {model_name}: {str(e)[:150]}\n")

if working_model:
    print(f"🎉 Modelo recomendado para usar en app.py: '{working_model}'")
else:
    print("❌ Ningún modelo funcionó. Verifica tu API Key.")
