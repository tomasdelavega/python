#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# gui.py
#
# File created by Tomás

import os
import sys
import time
import pygame

from pygame.locals import *

from clases import Elemento, Ensayo
from lib import obtener_cuadrante


def crear_ventana():
    # Ocultar puntero del ratón
    pygame.mouse.set_visible(False)
    #FULLSCREEN
    screen = pygame.display.set_mode((0, 0), FULLSCREEN)
    #screen = pygame.display.set_mode((1024, 768))
    return screen


def crear_matriz():
    matrix = pygame.Surface((670, 670))
    #pintar_lineas(matrix)
    return matrix


def pintar_lineas(screen):
    width, height = screen.get_size()
    center_x = width / 2
    center_y = height / 2
    top = pygame.draw.line(screen, pygame.Color('grey'), \
            (center_x, (center_y - 385)), \
            (center_x, (center_y - 340)), 1)
    bottom = pygame.draw.line(screen, pygame.Color('grey'), \
            (center_x, (center_y + 340)), \
            (center_x, (center_y + 385)), 1)
    left = pygame.draw.line(screen, pygame.Color('grey'), \
            ((center_x - 385), center_y), \
            ((center_x - 340), center_y), 1)
    right = pygame.draw.line(screen, pygame.Color('grey'), \
            ((center_x + 340), center_y), \
            ((center_x + 385), center_y), 1)
    pygame.display.flip()


def color_matriz(color, matrix):
    matrix.fill(pygame.Color(color))  # color surface


def color_pantalla(color, screen):
    screen.fill(pygame.Color(color))


def pintar_matriz(screen, matrix):
    width, height = screen.get_size()
    screen.blit(matrix, ((width - 670) / 2, (height - 670) / 2))


def pintar_punto_fijacion(color, matrix):
    pygame.draw.circle(matrix, pygame.Color(color), (335, 335), 5)


def pintar_pantalla(screen, matrix):
    pintar_matriz(screen, matrix)
    pygame.display.flip()
    #pygame.display.update()


def pintar_ensayo(ensayo, matrix):
    posicion
    color
    rotacion
    image
    # Función que recibe un ensayo y coloca en la matriz el outcome
    # y los distractores de dicho ensayo
    # Pintamos el outcome
    posicion = ensayo.devolver_posicion_outcome()
    color = ensayo.devolver_color_outcome()
    rotacion = ensayo.devolver_color_outcome()
    image = devolver_imagen(True, color, rotacion)
    matrix.blit(image, mapear_posicion(posicion))
    # Pintamos distractores
    for item in ensayo.devolver_distractores():
        posicion = item.devolver_posicion()
        color = item.devolver_color()
        rotacion = item.devolver_rotacion()
        image = devolver_imagen(False, color, rotacion)
        matrix.blit(image, mapear_posicion(posicion))


def devolver_imagen(t, c, r):
    # Comprobamos si la imagen a devolver es un target
    if t == True:
        if c == 'amarillo':
            if r == 90:
                image = pygame.image.load('images/ty90.png').convert()
            elif r == 270:
                image = pygame.image.load('images/ty270.png').convert()
        elif c == 'azul':
            if r == 90:
                image = pygame.image.load('images/tb90.png').convert()
            elif r == 270:
                image = pygame.image.load('images/tb270.png').convert()
        elif c == 'rojo':
            if r == 90:
                image = pygame.image.load('images/tr90.png').convert()
            elif r == 270:
                image = pygame.image.load('images/tr270.png').convert()
        elif c == 'verde':
            if r == 90:
                image = pygame.image.load('images/tg90.png').convert()
            elif r == 270:
                image = pygame.image.load('images/tg270.png').convert()
    # Distractores
    else:
        if c == 'amarillo':
            if r == 0:
                image = pygame.image.load('images/ly0.png').convert()
            elif r == 90:
                image = pygame.image.load('images/ly90.png').convert()
            elif r == 180:
                image = pygame.image.load('images/ly180.png').convert()
            elif r == 270:
                image = pygame.image.load('images/ly270.png').convert()
        elif c == 'azul':
            if r == 0:
                image = pygame.image.load('images/lb0.png').convert()
            elif r == 90:
                image = pygame.image.load('images/lb90.png').convert()
            elif r == 180:
                image = pygame.image.load('images/lb180.png').convert()
            elif r == 270:
                image = pygame.image.load('images/lb270.png').convert()
        elif c == 'rojo':
            if r == 0:
                image = pygame.image.load('images/lr0.png').convert()
            elif r == 90:
                image = pygame.image.load('images/lr90.png').convert()
            elif r == 180:
                image = pygame.image.load('images/lr180.png').convert()
            elif r == 270:
                image = pygame.image.load('images/lr270.png').convert()
        elif c == 'verde':
            if r == 0:
                image = pygame.image.load('images/lg0.png').convert()
            elif r == 90:
                image = pygame.image.load('images/lg90.png').convert()
            elif r == 180:
                image = pygame.image.load('images/lg180.png').convert()
            elif r == 270:
                image = pygame.image.load('images/lg270.png').convert()
    return image


def mapear_posicion(posicion):
    # COORDENADAS [FILA, COLUMNA]
    if posicion == 1:
        coordenada = [0, 0]
    elif posicion == 2:
        coordenada = [0, 83.75]
    elif posicion == 3:
        coordenada = [0, 167.50]
    elif posicion == 4:
        coordenada = [0, 251.25]
    elif posicion == 5:
        coordenada = [83.75, 0]
    elif posicion == 6:
        coordenada = [83.75, 83.75]
    elif posicion == 7:
        coordenada = [83.75, 167.50]
    elif posicion == 8:
        coordenada = [83.75, 251.25]
    elif posicion == 9:
        coordenada = [167.50, 0]
    elif posicion == 10:
        coordenada = [167.50, 83.75]
    elif posicion == 11:
        coordenada = [167.50, 167.50]
    elif posicion == 12:
        coordenada = [167.50, 251.25]
    elif posicion == 13:
        coordenada = [251.25, 0]
    elif posicion == 14:
        coordenada = [251.25, 83.75]
    elif posicion == 15:
        coordenada = [251.25, 167.50]
    elif posicion == 16:
        coordenada = [251.25, 251.25]
    # Segundo cuadrante
    elif posicion == 17:
        coordenada = [335, 0]
    elif posicion == 18:
        coordenada = [418.75, 0]
    elif posicion == 19:
        coordenada = [502.5, 0]
    elif posicion == 20:
        coordenada = [586.25, 0]
    elif posicion == 21:
        coordenada = [335, 83.75]
    elif posicion == 22:
        coordenada = [418.75, 83.75]
    elif posicion == 23:
        coordenada = [502.5, 83.75]
    elif posicion == 24:
        coordenada = [586.25, 83.75]
    elif posicion == 25:
        coordenada = [335, 167.50]
    elif posicion == 26:
        coordenada = [418.75, 167.50]
    elif posicion == 27:
        coordenada = [502.5, 167.50]
    elif posicion == 28:
        coordenada = [586.25, 167.50]
    elif posicion == 29:
        coordenada = [335, 251.25]
    elif posicion == 30:
        coordenada = [418.75, 251.25]
    elif posicion == 31:
        coordenada = [502.5, 251.25]
    elif posicion == 32:
        coordenada = [586.25, 251.25]
    # Tercer cuadrante
    elif posicion == 33:
        coordenada = [0, 335]
    elif posicion == 34:
        coordenada = [83.75, 335]
    elif posicion == 35:
        coordenada = [167.50, 335]
    elif posicion == 36:
        coordenada = [251.25, 335]
    elif posicion == 37:
        coordenada = [0, 418.75]
    elif posicion == 38:
        coordenada = [83.75, 418.75]
    elif posicion == 39:
        coordenada = [167.50, 418.75]
    elif posicion == 40:
        coordenada = [251.25, 418.75]
    elif posicion == 41:
        coordenada = [0, 502.5]
    elif posicion == 42:
        coordenada = [83.75, 502.5]
    elif posicion == 43:
        coordenada = [167.50, 502.5]
    elif posicion == 44:
        coordenada = [251.25, 502.5]
    elif posicion == 45:
        coordenada = [0, 586.25]
    elif posicion == 46:
        coordenada = [83.75, 586.25]
    elif posicion == 47:
        coordenada = [167.50, 586.25]
    elif posicion == 48:
        coordenada = [251.25, 586.25]
    # Cuarto cuadrante
    elif posicion == 49:
        coordenada = [335, 335]
    elif posicion == 50:
        coordenada = [335, 418.75]
    elif posicion == 51:
        coordenada = [335, 502.5]
    elif posicion == 52:
        coordenada = [335, 586.25]
    elif posicion == 53:
        coordenada = [418.75, 335]
    elif posicion == 54:
        coordenada = [418.75, 418.75]
    elif posicion == 55:
        coordenada = [418.75, 502.5]
    elif posicion == 56:
        coordenada = [418.75, 586.25]
    elif posicion == 57:
        coordenada = [502.5, 335]
    elif posicion == 58:
        coordenada = [502.5, 418.75]
    elif posicion == 59:
        coordenada = [502.5, 502.5]
    elif posicion == 60:
        coordenada = [502.5, 586.25]
    elif posicion == 61:
        coordenada = [586.25, 335]
    elif posicion == 62:
        coordenada = [586.25, 418.75]
    elif posicion == 63:
        coordenada = [586.25, 502.5]
    elif posicion == 64:
        coordenada = [586.25, 586.25]
    return coordenada


