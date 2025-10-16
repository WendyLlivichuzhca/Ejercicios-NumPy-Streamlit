import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================
# 🎨 ESTILO MODERNO WEB PREMIUM
# ============================
st.markdown("""
<style>
/* Fondo general y tipografía */
body {
    background: linear-gradient(135deg, #e0f7fa 0%, #e3f2fd 100%);
    font-family: 'Poppins', sans-serif;
    color: #2b2b2b;
    margin: 0;
    padding: 0;
}

/* Sidebar */
.sidebar .sidebar-content {
    background: #ffffff;
    padding: 1rem;
    border-radius: 16px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
}

.sidebar-title {
    background: linear-gradient(135deg, #0288d1, #26c6da);
    color: white;
    padding: 1rem;
    border-radius: 12px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
}

/* Botones premium animados */
.sidebar-button {
    background: linear-gradient(270deg, #ff6a00, #ee0979, #42a5f5, #1e88e5);
    background-size: 600% 600%;
    color: white !important;
    font-weight: 700;
    border-radius: 16px;
    border: none;
    padding: 1rem 1.2rem;
    width: 100%;
    text-align: left;
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin: 0.7rem 0;
    box-shadow: 0 8px 25px rgba(0,0,0,0.35);
    cursor: pointer;
    font-size: 1.1rem;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    animation: colorShift 8s ease infinite;
}

/* Gradiente animado */
@keyframes colorShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Botón activo */
.sidebar-button.active {
    background: linear-gradient(135deg, #ffd700, #ff8c00) !important;
    color: #1b1b1b !important;
    font-weight: 800;
    box-shadow: 0 14px 40px rgba(0,0,0,0.5);
    transform: scale(1.05);
}

/* Footer */
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

# ====== CATEGORIAS ======
st.sidebar.markdown("### 📚 Ejercicios NumPy")
if st.sidebar.button("Ejercicio 1: Estadísticas básicas"):
    st.session_state["ejercicio_numpy"] = 1
if st.sidebar.button("Ejercicio 2: Matriz aleatoria"):
    st.session_state["ejercicio_numpy"] = 2
if st.sidebar.button("Ejercicio 3: Distribución de frecuencias"):
    st.session_state["ejercicio_numpy"] = 3
if st.sidebar.button("Ejercicio 4: Normalización vector"):
    st.session_state["ejercicio_numpy"] = 4
if st.sidebar.button("Gestión de Estudiantes"):
    st.session_state["ejercicio_numpy"] = 5

st.sidebar.markdown("### 🧩 Ejercicios Pandas")
if st.sidebar.button("Cargar CSV"):
    st.session_state["ejercicio_pandas"] = 1
if st.sidebar.button("Promedio de notas"):
    st.session_state["ejercicio_pandas"] = 2
if st.sidebar.button("Valores faltantes"):
    st.session_state["ejercicio_pandas"] = 3
if st.sidebar.button("Tabla dinámica"):
    st.session_state["ejercicio_pandas"] = 4
if st.sidebar.button("Merge de dataframes"):
    st.session_state["ejercicio_pandas"] = 5
if st.sidebar.button("Ejercicios Matplotlib"):
    st.session_state["ejercicio_pandas"] = 6

st.sidebar.markdown("### 🧩 Ejercicios Matplotlib")
if st.sidebar.button("Gráfico de líneas"):
    st.session_state["ejercicio_plot"] = 1
if st.sidebar.button("Gráfico de barras"):
    st.session_state["ejercicio_plot"] = 2
if st.sidebar.button("Boxplot de notas"):
    st.session_state["ejercicio_plot"] = 3
if st.sidebar.button("Histograma de notas"):
    st.session_state["ejercicio_plot"] = 4

# ============================
# FUNCIONES DE CADA EJERCICIO
# ============================
# ================= NumPy =================
ej = st.session_state.get("ejercicio_numpy", 0)
if ej == 1:
    st.subheader("📈 Ejercicio 1: Estadísticas básicas con NumPy")
    arr = np.arange(1, 101)
    st.write("Array:", arr)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Media", round(np.mean(arr), 2))
    col2.metric("Mediana", round(np.median(arr), 2))
    col3.metric("Varianza", round(np.var(arr), 2))
    col4.metric("Percentil 90", round(np.percentile(arr, 90), 2))

elif ej == 2:
    st.subheader("🎲 Ejercicio 2: Matriz aleatoria 5x5")
    matriz = np.random.randn(5, 5)
    st.dataframe(pd.DataFrame(matriz))
    col1, col2 = st.columns(2)
    col1.success(f"Determinante: {np.linalg.det(matriz):.3f}")
    col2.info(f"Traza: {np.trace(matriz):.3f}")

elif ej == 3:
    st.subheader("📊 Ejercicio 3: Distribución de frecuencias")
    data = np.random.randint(0, 11, 1000)
    values, counts = np.unique(data, return_counts=True)
    freq_df = pd.DataFrame({'Número': values, 'Frecuencia': counts})
    st.dataframe(freq_df)
    st.bar_chart(freq_df.set_index('Número'))

elif ej == 4:
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

elif ej == 5:
    st.subheader("🎓 Gestión de Estudiantes del Ciclo")
    data = {
        "Nombres": ["Wendy", "Erick", "Sebastián", "Kenny", "Adriana", "Edwin"] + [""] * 12,
        "Apellidos": ["Llivichuzhca", "Torres", "Pérez", "Mora", "Rojas", "Vera"] + [""] * 12,
        "Edad": [22, 23, 21, 22, 23, 24] + [""] * 12,
        "Materia": ["IA", "Big Data", "Redes", "Desarrollo", "Bases", "Programación"] + [""] * 12,
        "Nota": [9.5, 8.7, 9.0, 8.9, 9.3, 8.5] + [""] * 12
    }
    df = pd.DataFrame(data)
    df_edit = st.data_editor(df, num_rows="dynamic", use_container_width=True)
    csv = df_edit.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Descargar CSV", csv, "estudiantes.csv", "text/csv")

# ================= Pandas =================
ep = st.session_state.get("ejercicio_pandas", 0)
if ep == 1:
    st.subheader("📂 Cargar CSV")
    try:
        df = pd.read_csv("estudiantes.csv")
        st.success("✅ Archivo cargado correctamente")
        st.dataframe(df.head(10))
    except FileNotFoundError:
        st.error("❌ No se encontró el archivo 'estudiantes.csv'")

elif ep == 2:
    st.subheader("📊 Promedio de notas por materia")
    promedio_materia = df.groupby("Materia")["Nota"].mean().sort_values(ascending=False)
    st.bar_chart(promedio_materia)
    st.dataframe(promedio_materia)

elif ep == 3:
    st.subheader("🧠 Valores faltantes")
    faltantes = df.isnull().sum()
    st.write(faltantes)
    for col in df.columns:
        if df[col].dtype in ["float64", "int64"]:
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna("Desconocido", inplace=True)
    st.success("✅ Valores faltantes imputados")
    st.dataframe(df)

elif ep == 4:
    st.subheader("📅 Tabla dinámica")
    pivot = df.pivot_table(values=["Edad", "Nota"], index="Materia", aggfunc="mean")
    st.dataframe(pivot)

elif ep == 5:
    st.subheader("🔗 Merge de DataFrames")
    tutores = pd.DataFrame({
        "Materia": ["IA", "Big Data", "Redes", "Desarrollo", "Bases", "Programación"],
        "Tutor": ["Carlos", "María", "José", "Ana", "Luis", "Sofía"]
    })
    merged = pd.merge(df, tutores, on="Materia", how="left")
    st.dataframe(merged)

elif ep == 6:
    st.subheader("📈 Ejercicios Matplotlib (Datos de Estudiantes)")
    uploaded_file = st.file_uploader("Sube tu archivo CSV de estudiantes", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Archivo cargado correctamente")
    else:
        st.info("Usando datos de ejemplo...")
        df = pd.DataFrame({
            "Nombres": ["Wendy", "Erick", "Sebastián", "Kenny", "Adriana", "Edwin"],
            "Materia": ["IA", "Big Data", "Redes", "Desarrollo", "Bases", "Programación"],
            "Nota": [9.5, 8.7, 9.0, 8.9, 9.3, 8.5],
            "Edad": [22, 23, 21, 22, 23, 24]
        })
    st.dataframe(df)

# ================= Matplotlib =================
epm = st.session_state.get("ejercicio_plot", 0)
if epm == 1:
    st.subheader("📈 Gráfico de líneas")
    promedio_por_estudiante = df.groupby("Nombres")["Nota"].mean()
    fig, ax = plt.subplots()
    ax.plot(promedio_por_estudiante.index, promedio_por_estudiante.values, marker='o')
    ax.set_title("Evolución del Promedio de Notas por Estudiante")
    ax.set_xlabel("Estudiante")
    ax.set_ylabel("Promedio de Nota")
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif epm == 2:
    st.subheader("📊 Gráfico de barras")
    promedio_materia = df.groupby("Materia")["Nota"].mean().sort_values(ascending=False).head(5)
    fig, ax = plt.subplots()
    ax.bar(promedio_materia.index, promedio_materia.values)
    ax.set_title("Top 5 Materias con Mejor Promedio")
    ax.set_xlabel("Materia")
    ax.set_ylabel("Promedio de Nota")
    plt.xticks(rotation=30)
    st.pyplot(fig)

elif epm == 3:
    st.subheader("📦 Boxplot de Notas por Materia")
    materias = df["Materia"].unique()
    data_box = [df[df["Materia"] == m]["Nota"].values for m in materias]
    fig, ax = plt.subplots()
    ax.boxplot(data_box, labels=materias)
    ax.set_title("Distribución de Notas por Materia")
    ax.set_xlabel("Materia")
    ax.set_ylabel("Nota")
    st.pyplot(fig)

elif epm == 4:
    st.subheader("📊 Histograma de notas")
    fig, ax = plt.subplots()
    ax.hist(df["Nota"], bins=10, edgecolor='black')
    ax.set_title("Distribución de Notas de Estudiantes")
    ax.set_xlabel("Nota")
    ax.set_ylabel("Frecuencia")
    st.pyplot(fig)

# ============================
# FOOTER
# ============================
st.markdown("""
<div class="footer">
    Desarrollado con ❤️ por <b>Wendy Llivichuzhca</b><br>
    Instituto Universitario Tecnológico del Azuay — Octubre 2025
</div>
""", unsafe_allow_html=True)
