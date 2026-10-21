# Especificación del Visor de Grafitis de Bogotá

## 1. Objetivo y Alcance
Desarrollar una aplicación web interactiva basada en Programación Orientada a Objetos (POO) en Python para visualizar, filtrar y ubicar arte urbano en Bogotá. Se usará Streamlit para la interfaz y Folium para el mapeo geoespacial.

## 2. Requisitos Funcionales
* **Catálogo de Grafitis:** El sistema debe almacenar una colección de obras de arte urbano.
* **Filtrado Dinámico:** El usuario podrá filtrar las obras por localidad (ej. La Candelaria, Teusaquillo) o por técnica (ej. Mural, Stencil).
* **Detalle de la Obra:** El sistema mostrará la información de cada grafiti: título, artista, técnica, historia y fotografía.
* **Geolocalización:** El sistema desplegará un mapa interactivo con marcadores exactos de los grafitis filtrados.

## 3. Requisitos No Funcionales
* La arquitectura interna debe basarse estrictamente en POO (clases, encapsulamiento, polimorfismo y herencia).
* La interfaz gráfica se ejecutará localmente en el navegador mediante Streamlit.
* Los datos iniciales se cargarán desde la memoria en objetos de Python (datos en crudo para simulación).

## 4. Lista de Tareas (Roadmap)
- [ ] 1. Diseñar el diagrama de clases POO.
- [ ] 2. Implementar las clases base (Grafiti, Artista, Ubicacion).
- [ ] 3. Instanciar el catálogo con datos reales de Bogotá.
- [ ] 4. Construir la interfaz de usuario web y aplicar filtros.
- [ ] 5. Integrar la renderización del mapa.