def flow(screen, matrix, ensayo, id_fase, sound_a, sound_f):
    # Log
    #print(ensayo.mostrar_ensayo())
    espera = pygame.time.Clock()
    # STATE ONE
    pintar_punto_fijacion('white', matrix)
    pintar_pantalla(screen, matrix)
    pygame.time.delay(500)

    # STATE TWO
    # Pintamos el punto de fijación de color negro
    pintar_punto_fijacion('black', matrix)
    # Creo objeto time para recoger el tiempo
    clock = pygame.time.Clock()
    # Pintamos ensayo, primero outcome y luego distractores
    if id_fase != 'incompleta':
        pos_out = ensayo.devolver_posicion_outcome()
        color = ensayo.devolver_color_outcome()
        rot_out = ensayo.devolver_rotacion_outcome()
        if id_fase == 'busqueda' or id_fase == 'practica':
            image = devolver_imagen(True, color, rot_out)
        elif id_fase == 'estandar':
            image = devolver_imagen(False, color, rot_out)
        matrix.blit(image, mapear_posicion(pos_out))
    else:
        pos_out = ensayo.devolver_posicion_outcome()
    # Pintamos distractores
    for item in ensayo.devolver_distractores():
        posicion = item.devolver_posicion()
        color = item.devolver_color()
        rotacion = item.devolver_rotacion()
        if posicion != ' ':
            image = devolver_imagen(False, color, rotacion)
            matrix.blit(image, mapear_posicion(posicion))
    # Actualizamos la pantalla
    pintar_pantalla(screen, matrix)
    # Bucle y tiempo
    # Se enciende el cronómetro
    clock.tick_busy_loop()
    pygame.event.clear()
    # Bucle para la fase de práctica y búsqueda.
    if id_fase == 'practica' or id_fase == 'busqueda':
        while 1:
            for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_z:
                            clock.tick_busy_loop()
                            ensayo.asignar_tiempo_respuesta(clock.get_time())
                            ensayo.asignar_respuesta('z')
                            if rot_out == 90:
                                ensayo.asignar_correcto(1)
                                color_matriz('black', matrix)
                                pintar_pantalla(screen, matrix)
                                sound_a.play()
                                pygame.time.delay(1000)
                                return
                            else:
                                color_matriz('black', matrix)
                                pintar_pantalla(screen, matrix)
                                sound_f.play()
                                pygame.time.delay(1000)
                                return
                        elif event.key == K_m:
                            clock.tick_busy_loop()
                            ensayo.asignar_tiempo_respuesta(clock.get_time())
                            ensayo.asignar_respuesta('m')
                            if rot_out == 270:
                                ensayo.asignar_correcto(1)
                                color_matriz('black', matrix)
                                pintar_pantalla(screen, matrix)
                                sound_a.play()
                                pygame.time.delay(1000)
                                return
                            else:
                                color_matriz('black', matrix)
                                pintar_pantalla(screen, matrix)
                                sound_f.play()
                                pygame.time.delay(1000)
                                return
    # Bucle para la fases de generación estándar e incompleta
    elif id_fase == 'estandar' or id_fase == 'incompleta':
        while 1:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Cuadrante 1, posiciones(1-16)
                    if event.key == K_q:
                        clock.tick_busy_loop()
                        ensayo.asignar_tiempo_respuesta(clock.get_time())
                        ensayo.asignar_respuesta('q')
                        if obtener_cuadrante(pos_out) == 1:
                            ensayo.asignar_correcto(1)
                        color_matriz('black', matrix)
                        pintar_pantalla(screen, matrix)
                        pygame.time.delay(1000)
                        return
                    # Cuadrante 2, posiciones(17-32)
                    elif event.key == K_o:
                        clock.tick_busy_loop()
                        ensayo.asignar_tiempo_respuesta(clock.get_time())
                        ensayo.asignar_respuesta('o')
                        if obtener_cuadrante(pos_out) == 2:
                            ensayo.asignar_correcto(1)
                        color_matriz('black', matrix)
                        pintar_pantalla(screen, matrix)
                        pygame.time.delay(1000)
                        return
                    # Cuadrante 3, posiciones(33-48)
                    elif event.key == K_s:
                        clock.tick_busy_loop()
                        ensayo.asignar_tiempo_respuesta(clock.get_time())
                        ensayo.asignar_respuesta('s')
                        if obtener_cuadrante(pos_out) == 3:
                            ensayo.asignar_correcto(1)
                        color_matriz('black', matrix)
                        pintar_pantalla(screen, matrix)
                        pygame.time.delay(1000)
                        return
                    # Cuadrante 4, posiciones(49-64)
                    elif event.key == K_k:
                        clock.tick_busy_loop()
                        ensayo.asignar_tiempo_respuesta(clock.get_time())
                        ensayo.asignar_respuesta('k')
                        if obtener_cuadrante(pos_out) == 4:
                            ensayo.asignar_correcto(1)
                        color_matriz('black', matrix)
                        pintar_pantalla(screen, matrix)
                        pygame.time.delay(1000)
                        return


