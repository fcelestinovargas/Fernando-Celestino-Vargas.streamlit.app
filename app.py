import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Ecuaciones de 1er grado", page_icon="🧮", layout="centered")

st.title("🧮 Resolver ecuaciones de primer grado")
st.markdown("Resuelve la ecuación y escribe tu respuesta (solo enteros).")

# --- Generar ecuación aleatoria ---
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 9)
    st.session_state.b = random.randint(-10, 10)
    st.session_state.x = random.randint(-10, 10)
    st.session_state.c = st.session_state.a * st.session_state.x + st.session_state.b

ecuacion = f"{st.session_state.a}x + {st.session_state.b} = {st.session_state.c}"
st.subheader(f"Ecuación: {ecuacion}")

# --- Campo para respuesta del usuario ---
respuesta = st.number_input("Tu respuesta para x:", step=1, format="%d")

# --- Botón para verificar ---
if st.button("Verificar"):
    if respuesta == st.session_state.x:
        st.success("✅ ¡Correcto!")
        st.balloons()
        # Generar nueva ecuación
        st.session_state.a = random.randint(1, 9)
        st.session_state.b = random.randint(-10, 10)
        st.session_state.x = random.randint(-10, 10)
        st.session_state.c = st.session_state.a * st.session_state.x + st.session_state.b
    else:
        st.error("❌ Incorrecto. Intenta de nuevo.")
