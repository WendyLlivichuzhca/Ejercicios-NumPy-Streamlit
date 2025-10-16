import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# ============================
# 🎨 ESTILO MODERNO WEB PREMIUM
# ============================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #e0f7fa 0%, #e3f2fd 100%);
    font-family: 'Poppins', sans-serif;
    color: #2b2b2b;
    margin: 0;
    padding: 0;
}
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
@keyframes colorShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
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
.sidebar-button:hover::before { opacity: 1; }
@keyframes glowPulse {
    0% { transform: scale(0.8); opacity: 0.3; }
    50% { transform: scale(1); opacity: 0.5; }
    100% { transform: scale(0.8); opacity: 0.3; }
}
.sidebar-button:hover {
    transform: translateY(-6px) scale(1.1);
    box-shadow: 0 16px 50px rgba(255,105,180,0.6), 0 8px 20px rgba(0,0,0,0.25);
}
.sidebar-button:active::after {
    content: "";
    position: absolute;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    width: 100px;
    height: 100px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0);
    animation: ripple 0.6s linear;
}
@keyframes ripple { to { transform: translate(-50%, -50%) scale(4); opacity: 0; } }
.sidebar-button.active {
    background: linear-gradient(135deg, #ffd700, #ff8c00) !important;
    color: #1b1b1b !important;
    font-weight: 800;
    box-shadow: 0 14px 40px rgba(0,0,0,0.5);
    transform: scale(1.12);
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
# SIDEBAR PRINCIPAL
# ============================
st.sidebar.markdown("""
<div class="sidebar-title">
📊 Tarea 4: NumPy + Pandas + Streamlit
</div>
""", unsafe_allow_html=True)

# Menú principal de categorías
categoria = st.sidebar.selectbox("Selecciona categoría", ["NumPy", "Pandas", "Matplotlib", "Plotly"])

# ============================
# EJERCICIOS NUMPY
# ============================
if categoria == "NumPy":
    st.sidebar.markdown("### 📚 Ejercicios (NumPy)")
    menu_numpy = st.sidebar.selectbox("Selecciona un ejercicio", ["Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4","Estudiantes"])

    if menu_numpy == "Ejercicio 1":
        st.subheader("📈 Ejercicio 1: Estadísticas básicas con NumPy")
        arr = np.arange(1, 101)
        st.write("Array:", arr)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Media", round(np.mean(arr), 2))
        col2.metric("Mediana", round(np.median(arr), 2))
        col3.metric("Varianza", round(np.var(arr), 2))
        col4.metric("Percentil 90", round(np.percentile(arr, 90), 2))

    elif menu_numpy == "Ejercicio 2":
        st.subheader("🎲 Ejercicio 2: Matriz aleatoria 5x5")
        matriz = np.random.randn(5, 5)
        st.dataframe(pd.DataFrame(matriz))
        col1, col2 = st.columns(2)
        col1.success(f"Determinante: {np.linalg.det(matriz):.3f}")
        col2.info(f"Traza: {np.trace(matriz):.3f}")

    elif menu_numpy == "Ejercicio 3":
        st.subheader("📊 Ejercicio 3: Distribución de frecuencias")
        data = np.random.randint(0, 11, 1000)
        values, counts = np.unique(data, return_counts=True)
        freq_df = pd.DataFrame({'Número': values, 'Frecuencia': counts})
        st.dataframe(freq_df)
        st.bar_chart(freq_df.set_index('Número'))

    elif menu_numpy == "Ejercicio 4":
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

    elif menu_numpy == "Estudiantes":
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
# EJERCICIOS PANDAS
# ============================
elif categoria == "Pandas":
    st.sidebar.markdown("### 🧩 Ejercicios (Pandas)")
    menu_pandas = st.sidebar.selectbox("Selecciona un ejercicio", ["Cargar csv", "Promedio de notas", "Valores Faltantes","Tabla dinamica", "Merge de dataframes"])

    try:
        df = pd.read_csv("estudiantes.csv")
    except FileNotFoundError:
        df = pd.DataFrame()  # Archivo no existe inicialmente

    if menu_pandas == "Cargar csv":
        st.subheader("📂 1. Cargar DataFrame de estudiantes")
        if not df.empty:
            st.success("✅ Archivo cargado correctamente desde el proyecto")
            st.dataframe(df.head(10))
        else:
            st.error("❌ No se encontró el archivo 'estudiantes.csv'.")

    elif menu_pandas == "Promedio de notas":
        st.subheader("📊 2. Promedio de notas por materia")
        if not df.empty:
            promedio_materia = df.groupby("Materia")["Nota"].mean().sort_values(ascending=False)
            st.bar_chart(promedio_materia)
            st.dataframe(promedio_materia)

    elif menu_pandas == "Valores Faltantes":
        st.subheader("🧠 3. Imputación de valores faltantes")
        if not df.empty:
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

    elif menu_pandas == "Tabla dinamica":
        st.subheader("📅 4. Tabla dinámica: Edad y Nota promedio por materia")
        if not df.empty:
            pivot = df.pivot_table(values=["Edad", "Nota"], index="Materia", aggfunc="mean")
            st.dataframe(pivot)

    elif menu_pandas == "Merge de dataframes":
        st.subheader("🔗 5. Merge entre DataFrames (Ejemplo)")
        if not df.empty:
            tutores = pd.DataFrame({
                "Materia": ["IA", "Big Data", "Redes", "Desarrollo", "Bases", "Programación"],
                "Tutor": ["Carlos", "María", "José", "Ana", "Luis", "Sofía"]
            })
            merged = pd.merge(df, tutores, on="Materia", how="left")
            st.dataframe(merged)

# ============================
# EJERCICIOS MATPLOTLIB
# ============================
elif categoria == "Matplotlib":
    st.sidebar.markdown("### 🧩 Ejercicios (Matplotlib)")
    menu_plot = st.sidebar.selectbox("Selecciona un ejercicio", ["Grafico de lineas", "Grafico de barras", "Boxplot de notas por materia", "Histograma de notas"])

    # Datos de ejemplo
    df = pd.DataFrame({
        "Nombres": ["Wendy", "Erick", "Sebastián", "Kenny", "Adriana", "Edwin"],
        "Materia": ["IA", "Big Data", "Redes", "Desarrollo", "Bases", "Programación"],
        "Nota": [9.5, 8.7, 9.0, 8.9, 9.3, 8.5],
        "Edad": [22, 23, 21, 22, 23, 24]
    })

    if menu_plot == "Grafico de lineas":
        st.subheader("📈 1. Evolución del promedio de notas (líneas)")
        promedio_por_estudiante = df.groupby("Nombres")["Nota"].mean()
        fig, ax = plt.subplots()
        ax.plot(promedio_por_estudiante.index, promedio_por_estudiante.values, marker='o')
        ax.set_title("Evolución del Promedio de Notas por Estudiante")
        ax.set_xlabel("Estudiante")
        ax.set_ylabel("Promedio de Nota")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    elif menu_plot == "Grafico de barras":
        st.subheader("📊 2. Top 5 materias con mejor promedio")
        promedio_materia = df.groupby("Materia")["Nota"].mean().sort_values(ascending=False).head(5)
        fig, ax = plt.subplots()
        ax.bar(promedio_materia.index, promedio_materia.values)
        ax.set_title("Top 5 Materias con Mejor Promedio")
        ax.set_xlabel("Materia")
        ax.set_ylabel("Promedio de Nota")
        plt.xticks(rotation=30)
        st.pyplot(fig)

    elif menu_plot == "Boxplot de notas por materia":
        st.subheader("📦 3. Boxplot de Notas por Materia")
        materias = df["Materia"].unique()
        data_box = [df[df["Materia"] == m]["Nota"].values for m in materias]
        fig, ax = plt.subplots()
        ax.boxplot(data_box, labels=materias)
        ax.set_title("Distribución de Notas por Materia")
        ax.set_xlabel("Materia")
        ax.set_ylabel("Nota")
        st.pyplot(fig)

    elif menu_plot == "Histograma de notas":
        st.subheader("📊 4. Histograma de distribución de notas")
        fig, ax = plt.subplots()
        ax.hist(df["Nota"], bins=10, edgecolor='black')
        ax.set_title("Distribución de Notas de Estudiantes")
        ax.set_xlabel("Nota")
        ax.set_ylabel("Frecuencia")
        st.pyplot(fig)
        st.success("✅ Ejercicios completados con datos de estudiantes")

# ============================
# EJERCICIOS PLOTLY
# ============================
elif categoria == "Plotly":
    st.sidebar.markdown("### 🧩 Ejercicios (Plotly)")
    menu_plotly = st.sidebar.selectbox("Selecciona un ejercicio", [
        "Área apilada por categoría", 
        "Treemap de categoría y producto",
        "Exportar figura a HTML"
    ])

    # ----------------------------
    # Datos base mejorados
    # ----------------------------
    fechas = pd.date_range("2025-01-01", periods=12, freq="M")
    categorias_area = ["Electrónica", "Ropa", "Alimentos", "Hogar", "Deportes"]

    # Área apilada: valores más variados
    df_area_base = pd.DataFrame({
        "Fecha": fechas,
        **{cat: np.random.randint(50, 500, 12) for cat in categorias_area}
    })

    # Treemap: categorías y productos más realistas
    productos_dict = {
        "Electrónica": ["Laptop", "Tablet", "Smartphone", "Auriculares"],
        "Ropa": ["Camisas", "Pantalones", "Zapatos", "Sombreros"],
        "Alimentos": ["Frutas", "Verduras", "Snacks", "Bebidas"],
        "Hogar": ["Muebles", "Decoración", "Electrodomésticos"],
        "Deportes": ["Pelotas", "Bicicletas", "Ropa Deportiva"]
    }

    df_treemap_base = pd.DataFrame([
        {"Categoría": cat, "Producto": prod, "Valor": np.random.randint(20, 500)}
        for cat in productos_dict
        for prod in productos_dict[cat]
    ])

    # ----------------------------
    # Área apilada por categoría
    # ----------------------------
    if menu_plotly == "Área apilada por categoría":
        st.subheader("📊 Gráfico de áreas apiladas")
        df_area = df_area_base.melt(
            id_vars=["Fecha"], 
            value_vars=categorias_area,
            var_name="Categoría", 
            value_name="Valor"
        )
        fig_area = px.area(
            df_area, 
            x="Fecha", 
            y="Valor", 
            color="Categoría",
            title="Área apilada por categoría"
        )
        st.plotly_chart(fig_area, key="area_apilada")

    # ----------------------------
    # Treemap de categoría y producto
    # ----------------------------
    elif menu_plotly == "Treemap de categoría y producto":
        st.subheader("🌍 Treemap de Categorías y Productos")
        fig_treemap = px.treemap(
            df_treemap_base,
            path=["Categoría", "Producto"],
            values="Valor",
            title="Treemap de Categorías y Productos"
        )
        st.plotly_chart(fig_treemap, key="treemap")

    # ----------------------------
    # Exportar figura a HTML
    # ----------------------------
    elif menu_plotly == "Exportar figura a HTML":
        st.subheader("💾 Exportar figura a HTML")
        df_area = df_area_base.melt(
            id_vars=["Fecha"], 
            value_vars=categorias_area,
            var_name="Categoría", 
            value_name="Valor"
        )
        fig_area_export = px.area(
            df_area, 
            x="Fecha", 
            y="Valor", 
            color="Categoría",
            title="Área apilada por categoría"
        )
        st.plotly_chart(fig_area_export, use_container_width=True, key="area_exportar")

        if st.button("📥 Generar archivo HTML"):
            import os
            with st.spinner("⏳ Generando archivo..."):
                # Crear carpeta "exportados" si no existe
                output_dir = os.path.join(os.getcwd(), "exportados")
                os.makedirs(output_dir, exist_ok=True)

                # Guardar el archivo HTML dentro de "exportados"
                html_path = os.path.join(output_dir, "grafico_plotly.html")
                fig_area_export.write_html(html_path, include_plotlyjs="cdn")
            
            st.success(f"✅ Figura exportada correctamente en: {html_path}\nAbre el archivo en tu navegador para interactuar")
# ============================
# FOOTER
# ============================
st.markdown("""
<div class="footer">
    Desarrollado con ❤️ por <b>Wendy Llivichuzhca</b><br>
    Instituto Universitario Tecnológico del Azuay — Octubre 2025
</div>
""", unsafe_allow_html=True)