# Función que muestra una pantalla de información entre bloques
def mensaje_post_bloque(screen, id_fase):
    # Poner pantalla en negro
    color_pantalla('white', screen)
    # Se puede crear dos mensajes para esta pantalla
    # Mensaje a mostrar
    if id_fase == 'busqueda':
        message = "No olvides responder lo más rápidamente posible y al mismo tiempo tratar de cometer el\nmenor número de errores posible.\n\nSi tienes alguna duda, plantéasela al experimentador antes de continuar. En caso\ncontrario, coloca los dedos sobre las teclas de respuesta igual que antes, y pulsa\nla BARRA ESPACIADORA para comenzar."
    else:
        message = "Hemos terminado este bloque.\n\nNo olvides responder guiándote por tu intución.\n\nSi tienes alguna duda, plantéasela al experimentador antes de\ncontinuar. En caso contrario, coloca los dedos sobre las teclas de respuesta igual que\nantes, y pulsa la BARRA ESPACIADORA para comenzar."
    # Definimos la fuente a utilizar, None = pygame por defecto
    fuente = pygame.font.Font(None, 25)
    #information = fuente.render(message, 0, pygame.Color('white'))
    # Obtenemos ancho y alto de la pantalla
    width, height = screen.get_size()
    # Coordenada de inicio x
    x = round(int((width - 900) / 2))
    y = round(int(height / 2) - 200)
    imprimir_texto(screen, message, x, y, pygame.Color('black'), fuente)
    # Actualizamos la pantalla
    pygame.display.flip()
    # Esperamos hasta que pulse la barra espaciadora
    # Limpiamos la cola de eventos
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_SPACE):
                    color_pantalla('black', screen)
                    pygame.display.flip()
                    return


def resultados_post_bloque(screen, bloques, longitud):
     # Pintamos la pantalla completamente de negro
    color_pantalla('white', screen)
    # Resolución de la pantalla
    width, height = screen.get_size()
    # Ancho y alto de la nueva superficie
    ancho = round(width * 0.8)
    alto = round(height * 0.8)
    # Dimensiones de las cabeceras
    columna = round(ancho / 3)
    fila = round(alto / (longitud + 2))
    # Creamos la superfice
    superficie = pygame.Surface((ancho, alto))
    superficie.fill(pygame.Color('white'))
    # Cabeceras de la tabla
    c1 = "TAREA (Búsqueda) /BLOQUE"
    c2 = "ACIERTOS (%)"
    c3 = "TIEMPO (Milisegundos)"
    # Texto informativo
     # Definimos la fuente a utilizar, None = pygame por defecto
    fuente = pygame.font.Font(None, 25)
    #info = "Presiona la tecla 'C' para pasar a la siguiente pantalla"
    if longitud != len(bloques):
        boton_continuar(screen)
        titulo = "Hemos terminado este bloque. Estos son los datos correspondientes a tu\ntiempo medio de respuesta y tu porcentaje de aciertos hasta el momento."
    else:
        titulo = "Hemos terminado esta parte de la tarea. Estos son los datos correspondientes\na tu tiempo medio de respuesta y tu porcentaje de aciertos hasta el momento."
        info = "Presiona la barra espaciadora para continuar"
        fuente_info = pygame.font.Font(None, 30)
        message = fuente_info.render(info, 0, pygame.Color('black'))
        # Creo rectángulo
        message_rect = message.get_rect()
        # Centro message
        message_rect.centerx = screen.get_rect().centerx
        center_y = height - round((height - alto) / 4)
        message_rect.centery = center_y
        # Dibujamos rectángulo en la superficie
        screen.blit(message, message_rect)
    imprimir_texto(screen, titulo, 100, 10, pygame.Color('black'), fuente)
    #fuente_info = pygame.font.Font(None, 30)
    # Creamos los objetos tipo texto
    cabecera1 = fuente.render(c1, 0, pygame.Color('black'))
    cabecera2 = fuente.render(c2, 0, pygame.Color('black'))
    cabecera3 = fuente.render(c3, 0, pygame.Color('black'))
    #mensaje = fuente_info.render(info, 0, pygame.Color('black'))
    #encabezado = fuente_info.render(titulo, 0, pygame.Color('black'))
    # Creo rectángulo para el mensaje de información
    #mensaje_rect = mensaje.get_rect()
    # Creo rectángulo para el encabezado
    #encabezado_rect = encabezado.get_rect()
    # Centro el rectángulo de información en la pantalla
    #mensaje_rect.centerx = screen.get_rect().centerx
    #center_y = height - round((height - alto) / 4)
    #mensaje_rect.centery = center_y
    # Centro el rectángulo del encabezado en la pantalla
    #encabezado_rect.centerx = screen.get_rect().centerx
    #encabezado_rect.centery = round((height - alto) / 4)
    # Dibujo el rectángulo de información en la pantalla
    #screen.blit(mensaje, mensaje_rect)
    # Dibujo el encabezado en la pantalla
    #screen.blit(encabezado, encabezado_rect)
    # Pintamos las cabeceras en la superficie
    superficie.blit(cabecera1, (0, 0))
    superficie.blit(cabecera2, (columna, 0))
    superficie.blit(cabecera3, (columna * 2, 0))
    # Nos recorremos la fase y pintamos la información de cada bloque
    promedio_aciertos = 0
    promedio_tmr = 0
    for i in range(len(bloques)):
        # Tiempo medio de respuesta
        tmr = 0
        aciertos = 0
        for item in bloques[i]:
            tmr = tmr + item.devolver_tiempo_respuesta()
            if item.devolver_correcto() == True:
                aciertos = aciertos + 1
        tmr = tmr / len(bloques[i])
        aciertos = (aciertos / len(bloques[i])) * 100
        promedio_aciertos = promedio_aciertos + aciertos
        promedio_tmr = promedio_tmr + tmr
        # Redondeo los valores
        aciertos = round(aciertos)
        tmr = round(tmr)
        promedio_aciertos = round(promedio_aciertos)
        promedio_tmr = round(promedio_tmr)
        # Objetos tipo texto
        celda1 = fuente.render(str(i + 1), 0, pygame.Color('black'))
        celda2 = fuente.render(str(aciertos), 0, pygame.Color('black'))
        celda3 = fuente.render(str(tmr), 0, pygame.Color('black'))
        # Pintamos en la superficie los resultados
        superficie.blit(celda1, (0, fila * (i + 1)))
        superficie.blit(celda2, (columna, fila * (i + 1)))
        superficie.blit(celda3, (columna * 2, fila * (i + 1)))
    # Se pinta la superficie en la pantalla y se refresca la pantalla
    screen.blit(superficie, ((width - ancho) / 2, (height - alto) / 2))
    pygame.display.flip()


def informacion_post_bloque(screen):
    # Poner pantalla en blanco
    color_pantalla('white', screen)
    # Se puede crear dos mensajes para esta pantalla
    message = "No olvides responder lo más rápidamente posible y al mismo tiempo tratar de cometer el\nmenor número de errores posible.\n\nSi tienes alguna duda, plantéasela al experimentador antes de continuar. En caso\ncontrario, coloca los dedos sobre las teclas de respuesta igual que antes, y pulsa\nla BARRA ESPACIADORA para comenzar."
    # Definimos la fuente a utilizar, None = pygame por defecto
    fuente = pygame.font.Font(None, 25)
    #information = fuente.render(message, 0, pygame.Color('white'))
    # Obtenemos ancho y alto de la pantalla
    width, height = screen.get_size()
    # Coordenada de inicio x
    x = round(int((width - 900) / 2))
    y = round(int(height / 2) - 200)
    imprimir_texto(screen, message, x, y, pygame.Color('black'), fuente)
    # Actualizamos la pantalla
    boton_atras(screen)
    pygame.display.flip()


