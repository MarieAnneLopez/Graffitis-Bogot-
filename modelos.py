import random
from abc import ABC, abstractmethod
import streamlit as st

class Artista:
    def __init__(self, nombre, alias, red_social):
        self.nombre = nombre
        self.alias = alias
        self.red_social = red_social

class Localidad:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class Ubicacion:
    def __init__(self, latitud, longitud, localidad, barrio):
        self.__latitud = latitud
        self.__longitud = longitud
        self.localidad = localidad
        self.barrio = barrio

    def obtener_coordenadas(self):
        return (self.__latitud, self.__longitud)

class ObraUrbana(ABC):
    def __init__(self, titulo, tecnica):
        self._titulo = titulo
        self._tecnica = tecnica

    @abstractmethod
    def mostrar_detalle(self):
        pass

class Grafiti(ObraUrbana):
    def __init__(self, titulo, tecnica, autor, locacion):
        super().__init__(titulo, tecnica)
        self.__autor = autor 
        self.__locacion = locacion 

    def mostrar_detalle(self):
        return f"Técnica: {self._tecnica}. Autor: {self.__autor.alias}. Barrio: {self.__locacion.barrio}."

    def obtener_coordenadas(self):
        return self.__locacion.obtener_coordenadas()

    def obtener_localidad(self):
        return self.__locacion.localidad.nombre
    
    def obtener_autor(self):
        return self.__autor

class Catalogo:
    def __init__(self):
        self.__obras = []

    def agregar_obra(self, obra):
        self.__obras.append(obra)

    def filtrar_por_localidad(self, nombre_localidad):
        if nombre_localidad == "Todas":
            return self.__obras
        return [obra for obra in self.__obras if obra.obtener_localidad() == nombre_localidad]

@st.cache_resource
def inicializar_catalogo_masivo():
    catalogo = Catalogo()

    datos_localidades = [
        (Localidad("Usaquén", "Norte"), 4.696, -74.030),
        (Localidad("Chapinero", "Nororiente"), 4.646, -74.062),
        (Localidad("Santa Fe", "Centro Oriente"), 4.613, -74.068),
        (Localidad("San Cristóbal", "Suroriente"), 4.565, -74.083),
        (Localidad("Usme", "Sur"), 4.450, -74.116),
        (Localidad("Tunjuelito", "Sur"), 4.575, -74.136),
        (Localidad("Bosa", "Suroccidente"), 4.618, -74.190),
        (Localidad("Kennedy", "Suroccidente"), 4.630, -74.152),
        (Localidad("Fontibón", "Occidente"), 4.673, -74.143),
        (Localidad("Engativá", "Noroccidente"), 4.701, -74.113),
        (Localidad("Suba", "Noroccidente"), 4.741, -74.084),
        (Localidad("Barrios Unidos", "Nororiente"), 4.668, -74.073),
        (Localidad("Teusaquillo", "Centro"), 4.635, -74.081),
        (Localidad("Los Mártires", "Centro"), 4.605, -74.086),
        (Localidad("Antonio Nariño", "Sur"), 4.588, -74.102),
        (Localidad("Puente Aranda", "Centro Occidente"), 4.632, -74.113),
        (Localidad("La Candelaria", "Centro Histórico"), 4.596, -74.075),
        (Localidad("Rafael Uribe Uribe", "Sur"), 4.576, -74.111),
        (Localidad("Ciudad Bolívar", "Sur"), 4.536, -74.145)
    ]

    artistas_base = [Artista("N", "Toxicómano", "@tox"), Artista("N", "Ledania", "@led"), 
                     Artista("N", "Ceroker", "@cer"), Artista("N", "Guache", "@gua"), 
                     Artista("N", "Stinkfish", "@stink"), Artista("N", "Bastardilla", "@bas")]

    tecnicas_base = ["Aerosol", "Mural", "Stencil", "Paste-up", "Cartelismo", "Bomba"]
    palabras_titulo = ["Resistencia", "Selva", "Color", "Caos", "Paz", "Bogotá", "Mirada", "Ancestros", "Futuro", "Raíces"]

    for i in range(1, 2501):
        loc, base_lat, base_lon = random.choice(datos_localidades)
        lat = base_lat + random.uniform(-0.025, 0.025)
        lon = base_lon + random.uniform(-0.025, 0.025)
        
        artista = random.choice(artistas_base)
        tecnica = random.choice(tecnicas_base)
        titulo = f"{random.choice(palabras_titulo)} Urbano #{i}"
        
        obra = Grafiti(titulo, tecnica, artista, Ubicacion(lat, lon, loc, "Vía Pública"))
        catalogo.agregar_obra(obra)
        
    return catalogo

catalogo_global = inicializar_catalogo_masivo()