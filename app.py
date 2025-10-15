import streamlit as st
import numpy as np
import pandas as pd
import io

# ==========================
# 🎨 ESTILO PERSONALIZADO
# ==========================
st.set_page_config(page_title="Ejercicios NumPy + Pandas", page_icon="📊", layout="wide")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f0f4f8, #e0f7fa);
    color: #333;
    font-family: 'Poppins', sans-serif;
}
header {
    text-align: center;
    padding: 20px 0;
}
h1, h2, h3 {
    color: #00796b;
    text-align: center;
}
section {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 30px;
}
button, .stDownloadButton>button {
    background: linear-gradient(135deg, #00bfa5, #00796b);
    color: white;
    border-radius: 10px;
    border: none;
    padding: 8px 20px;
    transition: 0.3s ease-in-out;
}
button:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg, #00796b, #004d40);
}
footer {
    text-align: center;
    padding: 15px;
    font-size: 12px;
    color: #555;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# 🧭 NAVEGACIÓN
# ==========================
st.title("📊 Aplicación Interactiva NumPy + Pandas")
st.markdown("### Desarrollado por: **Wendy Llivichuzhca** 💚")

menu = st.sidebar.radio("Selecciona una sección:", ["Ejercicios NumPy", "Ejercicios Pandas", "Gestión de Estudiantes"])

# ==========================
# 🔹 EJERCICIOS NUMPY
# ==========================
if menu == "Ejercicios NumPy":
    st.header("🧮 Ejercicios con NumPy")
    opcion = st.selectbox("Selecciona un ejercicio:", ["Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

    if opcion == "Ejercicio 1":
        st.subheader("Array del 1 al 100 y medidas estadísticas")
        arr = np.arange(1, 101)
        st.write("📈 Array:", arr)
        st.metric("Media", f"{np.mean(arr):.2f}")
        st.metric("Mediana", f"{np.median(arr):.2f}")
        st.metric("Varianza", f"{np.var(arr):.2f}")
        st.metric("Percentil 90", f"{np.percentile(arr, 90):.2f}")

    elif opcion == "Ejercicio 2":
        st.subheader("Matriz Aleatoria 5x5 (Normal estándar)")
        mat = np.random.randn(5, 5)
        st.dataframe(pd.DataFrame(mat))
        st.success(f"Determinante: {np.linalg.det(mat):.4f}")
        st.info(f"Traza: {np.trace(mat):.4f}")

    elif opcion == "Ejercicio 3":
        st.subheader("Distribución de Frecuencias")
        nums = np.random.randint(0, 11, 1000)
        valores, frec = np.unique(nums, return_counts=True)
        df = pd.DataFrame({'Número': valores, 'Frecuencia': frec})
        st.dataframe(df)
        st.bar_chart(df.set_index("Número"))

    elif opcion == "Ejercicio 4":
        st.subheader("Normalización de un Vector")
        tipo = st.radio("Selecciona modo de entrada:", ["Manual", "Aleatorio"])
        if tipo == "Manual":
            entrada = st.text_input("Ingrese los valores separados por coma (ej: 2,4,6,8):")
            if entrada:
                v = np.array([float(x) for x in entrada.split(",")])
        else:
            v = np.random.randint(1, 100, 10)
            st.write("Vector generado:", v)
        if 'v' in locals():
            normalizado = (v - np.mean(v)) / np.std(v)
            st.write("✅ Vector normalizado:", normalizado)

# ==========================
# 🧩 EJERCICIOS PANDAS
# ==========================
elif menu == "Ejercicios Pandas":
    st.header("🐼 Ejercicios con Pandas")

    ejercicio = st.selectbox("Selecciona un ejercicio:", [
        "1️⃣ Cargar CSV y mostrar primeras 10 filas",
        "2️⃣ Venta total por producto",
        "3️⃣ Valores faltantes e imputación",
        "4️⃣ Tabla dinámica (ventas por mes y producto)",
        "5️⃣ Merge entre DataFrames"
    ])

    if ejercicio == "1️⃣ Cargar CSV y mostrar primeras 10 filas":
        archivo = st.file_uploader("Sube un archivo CSV", type="csv")
        if archivo:
            df = pd.read_csv(archivo)
            st.success("Archivo cargado correctamente ✅")
            st.dataframe(df.head(10))
        else:
            st.info("📂 Sube un archivo para iniciar el análisis.")

    elif ejercicio == "2️⃣ Venta total por producto":
        st.write("Generando datos de ejemplo...")
        df = pd.DataFrame({
            'producto': ['A', 'B', 'C', 'A', 'B', 'C'],
            'ventas': [100, 200, 150, 130, 220, 180]
        })
        st.dataframe(df)
        ventas_totales = df.groupby('producto')['ventas'].sum().sort_values(ascending=False)
        st.subheader("📊 Ventas Totales por Producto")
        st.dataframe(ventas_totales)
        st.bar_chart(ventas_totales)

    elif ejercicio == "3️⃣ Valores faltantes e imputación":
        df = pd.DataFrame({
            'Producto': ['A', 'B', 'C', 'D'],
            'Precio': [10, np.nan, 15, np.nan],
            'Ventas': [200, 150, np.nan, 180]
        })
        st.write("Datos originales:")
        st.dataframe(df)
        metodo = st.radio("Método de imputación:", ["Media", "Mediana", "Moda"])
        for col in df.select_dtypes(include=[np.number]).columns:
            if metodo == "Media":
                df[col].fillna(df[col].mean(), inplace=True)
            elif metodo == "Mediana":
                df[col].fillna(df[col].median(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
        st.success("✅ Datos imputados:")
        st.dataframe(df)

    elif ejercicio == "4️⃣ Tabla dinámica (ventas por mes y producto)":
        df = pd.DataFrame({
            'Producto': ['A', 'B', 'A', 'C', 'B', 'C'],
            'Mes': ['Enero', 'Enero', 'Febrero', 'Febrero', 'Marzo', 'Marzo'],
            'Ventas': [120, 150, 180, 200, 170, 210]
        })
        st.write("Datos base:")
        st.dataframe(df)
        tabla = pd.pivot_table(df, values='Ventas', index='Producto', columns='Mes', aggfunc='sum')
        st.subheader("📈 Tabla dinámica:")
        st.dataframe(tabla)

    elif ejercicio == "5️⃣ Merge entre DataFrames":
        productos = pd.DataFrame({
            'id': [1, 2, 3],
            'producto': ['A', 'B', 'C']
        })
        ventas = pd.DataFrame({
            'id': [1, 2, 3],
            'ventas': [100, 200, 150]
        })
        st.write("Productos:")
        st.dataframe(productos)
        st.write("Ventas:")
        st.dataframe(ventas)
        merged = pd.merge(productos, ventas, on='id')
        st.success("✅ Resultado del Merge:")
        st.dataframe(merged)

# ==========================
# 👥 GESTIÓN DE ESTUDIANTES
# ==========================
elif menu == "Gestión de Estudiantes":
    st.header("🎓 Gestión de Estudiantes del Ciclo")
    st.markdown("Puedes editar los datos y descargar el archivo CSV.")

    data = {
        "Nombres": ["Erick", "Edwin", "Adriana", "Kenny", "Maura", "Stalyn"] + [""] * 12,
        "Apellidos": ["Chacón", "Choez", "Cornejo", "Valdivieso", "Calle", "Pesantez"] + [""] * 12,
        "Edad": [21, 22, 21, 23, 22, 21] + [""] * 12,
        "Materias": ["IA", "Bases de Datos", "Redes", "Programación", "Análisis", "Diseño"] + [""] * 12,
        "Notas": [18, 16, 19, 17, 20, 15] + [""] * 12
    }

    df = pd.DataFrame(data)
    df_edit = st.data_editor(df, num_rows="dynamic")

    csv = df_edit.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descargar CSV", data=csv, file_name="estudiantes.csv", mime="text/csv")

# ==========================
# 📍 FOOTER
# ==========================
st.markdown("""
<footer>
Desarrollado por <b>Wendy Llivichuzhca</b> · Instituto Universitario Tecnológico del Azuay 🏫<br>
Curso: <i>Inteligencia Artificial</i> · Docente: Ing. Jessica Pinos
</footer>
""", unsafe_allow_html=True)
