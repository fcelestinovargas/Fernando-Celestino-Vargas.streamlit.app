import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Portafolio - fcelestinovargas",
    page_icon="🌐",
    layout="wide"
)

# Encabezado principal
st.title("🌐 Portafolio Personal")
st.markdown("### Hola, soy **fcelestinovargas** 👋")
st.write("Bienvenido a mi portafolio en **Streamlit**. Aquí encontrarás información sobre mí, mis proyectos y formas de contacto.")

st.markdown("---")

# 📌 Sección: Sobre mí
st.header("👨‍💻 Sobre mí")
col1, col2 = st.columns([1,3])

with col1:
    st.image("https://via.placeholder.com/200", caption="Tu foto aquí", width=200)

with col2:
    st.write("""
    Soy un entusiasta de la tecnología y la Inteligencia Artificial.  
    Me interesa el desarrollo de software, el análisis de datos y la creación de aplicaciones innovadoras.
    """)
    st.success("Siempre aprendiendo, siempre creando 🚀")

# 📌 Sección: Habilidades
st.header("🛠️ Habilidades")
st.write("- Python, Java, JavaScript")
st.write("- Machine Learning & Deep Learning")
st.write("- Desarrollo de APIs y aplicaciones web")
st.write("- Bases de datos SQL y NoSQL")

# 📌 Sección: Proyectos
st.header("📂 Proyectos")
st.subheader("1. 📊 Análisis de Datos")
st.write("Aplicación que procesa grandes volúmenes de datos y genera visualizaciones interactivas.")

st.subheader("2. 🤖 IA Conversacional")
st.write("Modelo de chatbot entrenado para responder preguntas de clientes en un ecommerce.")

st.subheader("3. 🌱 Agricultura Inteligente")
st.write("Sistema de predicción de cosechas usando aprendizaje automático.")

# 📌 Sección: Contacto
st.header("📫 Contacto")
st.write("Puedes encontrarme en:")
st.markdown("- [LinkedIn](https://linkedin.com)")
st.markdown("- [GitHub](https://github.com/fcelestinovargas)")
st.markdown("- [Email](mailto:tucorreo@ejemplo.com)")

st.markdown("---")
st.caption("© 2025 - Portafolio creado con ❤️ en Streamlit")
