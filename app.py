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
    st.subheader("🐼 Ejercicios con Pandas")
    st.markdown("""
    **Ejercicio 1:** Carga un CSV propio  
    **Ejercicio 2:** Calcula la venta total por producto  
    **Ejercicio 3:** Imputa valores faltantes  
    **Ejercicio 4:** Crea una tabla dinámica por mes y producto  
    **Ejercicio 5:** Realiza un merge entre dos DataFrames  
    """)

    st.markdown("---")
    uploaded_file = st.file_uploader("📂 Sube tu archivo CSV", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Archivo cargado correctamente")
    else:
        st.info("Usando datos de ejemplo...")
        df = pd.DataFrame({
            "Producto": ["A", "B", "C", "A", "B", "C"],
            "Ventas": [200, 150, np.nan, 300, 250, 400],
            "Mes": ["Enero", "Enero", "Enero", "Febrero", "Febrero", "Febrero"]
        })

    st.dataframe(df.head(10))

    if "Producto" in df.columns and "Ventas" in df.columns:
        st.subheader("💰 2. Venta total por producto")
        venta_total = df.groupby("Producto")["Ventas"].sum().sort_values(ascending=False)
        st.bar_chart(venta_total)
    else:
        st.warning("⚠️ El archivo no contiene columnas 'Producto' y 'Ventas'")

    st.subheader("🧠 3. Imputación de valores faltantes")
    df["Ventas"].fillna(df["Ventas"].median(), inplace=True)
    st.dataframe(df)

    st.subheader("📆 4. Tabla dinámica por mes y producto")
    if "Mes" in df.columns:
        pivot = df.pivot_table(values="Ventas", index="Mes", columns="Producto", aggfunc="sum")
        st.dataframe(pivot)

    st.subheader("🔗 5. Merge entre dos DataFrames")
    productos = pd.DataFrame({
        "Producto": ["A", "B", "C"],
        "Categoria": ["Electrónica", "Ropa", "Alimentos"]
    })
    merged = pd.merge(df, productos, on="Producto", how="left")
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