# Pantallas de información post bloque en fase de búsqueda
def pantallas_post_bloque(screen, bloques, longitud):
    estado = 0
    cerrado = True
    # Falta llamar a la función que muestra la primera pantalla
    resultados_post_bloque(screen, bloques, longitud)
    while cerrado == True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_c):
                    if estado == 0:
                        estado = 1
                        informacion_post_bloque(screen)
                elif (event.key == K_a):
                    if estado == 1:
                        estado = 0
                        resultados_post_bloque(screen, bloques, longitud)
                elif (event.key == K_SPACE):
                    if estado == 1:
                        cerrado == False
                        return


# Fúncion que muestra los resultados de la fase de practica
def resultados_fase_practica(screen, fase):
    # Pintamos la pantalla completamente de blanco
    color_pantalla('white', screen)
    # Resolución de la pantalla
    width, height = screen.get_size()
    # Ancho y alto de la nueva superficie
    ancho = round(width * 0.8)
    alto = round(height * 0.8)
    # Dimensiones de las cabeceras
    columna = round(ancho / 3)
    fila = 50
    # Nueva superficie
    s1 = pygame.Surface((ancho, alto))
    s1.fill(pygame.Color('white'))
    # Obtenemos valores de la fase
    # tiempo medio de respuesta
    trm = 0
    # Porcentaje de aciertos
    aciertos = 0
    for item in fase:
        if item.devolver_correcto() == True:
            aciertos = aciertos + 1
        trm = trm + item.devolver_tiempo_respuesta()
    aciertos = (aciertos / len(fase)) * 100
    trm = trm / len(fase)
    # Redondeamos los datos
    aciertos = round(aciertos)
    trm = round(trm)
    # Cabeceras
    c1 = "TAREA (Práctica) / BLOQUE"
    c2 = "ACIERTOS (%)"
    c3 = "TIEMPO (Milisegundos)"
    info = "Presiona la barra espaciadora para continuar"
    titulo = "ESTOS SON TUS DATOS EN EL BLOQUE DE PRÁCTICA"
    # Definimos la fuente a utilizar, None = pygame por defecto
    fuente = pygame.font.Font(None, 25)
    fuente_info = pygame.font.Font(None, 30)
    # Objeto tipo texto
    cabecera_1 = fuente.render(c1, 0, pygame.Color('black'))
    cabecera_2 = fuente.render(c2, 0, pygame.Color('black'))
    cabecera_3 = fuente.render(c3, 0, pygame.Color('black'))
    salida1 = fuente.render('Bloque Práctica', 0, pygame.Color('black'))
    salida2 = fuente.render(str(aciertos), 0, pygame.Color('black'))
    salida3 = fuente.render(str(trm), 0, pygame.Color('black'))
    message = fuente_info.render(info, 0, pygame.Color('black'))
    encabezado = fuente_info.render(titulo, 0, pygame.Color('black'))
    # Creo rectángulo
    message_rect = message.get_rect()
    encabezado_rect = encabezado.get_rect()
    # Centro el rectángulo
    #message_rect.centerx = s1.get_rect().centerx
    #message_rect.centery = s1.get_rect().centery
    # Centro message
    message_rect.centerx = screen.get_rect().centerx
    center_y = height - round((height - alto) / 4)
    message_rect.centery = center_y
    # Centro encabezado
    encabezado_rect.centerx = screen.get_rect().centerx
    encabezado_rect.centery = round((height - alto) / 4)
    # Dibujamos sobre la superficie
    s1.blit(cabecera_1, (0, 0))
    s1.blit(cabecera_2, (columna, 0))
    s1.blit(cabecera_3, (columna * 2, 0))
    s1.blit(salida1, (0, fila))
    s1.blit(salida2, (columna, fila))
    s1.blit(salida3, (columna * 2, fila))
    screen.blit(message, message_rect)
    screen.blit(encabezado, encabezado_rect)
    screen.blit(s1, ((width - ancho) / 2, (height - alto) / 2))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_SPACE):
                    color_pantalla('black', screen)
                    pygame.display.flip()
                    return


def resultados_fase_busqueda(screen, fase):
    # Pintamos la pantalla completamente de negro
    color_pantalla('white', screen)
    # Resolución de la pantalla
    width, height = screen.get_size()
    # Ancho y alto de la nueva superficie
    ancho = round(width * 0.8)
    alto = round(height * 0.8)
    # Dimensiones de las cabeceras
    columna = round(ancho / 3)
    fila = round(alto / (len(fase) + 2))
    # Creamos la superfice
    superficie = pygame.Surface((ancho, alto))
    superficie.fill(pygame.Color('white'))
    # Cabeceras de la tabla
    c1 = "TAREA (Búsqueda) /BLOQUE"
    c2 = "ACIERTOS (%)"
    c3 = "TIEMPO (Milisegundos)"
    # Texto informativo
    #info = "Presiona la tecla 'C' para pasar a la siguiente pantalla"
    titulo = "DATOS TAREA DE BÚSQUEDA"
    # Definimos la fuente a utilizar, None = pygame por defecto
    fuente = pygame.font.Font(None, 25)
    fuente_info = pygame.font.Font(None, 30)
    # Creamos los objetos tipo texto
    cabecera1 = fuente.render(c1, 0, pygame.Color('black'))
    cabecera2 = fuente.render(c2, 0, pygame.Color('black'))
    cabecera3 = fuente.render(c3, 0, pygame.Color('black'))
    #mensaje = fuente_info.render(info, 0, pygame.Color('black'))
    encabezado = fuente_info.render(titulo, 0, pygame.Color('black'))
    # Creo rectángulo para el mensaje de información
    #mensaje_rect = mensaje.get_rect()
    # Creo rectángulo para el encabezado
    encabezado_rect = encabezado.get_rect()
    # Centro el rectángulo de información en la pantalla
    #mensaje_rect.centerx = screen.get_rect().centerx
    #center_y = height - round((height - alto) / 4)
    #mensaje_rect.centery = center_y
    # Centro el rectángulo del encabezado en la pantalla
    encabezado_rect.centerx = screen.get_rect().centerx
    encabezado_rect.centery = round((height - alto) / 4)
    # Dibujo el rectángulo de información en la pantalla
    #screen.blit(mensaje, mensaje_rect)
    # Dibujo el encabezado en la pantalla
    screen.blit(encabezado, encabezado_rect)
    # Pintamos las cabeceras en la superficie
    superficie.blit(cabecera1, (0, 0))
    superficie.blit(cabecera2, (columna, 0))
    superficie.blit(cabecera3, (columna * 2, 0))
    # Nos recorremos la fase y pintamos la información de cada bloque
    promedio_aciertos = 0
    promedio_tmr = 0
    for i in range(len(fase)):
        # Tiempo medio de respuesta
        tmr = 0
        aciertos = 0
        for item in fase[i]:
            tmr = tmr + item.devolver_tiempo_respuesta()
            if item.devolver_correcto() == True:
                aciertos = aciertos + 1
        tmr = tmr / len(fase[i])
        aciertos = (aciertos / len(fase[i])) * 100
        promedio_aciertos = promedio_aciertos + aciertos
        promedio_tmr = promedio_tmr + tmr
        # Redondeo los valores
        aciertos = round(aciertos)
        tmr = round(tmr)
        promedio_aciertos = round(promedio_aciertos)
        promedio_tmr = round(promedio_tmr)
        # Objetos tipo texto
        celda1 = fuente.render(str(i + 1), 0, pygame.Color('black'))
        celda2 = fuente.render(str(aciertos), 0, pygame.Color('black'))
        celda3 = fuente.render(str(tmr), 0, pygame.Color('black'))
        # Pintamos en la superficie los resultados
        superficie.blit(celda1, (0, fila * (i + 1)))
        superficie.blit(celda2, (columna, fila * (i + 1)))
        superficie.blit(celda3, (columna * 2, fila * (i + 1)))
    # Creamos objetos para las últimas celdas
    promedio = fuente.render('Promedio', 0, pygame.Color('black'))
    c2 = fuente.render(str(round(promedio_aciertos / len(fase))), 0, \
    pygame.Color('black'))
    c3 = fuente.render(str(round(promedio_tmr / len(fase))), 0, \
    pygame.Color('black'))
    # Pintamos en la superficie el promedio
    superficie.blit(promedio, (0, fila * (len(fase) + 1)))
    superficie.blit(c2, (columna, fila * (len(fase) + 1)))
    superficie.blit(c3, (columna * 2, fila * (len(fase) + 1)))
    # Se pinta la superficie en la pantalla y se refresca la pantalla
    screen.blit(superficie, ((width - ancho) / 2, (height - alto) / 2))
    pygame.display.flip()


