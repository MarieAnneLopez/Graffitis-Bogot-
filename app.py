import streamlit as st
import folium
from streamlit_folium import st_folium
from modelos import catalogo_global

st.set_page_config(page_title="Grafitis Bogotá", layout="wide")
st.title("Visor de Grafitis de Bogotá 🎨")

# Interfaz: Filtro lateral
localidades = ["Todas", "La Candelaria", "Chapinero", "Puente Aranda"]
localidad_seleccionada = st.sidebar.selectbox("Filtrar por localidad", localidades)

# Lógica: Obtener obras filtradas del catálogo
obras_filtradas = catalogo_global.filtrar_por_localidad(localidad_seleccionada)

# Mapa: Centrado en Bogotá
mapa_bogota = folium.Map(location=[4.6097, -74.0817], zoom_start=12)

# Itera sobre los objetos para poner los pines en el mapa
for Pobra in obras_filtradas:
    lat, lon = Pobra.obtener_coordenadas()
    folium.Marker(
        [lat, lon], 
        popup=Pobra.mostrar_detalle(),
        tooltip="Ver detalle"
    ).add_to(mapa_bogota)

# Renderiza el mapa
st_folium(mapa_bogota, width=800, height=500)

# Muestra detalles en texto
st.subheader(f"Obras en {localidad_seleccionada}:")
for Pobra in obras_filtradas:
    st.write(f"- {Pobra.mostrar_detalle()}")
    