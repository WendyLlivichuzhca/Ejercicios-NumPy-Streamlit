import streamlit as st
import numpy as np
import pandas as pd

# ============================
# 🎨 ESTILO MODERNO PROFESIONAL
# ============================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #e0f7fa 0%, #e3f2fd 100%);
    font-family: 'Poppins', sans-serif;
    color: #2b2b2b;
}
.sidebar-title {
    background: linear-gradient(135deg, #0288d1, #26c6da);
    color: white;
    padding: 1rem 1.2rem;
    border-radius: 16px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    box-shadow: 0 6px 20px rgba(0,0,0,0.2);
}
.sidebar-button {
    background: linear-gradient(135deg, #42a5f5, #26c6da);
    color: white !important;
    font-weight: 600;
    border-radius: 12px;
    border: none;
    padding: 0.8rem 1rem;
    width: 100%;
    text-align: left;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin: 0.5rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    transition: transform 0.2s, background 0.3s;
}
.sidebar-button:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg, #26c6da, #42a5f5);
}
.sidebar-button.active {
    background: linear-gradient(135deg, #ff8a65, #ff7043) !important;
    color: white !important;
    font-weight: 700;
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}
.footer {
    text-align: center;
    font-size: 0.9rem;
    color: #555;
    margin-top: 2.5rem;
    padding-top: 1rem;
    border-top: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

# ============================
# 🧭 SIDEBAR
# ============================
st.sidebar.markdown("""
<div class="sidebar-title">
📊 Tarea 4: NumPy + Pandas + Streamlit
</div>
""", unsafe_allow_html=True)

menu_options = [
    "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4",
    "Estudiantes", "Ejercicios Pandas"
]

if "menu" not in st.session_state:
    st.session_state.menu = "Ejercicio 1"

for option in menu_options:
    if st.sidebar.button(option, key=option):
        st.session_state.menu = option

menu = st.session_state.menu

# ============================
# 🧮 EJERCICIOS NUMPY
# ============================
if menu == "Ejercicio 1":
    st.subheader("📈 Ejercicio 1: Estadísticas básicas con NumPy")
    arr = np.arange(1, 101)
    st.write("Array:", arr)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Media", round(np.mean(arr), 2))
    col2.metric("Mediana", round(np.median(arr), 2))
    col3.metric("Varianza", round(np.var(arr), 2))
    col4.metric("Percentil 90", round(np.percentile(arr, 90), 2))

elif menu == "Ejercicio 2":
    st.subheader("🎲 Ejercicio 2: Matriz aleatoria 5x5")
    matriz = np.random.randn(5, 5)
    st.dataframe(pd.DataFrame(matriz))
    col1, col2 = st.columns(2)
    col1.success(f"Determinante: {np.linalg.det(matriz):.3f}")
    col2.info(f"Traza: {np.trace(matriz):.3f}")

elif menu == "Ejercicio 3":
    st.subheader("📊 Ejercicio 3: Distribución de frecuencias")
    data = np.random.randint(0, 11, 1000)
    values, counts = np.unique(data, return_counts=True)
    freq_df = pd.DataFrame({'Número': values, 'Frecuencia': counts})
    st.dataframe(freq_df)
    st.bar_chart(freq_df.set_index('Número'))

elif menu == "Ejercicio 4":
    st.subheader("⚙️ Ejercicio 4: Normalización de un vector")
    opcion = st.radio("Selecciona una opción:", ["Ingresar manualmente", "Generar aleatoriamente"])
    if opcion == "Ingresar manualmente":
        user_input = st.text_input("Introduce los valores separados por comas:", "10, 20, 30, 40, 50")
        v = np.array([float(x) for x in user_input.split(",")])
    else:
        v = np.random.randint(1, 100, 5)
        st.write("Vector generado:", v)
    normalizado = (v - np.mean(v)) / np.std(v)
    st.write("Vector normalizado:", normalizado)

# ============================
# 🎓 ESTUDIANTES
# ============================
elif menu == "Estudiantes":
    st.subheader("🎓 Gestión de Estudiantes del Ciclo")
    data = pd.read_csv("estudiantes.csv")
    df_edit = st.data_editor(data, num_rows="dynamic", use_container_width=True)
    csv = df_edit.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Descargar CSV", csv, "estudiantes_actualizado.csv", "text/csv")

# ============================
# 🐼 EJERCICIOS PANDAS
# ============================
elif menu == "Ejercicios Pandas":
    st.subheader("🐼 Ejercicios con Pandas (usando datos de estudiantes)")

    st.markdown("""
    **Ejercicio 1:** Carga el archivo `estudiantes.csv`  
    **Ejercicio 2:** Calcula el promedio de notas por materia  
    **Ejercicio 3:** Identifica y completa valores faltantes  
    **Ejercicio 4:** Crea una tabla dinámica con edad promedio y nota por materia  
    **Ejercicio 5:** Realiza un merge entre dos DataFrames (por ejemplo, estudiantes y tutores)
    """)

    st.markdown("---")

    # 1️⃣ Cargar CSV
    st.subheader("📂 1. Cargar o generar DataFrame de estudiantes")
    uploaded_file = st.file_uploader("Sube tu archivo CSV de estudiantes", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Archivo cargado correctamente")
    else:
        st.info("Usando datos de ejemplo de estudiantes...")
        df = pd.DataFrame({
            "Nombres": ["Wendy", "Erick", "Sebastián", "Kenny", "Adriana", "Edwin"],
            "Apellidos": ["Llivichuzhca", "Torres", "Pérez", "Mora", "Rojas", "Vera"],
            "Edad": [22, 23, 21, 22, 23, 24],
            "Materia": ["IA", "Big Data", "Redes", "Desarrollo", "Bases", "Programación"],
            "Nota": [9.5, 8.7, 9.0, 8.9, 9.3, 8.5]
        })

    st.dataframe(df.head(10))

    # 2️⃣ Promedio de notas por materia
    st.subheader("📊 2. Promedio de notas por materia")
    promedio_materia = df.groupby("Materia")["Nota"].mean().sort_values(ascending=False)
    st.bar_chart(promedio_materia)
    st.dataframe(promedio_materia)

   # 3️⃣ Manejo de valores faltantes
st.subheader("🧠 3. Imputación de valores faltantes")

# Contar valores faltantes
faltantes = df.isnull().sum()
st.write("Valores faltantes por columna:")
st.write(faltantes)

# Reemplazar valores faltantes:
# - Columnas numéricas → promedio
# - Columnas de texto → "Desconocido"
for col in df.columns:
    if df[col].dtype in ["float64", "int64"]:
        df[col].fillna(df[col].mean(), inplace=True)
    else:
        df[col].fillna("Desconocido", inplace=True)

    st.success("✅ Todos los valores faltantes han sido reemplazados automáticamente")
    st.dataframe(df)


    # 4️⃣ Tabla dinámica
    st.subheader("📅 4. Tabla dinámica: Edad y Nota promedio por materia")
    pivot = df.pivot_table(values=["Edad", "Nota"], index="Materia", aggfunc="mean")
    st.dataframe(pivot)

    # 5️⃣ Merge de DataFrames
    st.subheader("🔗 5. Merge entre DataFrames (Ejemplo)")
    tutores = pd.DataFrame({
        "Materia": ["IA", "Big Data", "Redes", "Desarrollo", "Bases", "Programación"],
        "Tutor": ["Carlos", "María", "José", "Ana", "Luis", "Sofía"]
    })
    merged = pd.merge(df, tutores, on="Materia", how="left")
    st.dataframe(merged)


# ============================
# FOOTER
# ============================
st.markdown("""
<div class="footer">
    Desarrollado con ❤️ por <b>Wendy Llivichuzhca</b><br>
    Instituto Universitario Tecnológico del Azuay — Octubre 2025
</div>
""", unsafe_allow_html=True)
