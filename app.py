import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from modelos import catalogo_global

st.set_page_config(page_title="Grafitis Bogotá - Fucsia", page_icon="💖", layout="wide")

# CSS avanzado para estilos fucsia, anulación de opacidad y animación de brillitos/mascotas
st.markdown("""
    <style>
    .stApp {
        background-color: #ffcce6;
    }
    section[data-testid="stSidebar"] {
        background-color: #ff80bf;
        border-right: 4px solid #ff007f;
    }
    h1, h2, h3 {
        font-family: 'Segoe UI', sans-serif;
        color: #b30059 !important;
        font-weight: 800;
        text-shadow: 1px 1px 2px #ff99cc;
    }
    p, label, span {
        font-family: 'Segoe UI', sans-serif;
        color: #4d0026 !important;
        font-weight: 600;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff;
        border-radius: 15px;
        border: 3px solid #ff007f;
    }
    div.element-container, iframe, .stFolium {
        opacity: 1 !important;
        filter: none !important;
        transition: none !important;
    }
    iframe {
        border-radius: 25px;
        border: 5px solid #ff007f;
        box-shadow: 0 0 25px rgba(255, 0, 127, 0.6);
    }
    
    /* Animación mágica de caída libre */
    @keyframes lluviaMagica {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 0.9; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }
    .magia {
        position: fixed;
        top: -10%;
        z-index: 9999;
        pointer-events: none; /* Evita que estorben al dar clic en el mapa */
        animation: lluviaMagica linear infinite;
    }
    </style>
    
    <!-- Inyección de elementos visuales flotantes -->
    <div class="magia" style="left: 5%; font-size: 25px; animation-duration: 8s; animation-delay: 0s;">✨</div>
    <div class="magia" style="left: 15%; font-size: 30px; animation-duration: 12s; animation-delay: 2s;">🐱</div>
    <div class="magia" style="left: 25%; font-size: 20px; animation-duration: 9s; animation-delay: 4s;">🌸</div>
    <div class="magia" style="left: 35%; font-size: 35px; animation-duration: 15s; animation-delay: 1s;">🐶</div>
    <div class="magia" style="left: 50%; font-size: 28px; animation-duration: 11s; animation-delay: 5s;">💖</div>
    <div class="magia" style="left: 65%; font-size: 22px; animation-duration: 10s; animation-delay: 3s;">✨</div>
    <div class="magia" style="left: 75%; font-size: 32px; animation-duration: 14s; animation-delay: 0.5s;">🐱</div>
    <div class="magia" style="left: 85%; font-size: 26px; animation-duration: 13s; animation-delay: 6s;">🌸</div>
    <div class="magia" style="left: 95%; font-size: 24px; animation-duration: 9s; animation-delay: 2.5s;">🐶</div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>💖 Censo Masivo de Arte Urbano - Bogotá 💖</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem;'>✨ Visualización espacial con 2,500 puntos optimizados ✨</p>", unsafe_allow_html=True)
st.divider()

with st.sidebar:
    st.markdown("### 🌸 Panel de Control")
    st.markdown("💗 *Filtrar Localidad* 💗")
    
    todas_obras = catalogo_global.filtrar_por_localidad("Todas")
    localidades_unicas = sorted(list(set(obra.obtener_localidad() for obra in todas_obras)))
    
    localidades = ["Todas"] + localidades_unicas
    localidad_seleccionada = st.selectbox("Elige una localidad:", localidades)

obras_filtradas = catalogo_global.filtrar_por_localidad(localidad_seleccionada)

st.markdown(f"### 🌷 Se muestran **{len(obras_filtradas)}** puntos georreferenciados con estilo vibrante 💕")

mapa_bogota = folium.Map(
    location=[4.6097, -74.0817], 
    zoom_start=11
)

cluster = MarkerCluster(
    disableClusteringAtZoom=16,
    spiderfyOnMaxZoom=True
).add_to(mapa_bogota)

for obra in obras_filtradas:
    lat, lon = obra.obtener_coordenadas()
    autor = obra.obtener_autor()
    
    texto_popup = f"""
    <div style='font-family:sans-serif; background-color: #ffe6f2; padding: 12px; border-radius: 12px; border: 2px solid #ff007f;'>
        <b style='color: #b30059; font-size: 14px;'>💖 {obra._titulo}</b><br>
        🌸 <b>Autor:</b> {autor.alias}<br>
        🌷 <b>Técnica:</b> {obra._tecnica}
    </div>
    """
    
    icono_vibrante = folium.Icon(color="pink", icon="heart", prefix="fa")
    
    folium.Marker(
        [lat, lon], 
        popup=texto_popup,
        tooltip=f"💖 {obra._titulo}",
        icon=icono_vibrante
    ).add_to(cluster)

st_folium(mapa_bogota, use_container_width=True, height=750, returned_objects=[])