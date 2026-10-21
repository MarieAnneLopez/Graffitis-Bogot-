from abc import ABC, abstractmethod

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
        # Encapsulamiento: atributos privados con __
        self.__latitud = latitud
        self.__longitud = longitud
        self.localidad = localidad
        self.barrio = barrio

    def obtener_coordenadas(self):
        return (self.__latitud, self.__longitud)

# Abstracción: Clase base que no se puede instanciar directamente
class ObraUrbana(ABC):
    def __init__(self, titulo, tecnica):
        self._titulo = titulo
        self._tecnica = tecnica

    @abstractmethod
    def mostrar_detalle(self):
        pass

# Herencia: Grafiti hereda de ObraUrbana
class Grafiti(ObraUrbana):
    def __init__(self, titulo, tecnica, autor, locacion, imagen_url=""):
        super().__init__(titulo, tecnica)
        self.__autor = autor # Asociación
        self.__locacion = locacion # Composición
        self.__imagen_url = imagen_url

    # Polimorfismo: Implementación específica del método abstracto
    def mostrar_detalle(self):
        return f"'{self._titulo}' ({self._tecnica}) por {self.__autor.alias}. Barrio: {self.__locacion.barrio}."

    def obtener_coordenadas(self):
        return self.__locacion.obtener_coordenadas()

    def obtener_localidad(self):
        return self.__locacion.localidad.nombre

class Catalogo:
    def __init__(self):
        self.__obras = []

    def agregar_obra(self, obra):
        self.__obras.append(obra)

    def filtrar_por_localidad(self, nombre_localidad):
        if nombre_localidad == "Todas":
            return self.__obras
        return [obra for obra in self.__obras if obra.obtener_localidad() == nombre_localidad]

# Instanciación de objetos con datos de Bogotá
catalogo_global = Catalogo()

loc_candelaria = Localidad("La Candelaria", "Centro histórico")
loc_chapinero = Localidad("Chapinero", "Zona cultural")
loc_puente_aranda = Localidad("Puente Aranda", "Distrito grafitero")

art_toxicomano = Artista("Andrés", "Toxicómano", "@toxicomano")
art_ledania = Artista("Diana", "Ledania", "@ledania")
art_ceroker = Artista("Camilo", "Ceroker", "@ceroker")

grafiti1 = Grafiti("Resistencia", "Stencil", art_toxicomano, Ubicacion(4.5980, -74.0760, loc_candelaria, "Centro"))
grafiti2 = Grafiti("Naturaleza Urbana", "Aerosol", art_ledania, Ubicacion(4.6460, -74.0620, loc_chapinero, "Pardo Rubio"))
grafiti3 = Grafiti("Color Local", "Mural", art_ceroker, Ubicacion(4.6320, -74.1130, loc_puente_aranda, "Zona Industrial"))

catalogo_global.agregar_obra(grafiti1)
catalogo_global.agregar_obra(grafiti2)
catalogo_global.agregar_obra(grafiti3)