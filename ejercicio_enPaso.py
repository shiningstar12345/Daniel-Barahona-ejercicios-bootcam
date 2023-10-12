from cmu_graphics import *

def onMouseMove(x, y):
    

    app.fondo = 'negro'

Rótulo('*No a escala', 340, 370, relleno='blanco', tamaño=16)

cometa = Grupo(
        Estrella(260,160,6,6,relleno='amarillo'),
        Ovalo(260,160,10,20,relleno='marrón',opacidad=60,rotarÁngulo=-25))

cometa.agregar()       

sol = Estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))

tierra = Grupo(
    Círculo(200, 200, 150, relleno=None, borde='grisOscuro'),
    Círculo(200, 50, 15, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior'))
    )
tierra.dirección = 'sentido-horario'

mercurio = Grupo(
    Circulo(200,200,50,relleno=None,borde ='grisOscuro'),
    Circulo(200,150,5,relleno='plateado')
)
venus = Grupo(
    Circulo(200,200,100,relleno=None,borde='grisOscuro'),
    Circulo(200,100,10,relleno=gradiente('marron','gris','amarillo'))
)
marte = Grupo(
    Circulo(200,200,200,relleno=None,borde='grisOscuro'),
    Circulo(200,0,20,relleno=gradiente('carmesi','rojo'))
            
)

def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
        
    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'

def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    
    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 3
        marte.rotarÁngulo += 2
        venus.rotarÁngulo += 4
        mercurio.rotarÁngulo += 5
        cometa.centroX+=1
        cometa.centroY+=1
    else:
        tierra.rotarÁngulo -= 3
        marte.rotarÁngulo -= 2
        venus.rotarÁngulo -= 4
        mercurio.rotarÁngulo -= 5
    # Incremente el número de puntos del sol por 1.
    if cometa.centroY >= 400:
        cometa.centro=0
    sol.puntos += 1

cmu_graphics.run()