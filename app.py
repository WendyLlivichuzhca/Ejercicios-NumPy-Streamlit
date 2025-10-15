import streamlit as st
import numpy as np
import pandas as pd

# ============================
# 🎨 ESTILO MODERNO PROFESIONAL WEB
# ============================
st.markdown("""
<style>
/* Fondo general y tipografía */
body {
    background: linear-gradient(135deg, #e0f7fa 0%, #e3f2fd 100%);
    font-family: 'Poppins', sans-serif;
    color: #2b2b2b;
    padding: 0;
    margin: 0;
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

/* Botones animados tipo premium */
.sidebar-button {
    background: linear-gradient(135deg, #ff6a00, #ee0979);
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
    animation: colorShift 5s infinite alternate;
}

/* Cambio dinámico de colores gradiente */
@keyframes colorShift {
    0% { background: linear-gradient(135deg, #ff6a00, #ee0979); }
    50% { background: linear-gradient(135deg, #42a5f5, #1e88e5); }
    100% { background: linear-gradient(135deg, #ffb347, #ffcc33); }
}

/* Glow animado */
.sidebar-button::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 60%);
    opacity: 0;
    transition: all 0.5s ease;
    animation: glowPulse 2s infinite;
}
.sidebar-button:hover::before {
    opacity: 1;
}
@keyframes glowPulse {
    0% { transform: scale(0.8); opacity: 0.3; }
    50% { transform: scale(1); opacity: 0.5; }
    100% { transform: scale(0.8); opacity: 0.3; }
}

/* Efecto “levitación” al pasar el mouse */
.sidebar-button:hover {
    transform: translateY(-5px) scale(1.08);
    box-shadow: 0 12px 35px rgba(0,0,0,0.45);
}

/* Botón activo */
.sidebar-button.active {
    background: linear-gradient(135deg, #ffd700, #ff8c00) !important;
    color: #1b1b1b !important;
    font-weight: 800;
    box-shadow: 0 14px 40px rgba(0,0,0,0.5);
    transform: scale(1.1);
}

/* DataFrames y tablas */
.stDataFrame table {
    border-collapse: collapse;
    width: 100%;
}
.stDataFrame th, .stDataFrame td {
    padding: 0.5rem 0.8rem;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
.stDataFrame tr:hover {
    background-color: #f1f1f1;
}

/* Metrics */
.stMetric {
    border-radius: 12px;
    background: #ffffff;
    padding: 1rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
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
st.sidebar.markdown('<div class="sidebar-title">📊 Tarea 4: NumPy + Pandas + Streamlit</div>', unsafe_allow_html=True)

# Lista de opciones
menu_options = [
    ("📈 Ejercicio 1", "Ejercicio 1"),
    ("🎲 Ejercicio 2", "Ejercicio 2"),
    ("📊 Ejercicio 3", "Ejercicio 3"),
    ("⚙️ Ejercicio 4", "Ejercicio 4"),
    ("🎓 Estudiantes", "Estudiantes"),
    ("🐼 Ejercicios Pandas", "Ejercicios Pandas")
]

if "menu" not in st.session_state:
    st.session_state.menu = "Ejercicio 1"

# Crear botones animados en sidebar usando HTML y Markdown
for display, option in menu_options:
    active_class = "active" if st.session_state.menu == option else ""
    button_html = f'''
    <form action="/">
        <input type="hidden" name="menu" value="{option}">
        <button class="sidebar-button {active_class}" type="submit">{display}</button>
    </form>
    '''
    st.sidebar.markdown(button_html, unsafe_allow_html=True)

# Capturar la opción seleccionada
menu = st.experimental_get_query_params().get("menu", [st.session_state.menu])[0]
st.session_state.menu = menu

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

# ============================
# 🐼 EJERCICIOS PANDAS
# ============================
elif menu == "Ejercicios Pandas":
    st.subheader("🐼 Ejercicios con Pandas (usando datos de estudiantes)")

    st.subheader("📂 1. Cargar DataFrame de estudiantes")
    df = pd.read_csv("estudiantes.csv")
    st.success("✅ Archivo cargado correctamente desde el proyecto")
    st.dataframe(df.head(10))

    st.subheader("📊 2. Promedio de notas por materia")
    promedio_materia = df.groupby("Materia")["Nota"].mean().sort_values(ascending=False)
    st.bar_chart(promedio_materia)
    st.dataframe(promedio_materia)

    st.subheader("🧠 3. Imputación de valores faltantes")
    faltantes = df.isnull().sum()
    st.write("Valores faltantes por columna:")
    st.write(faltantes)
    for col in df.columns:
        if df[col].dtype in ["float64", "int64"]:
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna("Desconocido", inplace=True)
    st.success("✅ Todos los valores faltantes han sido reemplazados automáticamente")
    st.dataframe(df)

    st.subheader("📅 4. Tabla dinámica: Edad y Nota promedio por materia")
    pivot = df.pivot_table(values=["Edad", "Nota"], index="Materia", aggfunc="mean")
    st.dataframe(pivot)

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
