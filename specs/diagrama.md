# Diagrama de Clases: Visor de Grafitis

```mermaid
classDiagram
    class Artista {
        +str nombre
        +str alias
        +str red_social
        +mostrar_info() str
    }

    class Localidad {
        +str nombre
        +str descripcion
    }

    class Ubicacion {
        -float __latitud
        -float __longitud
        +Localidad localidad
        +str barrio
        +obtener_coordenadas() tuple
    }

    class ObraUrbana {
        <<abstract>>
        #str _titulo
        #str _tecnica
        +mostrar_detalle()* str
    }

    class Grafiti {
        -Artista __autor
        -Ubicacion __locacion
        -str __imagen_url
        +mostrar_detalle() str
        +obtener_coordenadas() tuple
        +obtener_autor() Artista
    }

    class Catalogo {
        -list __obras
        +agregar_obra(Grafiti)
        +filtrar_por_localidad(str) list
        +obtener_todas() list
    }

    class VisorGrafitis {
        -Catalogo __catalogo
        +iniciar_interfaz()
        -renderizar_mapa(list)
    }

    ObraUrbana <|-- Grafiti : Herencia
    Grafiti *-- Ubicacion : Composición
    Grafiti o-- Artista : Asociación
    Ubicacion --> Localidad : Conoce a
    Catalogo o-- Grafiti : Agregación
    VisorGrafitis *-- Catalogo : Composición