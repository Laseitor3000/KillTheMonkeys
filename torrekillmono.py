#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random


TIEMPO = 6
fin_de_juego = False

pilas = pilasengine.iniciar()
# Usar un fondo estándar
pilas.fondos.Tarde()
# Añadir un marcador
puntos = pilas.actores.Puntaje(x=230, y=200, color=pilas.colores.verde)
puntos.magnitud = 100
# Añadir el conmutador de Sonido
pilas.actores.Sonido()
# Variables y Constantes
balas_simples = pilas.actores.Bala()
monos = []
enemigos=monos
sonido_de_explosion = pilas.sonidos.cargar('explosion.wav')




# Funciones

def mono_destruido(enemigo, bala):
    # Eliminar el mono alcanzado
    enemigo.eliminar()
    bala.eliminar() 
    puntos.aumentar(1)
    # Actualizar el marcador con un efecto bonito
	    




def crear_mono():
    # Crear un enemigo nuevo
    enemigo = pilas.actores.Mono()
    # Hacer que se aparición sea con un efecto bonito
    ##la escala varíe entre 0,25 y 0,75 (Ojo con el radio de colisión)
    enemigo.escala = .3
    enemigo.radio_de_colision=15
    # Dotarle de la habilidad de que explote al ser alcanzado por un disparo
    enemigo.aprender(pilas.habilidades.PuedeExplotar)
    # Situarlo en una posición al azar, no demasiado cerca del jugador
    x = random.randrange(-320, 320)
    y = random.randrange(-240, 240)
    if x >= 0 and x <= 100:
        x = 180
    elif x <= 0 and x >= -100:
        x = -180
    if y >= 0 and y <= 100:
        y = 180
    elif y <= 0 and y >= -100:
        y = -180
    enemigo.x = x
    enemigo.y = y
    # Dotarlo de un movimiento irregular más impredecible
    tipo_interpolacion = ['lineal',
                            'aceleracion_gradual',
                            'desaceleracion_gradual',
                            'rebote_inicial',
                            'rebote_final']
    
    duracion = 1 +random.random()*4
    
    pilas.utils.interpolar(enemigo, 'x', 0, duracion)
    pilas.utils.interpolar(enemigo, 'y', 0, duracion)
    #enemigo.x = pilas.interpolar(0,tiempo,tipo=random.choice(tipo_interpolacion))
    #enemigo.y = pilas.interpolar(0, tiempo,tipo=random.choice(tipo_interpolacion))
    # Añadirlo a la lista de enemigos
    monos.append(enemigo)
    # Permitir la creación de enemigos mientras el juego esté en activo
   

    if fin_de_juego:
        return False
    else:
        return True

def cuando_colisionan(torreta,enemigos):
    enemigos.sonreir()
    torreta.eliminar()
    crendo_monos.terminar()
    pilas.actores.Menu([('GAME OVER', cuando_colisionan)])
    print "FIN DEL JUEGO"
    pilas.fondos.Espacio()






torreta = pilas.actores.Torreta(enemigos=monos, cuando_elimina_enemigo=mono_destruido)
pilas.colisiones.agregar(torreta, monos, cuando_colisionan)

crendo_monos = pilas.tareas.agregar(1, crear_mono)
#pilas.mundo.agregar_tarea(1, crear_mono) <-- sintaxis vieja


# Arrancar el juego
pilas.ejecutar()
