from cmu_graphics import *
app.fondo = rgb(60, 60, 60)

# anillo
Círculo(200, 200, 110, relleno=None, borde='blancoFantasma', anchuraDeBorde=3, guión=(40, 1))
Círculo(200, 200, 145, relleno=None, borde='blancoFantasma', anchuraDeBorde=3, guión=(80, 1))

# rótulos de la brújula
Rótulo('N', 200, 75, relleno='blancoFantasma', tamaño=30)
Rótulo('S', 200, 325, relleno='blancoFantasma', tamaño=30)
Rótulo('W', 75, 200, relleno='blancoFantasma', tamaño=30)
Rótulo('E', 325, 200, relleno='blancoFantasma', tamaño=30)

# estrella de fondo
Estrella(200, 200, 100, 12, relleno='blancoFantasma', redondez=20)
Estrella(200, 200, 100, 12, relleno=app.fondo, redondez=10)
Estrella(200, 200, 100, 12, relleno='blancoFantasma', redondez=5)

# Crea una aguja como una línea con el finalDeFlecha igual a Verdadero.
aguja = Línea(200, 200, 200, 120, relleno='carmesí', anchuraDeLínea=8, finalDeFlecha=Verdadero)

def enRatónMovido(ratónX, ratónY):
    # Obtenga el ángulo entre el punto (200, 200) y la posición actual del cursor.
    ángulo = ánguloA(200, 200, ratónX, ratónY)

    # Use la función obtenerPuntoEnDir para obtener los valores nuevoX2, y nuevoY2 para la aguja.
    nuevoX2, nuevoY2 = obtenerPuntoEnDir(200, 200, ángulo, 80)

    # Establezca el x2 y el y2 de la aguja a los valores calculados arriba.
    aguja.x2 = nuevoX2
    aguja.y2 = nuevoY2
    if aguja.

cmu_graphics.run()