# Función que devuelve una superficie con información de
# la fase de generación estándar e incompleta
def resultados_fase_generacion(screen, fase_estandar, fase_incompleta):
    # Pintamos la pantalla completamente de negro
    color_pantalla('white', screen)
    # Resolución de la pantalla
    width, height = screen.get_size()
    # Ancho y alto de la nueva superficie
    ancho = round(width * 0.8)
    alto = round(height * 0.8)
    # Dimensiones de las cabeceras
    columna = round(ancho / 3)
    fila = 100
    # Creamos la superfice
    superficie = pygame.Surface((ancho, alto))
    superficie.fill(pygame.Color('white'))
    # Cabeceras de la tabla
    c1 = "TAREA (12 'Ls')"
    c2 = "ACIERTOS (%)"
    c3 = "TIEMPO (Milisegundos)"
    # Texto informativo
    #info = "Pulsa la tecla 'A' para volver atrás y la 'C' para continuar"
    titulo = "DATOS TAREAS DE PREDICCIÓN"
    # Definimos la fuente a utilizar, None = pygame por defecto
    fuente = pygame.font.Font(None, 25)
    fuente_info = pygame.font.Font(None, 30)
     # Creamos los objetos tipo texto
    cabecera1 = fuente.render(c1, 0, pygame.Color('black'))
    cabecera2 = fuente.render(c2, 0, pygame.Color('black'))
    cabecera3 = fuente.render(c3, 0, pygame.Color('black'))
    #mensaje = fuente_info.render(info, 0, pygame.Color('black'))
    encabezado = fuente_info.render(titulo, 0, pygame.Color('black'))
    # Creo rectángulo para el mensaje de información
    #mensaje_rect = mensaje.get_rect()
    # Creo rectángulo para el encabezado
    encabezado_rect = encabezado.get_rect()
    # Centro el rectángulo de información en la pantalla
    #mensaje_rect.centerx = screen.get_rect().centerx
    #center_y = height - round((height - alto) / 4)
    #mensaje_rect.centery = center_y
    # Centro el rectángulo del encabezado
    encabezado_rect.centerx = screen.get_rect().centerx
    encabezado_rect.centery = round((height - alto) / 4)
    # Dibujo el rectángulo de información en la pantalla
    #screen.blit(mensaje, mensaje_rect)
    # Dibujo el encabezado en la pantalla
    screen.blit(encabezado, encabezado_rect)
    # Pintamos las cabeceras en la superficie
    superficie.blit(cabecera1, (0, 0))
    superficie.blit(cabecera2, (columna, 0))
    superficie.blit(cabecera3, (columna * 2, 0))
    # Recorremos la fase estándar
    aciertos = 0
    tmr = 0
    numero_bloques = len(fase_estandar)
    numero_ensayos = len(fase_estandar[0])
    for bloque in fase_estandar:
        for item in bloque:
            if item.devolver_correcto() == True:
                aciertos += 1
            tmr += item.devolver_tiempo_respuesta()
    aciertos = round((aciertos / (numero_bloques * numero_ensayos)) * 100)
    tmr = round(tmr / (numero_bloques * numero_ensayos))
    # Objetos tipo texto
    celda1 = fuente.render("Promedio", 0, pygame.Color('black'))
    celda2 = fuente.render(str(aciertos), 0, pygame.Color('black'))
    celda3 = fuente.render(str(tmr), 0, pygame.Color('black'))
    # Pintamos en la superficie los resultados
    superficie.blit(celda1, (0, fila))
    superficie.blit(celda2, (columna, fila))
    superficie.blit(celda3, (columna * 2, fila))
    # Ahora procesamos la fase incompleta
    c1 = "TAREA (8 'Ls')"
    # Creo objeto texto para la cabecera
    cabecera1 = fuente.render(c1, 0, pygame.Color('black'))
    # Pintamos las cabeceras en la superficie
    superficie.blit(cabecera1, (0, fila * 3))
    superficie.blit(cabecera2, (columna, fila * 3))
    superficie.blit(cabecera3, (columna * 2, fila * 3))
    # Recorre la fase incompleta
    aciertos = 0
    tmr = 0
    for bloque in fase_incompleta:
        for item in bloque:
            if item.devolver_correcto() == True:
                aciertos += 1
            tmr += item.devolver_tiempo_respuesta()
    aciertos = round((aciertos / (numero_bloques * numero_ensayos)) * 100)
    tmr = round(tmr / (numero_bloques * numero_ensayos))
    # Objetos tipo texto
    celda1 = fuente.render("Promedio", 0, pygame.Color('black'))
    celda2 = fuente.render(str(aciertos), 0, pygame.Color('black'))
    celda3 = fuente.render(str(tmr), 0, pygame.Color('black'))
    # Pintamos en la superficie los resultados
    superficie.blit(celda1, (0, fila * 4))
    superficie.blit(celda2, (columna, fila * 4))
    superficie.blit(celda3, (columna * 2, fila * 4))
    # Se pinta la superficie en la pantalla y se refresca la pantalla
    screen.blit(superficie, ((width - ancho) / 2, (height - alto) / 2))
    pygame.display.flip()


# Función que muestra los resultados de las Fases de Búsqueda y Generación
def mostrar_resultados(screen, f_b, f_g_e, f_g_i):
    # Definimos e inicializamos la variable estado
    estado = 0
    # Definimos e inicializamos la variable del bucle
    cerradura = True
    # Mostramos los resultados de la fase de Búsqueda
    resultados_fase_busqueda(screen, f_b)
    boton_continuar(screen)
    pygame.display.update()
    #print('Dentro de mostrar resultados')
    #print('State')
    # Bucle de estados
    while cerradura == True:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                # Siguiente estado
                if evento.key == K_c:
                    if estado == 1:
                        #color_pantalla('white', screen)
                        estado = 2
                        mostrar_despedida(screen)
                        boton_atras(screen)
                        pygame.display.update()
                    elif estado == 0:
                        estado = 1
                        resultados_fase_generacion(screen, f_g_e, f_g_i)
                        boton_atras(screen)
                        boton_continuar(screen)
                        pygame.display.update()
                # Estado anterior
                elif evento.key == K_a:
                    if estado == 1:
                        estado = 0
                        resultados_fase_busqueda(screen, f_b)
                        boton_continuar(screen)
                        pygame.display.update()
                    if estado == 2:
                        estado = 1
                        resultados_fase_generacion(screen, f_g_e, f_g_i)
                        boton_atras(screen)
                        boton_continuar(screen)
                        pygame.display.update()
                elif evento.key == K_ESCAPE:
                    color_pantalla('white', screen)
                    pygame.display.update()
                    cerradura = False


