import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Presentación - Fernando Celestino Vargas",
    page_icon="👋",
    layout="centered"
)

# Encabezado principal
st.title("👋 ¡Hola! Soy Fernando Celestino Vargas")
st.markdown("---")

# Sección: Introducción
st.subheader("🌟 Sobre mí")
st.write("""
Soy **Fernando Celestino Vargas**, apasionado por la tecnología y el aprendizaje constante.  
Me interesa el desarrollo de software, la innovación digital y las soluciones basadas en Inteligencia Artificial.
""")

# Sección: Intereses
st.subheader("🎯 Mis intereses")
st.write("""
- Desarrollo de aplicaciones modernas  
- Inteligencia Artificial y Machine Learning  
- Soluciones que ayuden a las personas en su vida diaria  
""")

# Sección: Mensaje personal
st.info("✨ Mi objetivo es crecer cada día como profesional y aportar valor con la tecnología.")

# Sección de contacto
st.subheader("📫 Contacto")
st.write("Puedes comunicarte conmigo en:")
st.markdown("- ✉️ Email: fernando.celestino@example.com")
st.markdown("- 🌐 GitHub: [fcelestinovargas](https://github.com/fcelestinovargas)")

# Pie de página
st.markdown("---")
st.caption("Página de presentación creada con ❤️ en Streamlit")
