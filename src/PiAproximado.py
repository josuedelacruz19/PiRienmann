#!/usr/bin/env python
"""
Elementos de Computación
Laboratorio 01: Estimar el valor de pi mediante integración de sumas de Rienmann.

Estudiante: Josué Alfonso De la Cruz Roa - B82526

Desarrollo: Para estimar el valor de pi haciendo uso de las sumas de Rienmann para la función f(x)=4/(1+x**2) se deben tomar en cuenta varios aspectos.
Es importante recordar que una suma de Rienmann divide el área de la función en rectángulos y suma las áreas de estos.
Para el desarrollo de esta función se toman en cuenta el punto medio de cada base de estos rectángulos. Además, la función no se limita a un número fijo de rectángulos o valores fijos de extremos.
"""

#Se crea la función sumas_Rienmann, donde a es el límite inferior, b el superior y n el número de divisiones/rectángulos.
def sumas_Rienmann(a,b,n):

    #Se calcula el ancho de cada rectángulo
    ancho_rectángulo = (b-a)/n

    #Se inicia el conteo para la variable sumas_R
    sumas_R = 0

    #Se usa for para que la operación se repita en el rango 0-n,
    for i in range(n):

        #Se calcula el punto medio de cada rectángulo
        punto_medio = a + ancho_rectángulo * (i+0.5)

        #Se incluye el punto medio dentro de la función 4/(1+x**2) para calcular la altura de cada punto medio
        función_pi= 4/(1+punto_medio**2)

        #Se procede a calcular el área de cada rectángulo (base * altura) y se suman todas las áreas.
        sumas_R += función_pi * ancho_rectángulo

    #La función retorna la suma de las áreas
    return sumas_R

#Prueba de la función
print(sumas_Rienmann(0,1,100))