# Funcion que recibe una fase y la procesa
def ejecutar_fase(id_fase, fase, screen):
    # Se crea el reloj
    reloj = pygame.time.Clock()
    # Creamos la matriz
    matrix = crear_matriz()
    list_key = []
    # Definimos las teclas que van actuar en las fases
    if id_fase == 'busqueda' or id_fase == 'practica':
        list_key.append(K_z)
        list_key.append(K_m)
    elif id_fase == 'estandar' or id_fase == 'incompleta':
        list_key.append(K_q)
        list_key.append(K_o)
        list_key.append(K_s)
        list_key.append(K_k)
    # Archivos de Sonido
    acierto = pygame.mixer.Sound("audio/acierto.ogg")
    fallo = pygame.mixer.Sound("audio/fallo.ogg")
    # Pintamos pantalla en negro
    color_pantalla('black', screen)
    if id_fase == 'practica':
        # Pintar las 4 líneas en la pantalla
        pintar_lineas(screen)
        # Bucle que recorre la fase de práctica
        for item in fase:
            flow(screen, matrix, item, id_fase, acierto, fallo)
        # Se enciende el reloj
        reloj.tick_busy_loop()
        # Mostramos información tras la fase de practica
        resultados_fase_practica(screen, fase)
        # Se apaga el reloj
        reloj.tick_busy_loop()
        return reloj.get_time()
    elif id_fase == 'busqueda':
        lista = []
        cont = 0
        longitud = len(fase)
        for bloque in fase:
            cont += 1
            pintar_lineas(screen)
            for item in bloque:
                flow(screen, matrix, item, id_fase, acierto, fallo)
            if cont < longitud:
                reloj.tick_busy_loop()
                pantallas_post_bloque(screen, fase[:cont], longitud)
                reloj.tick_busy_loop()
                lista.append(reloj.get_time())
                color_pantalla('black', screen)
            else:
                reloj.tick_busy_loop()
                resultados_post_bloque(screen, fase[:cont], longitud)
                cerrado = True
                while cerrado == True:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if (event.key == K_SPACE):
                                reloj.tick_busy_loop()
                                lista.append(reloj.get_time())
                                cerrado = False
            pygame.display.flip()
        return lista
    else:
        lista = []
        # Bucle que recorre la fase de búsqueda, estándar e incompleta
        ultimo = len(fase)
        cont = 0
        for bloque in fase:
            cont += 1
            # Pintar las 4 líneas en la pantalla
            pintar_lineas(screen)
            for item in bloque:
                flow(screen, matrix, item, id_fase, acierto, fallo)
            if cont < ultimo:
                reloj.tick_busy_loop()
                mensaje_post_bloque(screen, id_fase)
                reloj.tick_busy_loop()
                lista.append(reloj.get_time())
        return lista
        '''
        # Prueba
        for i in range(2):
            pintar_lineas(screen)
            for item in fase[i]:
                flow(screen, matrix, item, id_fase, acierto, fallo)
            if i < 1:
                reloj.tick_busy_loop()
                mensaje_post_bloque(screen, id_fase)
                reloj.tick_busy_loop()
                lista.append(reloj.get_time())
        return lista
        '''


def imprimir_texto(screen, texto, x, y, color, fuente):
    # separa el texto en elementos de una lista
    # ejemplo: convierte "hola \n mundo" en ["hola ", " mundo"]
    texto_en_lineas = texto.split('\n')
    # un bucle que itera por cada una de las lineas del texto
    for linea in texto_en_lineas:
        nueva = fuente.render(linea, 1, color)
        # imprime en pantalla (se debe ejecutar pygame.display.flip() luego)
        screen.blit(nueva, (x, y))
        # reduce la altura de la coordenada vertical, para luego volver
        # a imprimir la siguiente linea de texto mas abajo.
        y += nueva.get_height()


def instrucciones_iniciales(screen):
    # Color de la pantalla
    color_pantalla('white', screen)
    # Estado inicial
    estado = 0
    mostrar_instrucciones(estado, screen)
    cerradura = True
    while cerradura == True:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                # Siguiente estado
                if evento.key == K_c:
                    if estado < 3:
                        estado += 1
                    if estado == 1:
                        mostrar_instrucciones(estado, screen)
                    elif estado == 2:
                        mostrar_instrucciones(estado, screen)
                    elif estado == 3:
                        mostrar_instrucciones(estado, screen)
                    elif estado == 4:
                        mostrar_instrucciones(estado, screen)
                # Estado anterior
                elif evento.key == K_a:
                    if estado == 0:
                        mostrar_instrucciones(estado, screen)
                    else:
                        estado -= 1
                        if estado == 0:
                            mostrar_instrucciones(estado, screen)
                        elif estado == 1:
                            mostrar_instrucciones(estado, screen)
                        elif estado == 2:
                            mostrar_instrucciones(estado, screen)
                        elif estado == 3:
                            mostrar_instrucciones(estado, screen)
                        elif estado == 4:
                            mostrar_instrucciones(estado, screen)
                # Comenzar bloque práctica
                if evento.key == K_SPACE:
                    if estado == 3:
                        cerradura = False


def instrucciones_busqueda(screen):
    # Color de la pantalla
    color_pantalla('white', screen)
    mostrar_instrucciones(5, screen)
    cerradura = True
    while cerradura == True:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                if evento.key == K_SPACE:
                    cerradura = False


def instrucciones_estandar(screen):
    # Color de la pantalla
    color_pantalla('white', screen)
    # Estado
    estado = 6
    mostrar_instrucciones(6, screen)
    cerradura = True
    while cerradura == True:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                # Pantalla siguiente
                if evento.key == K_c:
                    if estado == 6:
                        estado = 7
                        mostrar_instrucciones(estado, screen)
                if evento.key == K_a:
                    if estado == 7:
                        estado = 6
                        mostrar_instrucciones(estado, screen)
                if evento.key == K_SPACE:
                    if estado == 7:
                        cerradura = False


def instrucciones_incompleta(screen):
    # Color de la pantalla
    color_pantalla('white', screen)
    mostrar_instrucciones(8, screen)
    cerradura = True
    while cerradura == True:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                if evento.key == K_SPACE:
                    cerradura = False


def mostrar_despedida(screen):
    color_pantalla('white', screen)
    # Definimos la fuente a utilizar, None = pygame por defecto
    fuente = pygame.font.Font(None, 25)
    # Obtenemos ancho y alto de la pantalla
    width, height = screen.get_size()
    # Coordenada de inicio x
    x = round(int((width - 900) / 2))
    y = round(int(height / 2) - 200)
    texto = instrucciones('despedida')
    imprimir_texto(screen, texto, x, y, pygame.Color('black'), fuente)
    # Actualizamos la pantalla
    pygame.display.flip()


