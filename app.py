import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# --------------------
# Configuración de la página
# --------------------
st.set_page_config(
    page_title="Presentación - Fernando Celestino Vargas",
    page_icon="👋",
    layout="centered"
)

# --------------------
# Encabezado principal
# --------------------
st.title("👋 ¡Hola! Soy Fernando Celestino Vargas")
st.markdown("---")

# --------------------
# Sección: Introducción
# --------------------
st.subheader("🌟 Sobre mí")
st.write("""
Soy **Fernando Celestino Vargas**, apasionado por la tecnología y el aprendizaje constante.  
Me interesa el desarrollo de software, la innovación digital y las soluciones basadas en Inteligencia Artificial.
""")

# --------------------
# Sección: Intereses
# --------------------
st.subheader("🎯 Mis intereses")
st.write("""
- Desarrollo de aplicaciones modernas  
- Inteligencia Artificial y Machine Learning  
- Soluciones que ayuden a las personas en su vida diaria  
""")

# --------------------
# Nueva Sección: Mini programa IA
# --------------------
st.subheader("🤖 Prueba un programa de IA")
st.write("Escribe una frase y la IA intentará clasificarla como **positiva** o **negativa**.")

# Datos de entrenamiento (muy básicos)
X = ["me gusta la IA", "odio los errores", "la IA es genial", "no me gusta fallar"]
y = ["positivo", "negativo", "positivo", "negativo"]

# Crear vectorizador y modelo
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)
modelo = MultinomialNB()
modelo.fit(X_vec, y)

# Entrada del usuario
frase = st.text_input("✍️ Escribe tu frase:")

if frase:
    frase_vec = vectorizer.transform([frase])
    pred = modelo.predict(frase_vec)[0]
    if pred == "positivo":
        st.success(f"La IA piensa que tu frase es **{pred}** 😃")
    else:
        st.error(f"La IA piensa que tu frase es **{pred}** 😡")

# --------------------
# Sección: Mensaje personal
# --------------------
st.info("✨ Mi objetivo es crecer cada día como profesional y aportar valor con la tecnología.")

# --------------------
# Sección de contacto
# --------------------
st.subheader("📫 Contacto")
st.write("Puedes comunicarte conmigo en:")
st.markdown("- 🌐 GitHub: [fcelestinovargas](https://github.com/fcelestinovargas)")

# --------------------
# Pie de página
# --------------------
st.markdown("---")
st.caption("Página de presentación creada con ❤️ en Streamlit")
