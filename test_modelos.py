from modelos import Catalogo, Grafiti, Artista, Ubicacion, Localidad

def test_filtrar_localidad():
    cat = Catalogo()
    loc = Localidad("Suba", "Norte")
    art = Artista("X", "Y", "Z")
    graf = Grafiti("Prueba", "Mural", art, Ubicacion(4.7, -74.0, loc, "Prado"))
    
    cat.agregar_obra(graf)
    resultados = cat.filtrar_por_localidad("Suba")
    
    assert len(resultados) == 1
    assert resultados[0]._titulo == "Prueba"