def mostrar_instrucciones(estado, screen):
    # Función que pinta en pantalla las instrucciones
    # Resolución de la pantalla
    width, height = screen.get_size()
    # Definimos margenes
    x = round(int((width - 900) / 2))
    y = round(int((height - (height * 0.9)) / 2))
    # Color de la pantalla
    color_pantalla('white', screen)
    # Fuente
    fuente = pygame.font.Font(None, 25)
    if estado == 0:
        texto = instrucciones('entrada')
        imprimir_texto(screen, texto, x, y, pygame.Color('black'), fuente)
        boton_continuar(screen)
    elif estado == 1:
        texto = instrucciones('consentimiento')
        imprimir_texto(screen, texto, x, y, pygame.Color('black'), fuente)
        boton_continuar(screen)
        boton_atras(screen)
    elif estado == 2:
        texto = instrucciones('busqueda1')
        imprimir_texto(screen, texto, x, y, pygame.Color('black'), fuente)
        boton_continuar(screen)
        boton_atras(screen)
    elif estado == 3:
        texto = instrucciones('busqueda2')
        imprimir_texto(screen, texto, x, y, pygame.Color('black'), fuente)
        #boton_continuar(screen)
        boton_atras(screen)
    elif estado == 4:
        texto = instrucciones('practica')
        imprimir_texto(screen, texto, x, y, pygame.Color('black'), fuente)
        boton_atras(screen)
    elif estado == 5:
        texto = instrucciones('experimentales')
        imprimir_texto(screen, texto, x, y, pygame.Color('black'), fuente)
    elif estado == 6:
        texto = instrucciones('estandar1')
        imprimir_texto(screen, texto, x, y, pygame.Color('black'), fuente)
        boton_continuar(screen)
    elif estado == 7:
        texto = instrucciones('estandar2')
        imprimir_texto(screen, texto, x, y, pygame.Color('black'), fuente)
        boton_atras(screen)
    elif estado == 8:
        texto = instrucciones('incompleta')
        imprimir_texto(screen, texto, x, y, pygame.Color('black'), fuente)
    pygame.display.flip()


def boton_continuar(screen):
    texto = "CONTINUAR (C)"
    # Fuente
    fuente = pygame.font.Font(None, 27)
    # Objeto texto
    message = fuente.render(texto, 0, pygame.Color('black'))
    # Resolución de la pantalla
    width, height = screen.get_size()
    # Coordenadas del rectángulo para mostrar
    x = width - 160
    y = height - 50
    screen.blit(message, (x, y))


def boton_atras(screen):
    texto = "ATRÁS (A)"
    # Fuente
    fuente = pygame.font.Font(None, 27)
    # Objeto texto
    message = fuente.render(texto, 0, pygame.Color('black'))
    # Resolución de la pantalla
    width, height = screen.get_size()
    # Coordenadas del rectángulo para mostrar
    x = 10
    y = height - 50
    screen.blit(message, (x, y))


# Instrucciones de la tarea
def instrucciones(id):
    if id == 'entrada':
        texto = "Bienvenid@. A continuación, vamos a pedirte que durante esta sesión realices una tarea muy sencilla."
    elif id == 'consentimiento':
        texto = "Antes de comenzar, nos gustaría agradecer tu participación en este experimento, así como\ntambién recordarte que los datos personales que nos proporciones (nombre, apellidos y/o \nteléfono, si nos los has facilitado para concertar esta sesión) son confidenciales: \núnicamente te incluiremos en nuestra lista de participantes, para saber que has hecho \nla tarea y no pedírtelo nuevamente en el futuro (desde un punto de vista experimental \ndebes saber que, como norma general, es poco recomendable realizar la misma tarea en más\nde una ocasión). Lo que nos interesa son tus respuestas a lo largo de la sesión (a \ncontinuación te explicaremos en qué consiste la tarea): además, para elaborar el informe\nexperimental no consideraremos tus datos aisladamente, sino que tendremos en cuenta el\npromedio del grupo. Por esta razón hemos anotado si eres un chico o una chica y tu edad\n(para que podamos caracterizar la muestra en el informe: respuestas promedio y edad del\ngrupo, cuántos chicos y chicas hay… Sin referencia específica alguna a participantes\nconcret@s).\n\nSi te parece correcto, antes de continuar leyendo las instrucciones, por favor, rellena\nla copia que tienes a tu lado y pulsa la tecla correspondiente. En caso contrario, por\nfavor, avisa al experimentador."
    elif id == 'busqueda1':
        texto = "En esta tarea debes localizar una ‘T’ rotada entre un conjunto de letras ‘L’ también\nrotadas, e indicar hacia dónde apunta la ‘T’ (izquierda o derecha). Si el extremo más\nlargo de la ‘T’ apunta hacia la IZQUIERDA, pulsa la tecla correspondiente a la letra ‘Z’,\ny si apunta hacia la DERECHA, pulsa la tecla correspondiente a la letra ‘M’.\nDebes responder lo más RÁPIDAMENTE POSIBLE, y al mismo tiempo, debes tratar de cometer\nel MENOR NÚMERO DE ERRORES POSIBLE. Para ello, mantén colocado el dedo índice de cada\nmano sobre las teclas de respuesta durante toda la tarea (dedo índice de la mano\nizquierda, sobre la tecla ‘Z’, y dedo índice de la mano derecha, sobre la tecla ‘M’).\nCada vez que tu respuesta sea correcta escucharás un tono agudo muy breve, y cada vez que\ncometas un error escucharás un tono grave más largo. Antes de comenzar cada ensayo, debes\nmirar un punto de fijación de color blanco que se mostrará en el centro de la pantalla\ndurante un momento, y que te indicará que debes prepararte para comenzar.\n\nSi en algún momento necesitas hacer una pausa, puedes hacerlo al FINAL de cada bloque de\nensayos, pero NO DURANTE la realización de uno de los bloques, pues debes tratar de\nresponder lo más rápidamente posible. Es recomendable que NO SALGAS de la cabina\nexperimental durante las pausas (en caso de que las necesites).\n\nLa tarea consta de varios bloques experimentales, de tal forma que, cuando finalices cada\nuno de ellos, se te pedirá que pulses una tecla para comenzar el siguiente, y así hasta\nque termine la tarea. Al final de cada bloque se te dará información relativa al tiempo\nmedio de respuesta (milisegundos) empleado durante el bloque, y al porcentaje de aciertos.\nEste porcentaje debe ser igual o superio al 90% para que tus datos sean útiles y podeamos\nanalizarlos. Sin embargo, si en algún bloque tu porcentaje de aciertos no supera el 90%, esto\nno significa que debas dejar la tarea: en este caso, utiliza esta información (tu porcentaje)\npara tratar de mejorar tu ejecución en el siguiente bloque de ensayos. No obstante, no olvides\nque la tarea requiere PRECISIÓN PERO TAMBIÉN RAPIDEZ.\nRecuerda:\n\n    -‘T’ apuntando hacia la IZQUIERDA: tecla ‘Z’ con el índice de tu mano izquierda.\n\n    -‘T’ apuntando hacia la DERECHA: tecla ‘M’ con el índice de la tu mano derecha."
    elif id == 'busqueda2':
        texto = "NO OLVIDES RESPONDER LO MÁS RÁPIDAMENTE QUE PUEDAS, TRATANDO AL MISMO TIEMPO DE\nCOMETER EL MENOR NÚMERO DE ERRORES POSIBLE.\n\nSi tienes alguna duda, plantéasela al experimentador antes de continuar. En caso\ncontrario, pulsa la BARRA ESPACIADORA para comenzar el BLOQUE DE PRÁCTICA, después del\ncual comenzarán los BLOQUES EXPERIMENTALES.\nPulsa la BARRA ESPACIADORA para continuar la sesión."
    elif id == 'practica':
        texto = "Vamos a comenzar el BLOQUE DE PRÁCTICA. Intenta responder con la mayor rapidez y\nprecisión. Al finalizar el bloque podrás ver los datos correspondientes al tiempo medio\nde respuesta y a tu porcentaje de aciertos, tal y como se te irán mostrando\na lo largo de la tarea.\n\nPulsa la BARRA ESPACIADORA para comenzar."
    elif id == 'experimentales':
        texto = "Vamos a comenzar los BLOQUES EXPERIMENTALES. Como antes, intenta responder con la mayor\nrapidez y precisión.\n\nSi tienes alguna duda, plantéasela al experimentador antes de continuar. En caso\ncontrario, pulsa la BARRA ESPACIADORA para comenzar."
    elif id == 'transcion':
        texto = "Hemos terminado este bloque. Estos son los datos correspondientes a tu tiempo medio\nde respuesta y tu porcentaje de aciertos hasta el momento:\n\nNo olvides responder lo más rápidamente posible y al mismo tiempo tratar de cometer el\nmenor número de errores posible.\n\nSi tienes alguna duda, plantéasela al experimentador antes de continuar. En caso\ncontrario, coloca los dedos sobre las teclas de respuesta igual que antes, y pulsa\nla BARRA ESPACIADORA para comenzar."
    elif id == 'estandar1':
        texto = "Hasta aquí ha llegado esta parte de la sesión. Ahora vamos a pedirte que realices otra\ntarea, un poco diferente de la anterior.\n\nDurante los BLOQUES ANTERIORES has tenido que BUSCAR UNA LETRA ‘T’ ROTADA y RESPONDER A\nSU ORIENTACIÓN, con RAPIDEZ y PRECISIÓN, pulsando la tecla correspondiente (‘Z’ si\napuntaba hacia la izquierda y ‘M’ si apuntaba hacia la derecha).\n\nAHORA YA NO DEBES RESPONDER A LA ORIENTACIÓN DE LA LETRA ‘T’. AHORA, en cada ensayo verás\nen la pantalla DOCE LETRAS ‘L’ ROTADAS Y NINGUNA LETRA ‘T’. Tu tarea consiste en indicar\nDÓNDE CREES QUE SE HABRÍA PRESENTADO la LETRA ‘T’ en cada ensayo, esto es, debes INDICAR\nen CUÁL DE LOS CUATRO CUADRANTES que aparecen en la pantalla APARECERÍA LA LETRA ‘T’.\nHazlo de forma rápida, sin pensarlo demasiado, pues lo que has aprendido hasta\nahora, aunque no seas consciente de ello, debería ayudarte a acertar en cierto número de\nensayos.\n\nPara responder, utiliza las teclas ‘Q’, ‘O’, ‘S’ y ‘K’. Para indicar que la letra ‘T’ se\nhabría presentado en el cuadrante superior izquierdo, utiliza la tecla ‘Q’; para indicar\nque aparecería en el CUADRANTE SUPERIOR DERECHO, utiliza la tecla ‘O’; para indicar que\nse habría presentado en el CUADRANTE INFERIOR IZQUIERDO, utiliza la tecla ‘S’; y para\nindicar que aparecería en el CUADRANTE INFERIOR DERECHO, utiliza la tecla ‘K’.\nAsí:\n\n    -ARRIBA A LA IZQUIERDA: tecla ‘Q’.\n\n    -ARRIBA A LA DERECHA: tecla ‘O’.\n\n    -ABAJO A LA IZQUIERDA: tecla ‘S’.\n\n    -ABAJO A LA DERECHA: tecla ‘K’.\n\nColoca el DEDO ÍNDICE de las manos izquierda y derecha sobre las teclas ‘S’ y ‘K’,\nrespectivamente, y el DEDO CORAZÓN izquierdo y derecho sobre las teclas ‘Q’ y ‘O’,\nrespectivamente. Como antes, es importante que mantengas los dedos sobre las teclas\nde respuesta durante toda la tarea."
    elif id == 'estandar2':
        texto = "Ahora ya no escucharás ningún tono que te indique si tus respuestas son o no correctas\ndespués de responder en cada ensayo. Es importante que te dejes llevar por tu primera\nimpresión (INTUICIÓN) en cada ensayo, y pulses muy rápidamente la tecla correspondiente\nal cuadrante en que esperarías encontrar la letra ‘T’. Por tanto, aunque ahora no es\nimprescindible responder lo más rápidamente posible, sí es conveniente que respondas muy\nrápido para facilitar que tu intuición actúe de modo más eficiente guiando tus respuestas.\n\nSi tienes alguna DUDA, es IMPRESCINDIBLE QUE AVISES al experimentador. En caso contrario,\npulsa la BARRA ESPACIADORA para empezar."
    elif id == 'incompleta':
        texto = "Hasta aquí ha llegado esta parte de la sesión. Ahora vamos a pedirte que realices una\núltima tarea, similar a la anterior.\n\nDurante los BLOQUES ANTERIORES has tenido que indicar DÓNDE CREES QUE SE HABRÍA PRESENTADO\nla LETRA ‘T’ en cada ensayo, esto es, debías INDICAR en CUÁL DE LOS CUATRO CUADRANTES que\naparecen en la pantalla APARECERÍA LA LETRA ‘T’. AHORA lo harás de nuevo, PERO en lugar de\nver doce letras ‘L’ rotadas verás OCHO. Como antes, hazlo de forma rápida, sin\npensarlo demasiado, pues lo que has aprendido hasta ahora, aunque no seas consciente\nde ello, debería ayudarte a acertar en cierto número de ensayos.\n\nPara responder, utiliza las teclas ‘Q’, ‘O’, ‘S’ y ‘K’. Para indicar que la letra ‘T’ se\nhabría presentado en el cuadrante superior izquierdo, utiliza la tecla ‘Q’; para indicar\nque aparecería en el CUADRANTE SUPERIOR DERECHO, utiliza la tecla ‘O’; para indicar que se\nhabría presentado en el CUADRANTE INFERIOR IZQUIERDO, utiliza la tecla ‘S’; y para indicar\nque aparecería en el CUADRANTE INFERIOR DERECHO, utiliza la tecla ‘K’.\nAsí:\n\n    -ARRIBA A LA IZQUIERDA: tecla ‘Q’.\n\n    -ARRIBA A LA DERECHA: tecla ‘O’.\n\n    -ABAJO A LA IZQUIERDA: tecla ‘S’.\n\n    -ABAJO A LA DERECHA: tecla ‘K’.\n\nColoca el DEDO ÍNDICE de las manos izquierda y derecha sobre las teclas ‘S’ y ‘K’,\nrespectivamente, y el DEDO CORAZÓN izquierdo y derecho sobre las teclas ‘Q’ y ‘O’,\nrespectivamente. Como antes, es importante que mantengas los dedos sobre las teclas de\nrespuesta durante toda la tarea.\n\nComo antes,  no escucharás ningún tono que te indique si tus respuestas son o no correctas\ndespués de responder en cada ensayo. Es importante que te dejes llevar por tu primera\nimpresión (INTUICIÓN) en cada ensayo, y pulses muy rápidamente la tecla correspondiente al\ncuadrante en que esperarías encontrar la letra ‘T’. Por tanto, aunque ahora no es\nimprescindible responder lo más rápidamente posible, sí es conveniente que respondas muy\nrápido para facilitar que tu intuición actúe de modo más eficiente guiando tus respuestas.\n\nSi tienes alguna DUDA, es IMPRESCINDIBLE QUE AVISES al experimentador. En caso contrario,\npulsa la BARRA ESPACIADORA para empezar."
    elif id == 'despedida':
        texto = "Hemos terminado: hasta aquí ha llegado la sesión experimental.\n\n\n¡Gracias por participar!\n\n\nNo es necesario que pulses ninguna tecla. Por favor, en silencio, indícale al\nexperimentador que has finalizado la tarea o espera a que se acerque a tu cabina."
    return texto
