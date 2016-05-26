import pygame
from pygame.locals import *
import os
import sys
import time
from tkinter import *
from tkinter import ttk
from datetime import date
from lib import generar_fases, guardar_datos, grabar_flujo
from gui import ejecutar_fase, crear_ventana, mostrar_resultados, \
instrucciones_iniciales, instrucciones_busqueda,  instrucciones_estandar, \
instrucciones_incompleta


def main(sexo, edad, condicion_experimental, participante):
    # #####################################
    # ##########COMIENZO DE LA TAREA#######
    # #####################################
    date_t = time.localtime()
    # setup mixer to avoid sound lag
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()                      # initialize pygame
    # Generamos las diversas fases que componen el experimento
    # Fases: práctica, búsqueda, generación estándar e incompleta
    fases = generar_fases(int(condicionExperimental))
    # ########################################
    # ###########Guardar Secuencia############
    # ########################################
    # Guardar flujo experimento
    parametros = []
    parametros.append(str(condicion_experimental))
    parametros.append(participante)
    grabar_flujo(fases, parametros)
    # creamos la superficie principal la ventana
    ventana = crear_ventana()
    # Reloj para cronometrar el tiempo entre instrucciones
    reloj = pygame.time.Clock()
    # Comienza la cuenta
    reloj.tick_busy_loop()
    # Instrucciones iniciales
    instrucciones_iniciales(ventana)
    # Termina la cuenta
    reloj.tick_busy_loop()
    tiempo_instrucciones_iniciales = reloj.get_time()
    # Instrucciones
    # Fase Práctica
    # Guardo hora de inicio
    start_phases = []
    start_phase = time.localtime()
    hour = str(start_phase[3]) + ':' + str(start_phase[4]) + ':' + \
        str(start_phase[5])
    start_phases.append(hour)
    tiempo_f_p = ejecutar_fase('practica', fases[0], ventana)
    # Comienza la cuenta
    reloj.tick_busy_loop()
    # Instrucciones fase busqueda
    instrucciones_busqueda(ventana)
    # Termina la cuenta
    reloj.tick_busy_loop()
    tiempo_instrucciones_busqueda = reloj.get_time()
    # Fase Búsqueda
    start_phase = time.localtime()
    hour = str(start_phase[3]) + ':' + str(start_phase[4]) + ':' + \
        str(start_phase[5])
    start_phases.append(hour)
    tiempo_f_b = ejecutar_fase('busqueda', fases[1], ventana)
    # Comienza la cuenta
    reloj.tick_busy_loop()
    # Instrucciones fase generación estándar
    instrucciones_estandar(ventana)
    # Termina la cuenta
    reloj.tick_busy_loop()
    tiempo_instrucciones_estandar = reloj.get_time()
    # Fase Generación Estándar
    start_phase = time.localtime()
    hour = str(start_phase[3]) + ':' + str(start_phase[4]) + ':' + \
        str(start_phase[5])
    start_phases.append(hour)
    tiempo_f_g_e = ejecutar_fase('estandar', fases[2], ventana)
    # Comienza la cuenta
    reloj.tick_busy_loop()
    # Instrucciones generación incompleta
    instrucciones_incompleta(ventana)
    # Termina la cuenta
    reloj.tick_busy_loop()
    tiempo_instrucciones_incompleta = reloj.get_time()
    # Fase Generación Incompleta
    start_phase = time.localtime()
    hour = str(start_phase[3]) + ':' + str(start_phase[4]) + ':' + \
        str(start_phase[5])
    start_phases.append(hour)
    tiempo_f_g_i = ejecutar_fase('incompleta', fases[3], ventana)
    # Mostramos los resultados obtenidos en las fases de Búsqueda y Generación
    mostrar_resultados(ventana, fases[1], fases[2], fases[3])
    # #################################################
    # ###############GUARDAR DATOS#####################
    # #################################################
    lista = []
    fecha = str(date_t[2]) + '/' + str(date_t[1]) + '/' + str(date_t[0])
    hora = str(date_t[3]) + ':' + str(date_t[4]) + ':' + str(date_t[5])
    lista.append(fecha)
    lista.append(hora)
    lista.append('x126a')
    lista.append(str(condicion_experimental))
    lista.append(participante)
    if sexo == 'Chico':
        lista.append('1')
    else:
        lista.append('2')
    lista.append(edad)
    # Fin del experimento
    start_phase = time.localtime()
    hour = str(start_phase[3]) + ':' + str(start_phase[4]) + ':' + \
        str(start_phase[5])
    start_phases.append(hour)
    # Guardamos datos
    guardar_datos(fases, lista, tiempo_instrucciones_iniciales, tiempo_f_p, \
        tiempo_instrucciones_busqueda, tiempo_f_b, \
        tiempo_instrucciones_estandar, tiempo_f_g_e, \
        tiempo_instrucciones_incompleta, tiempo_f_g_i, start_phases)
    while 1:
            for event in pygame.event.get():
                if (event.type == KEYUP) or (event.type == KEYDOWN):
                    print(event)
                    if (event.key == K_ESCAPE):
                        sys.exit()
                if event.type == pygame.QUIT:
                    sys.exit()


def validar():
    completo = True
    mensaje = ""
    if combo_sexo.get() == 'Sexo':
        completo = False
        mensaje += "Selecciona sexo.\n"
    if entry_edad.get() == "":
        completo = False
        mensaje += "Introduce edad.\n"
    if combo_experimental.get() == 'Condición Experimental':
        completo = False
        mensaje += "Selecciona Condición Experimental.\n"
    if entry_participante.get() == "":
        completo = False
        mensaje += "Introduce participante."
    if completo == False:
        label_mensaje['text'] = mensaje
    else:
        root.quit()
        print('Correcto')


if __name__ == '__main__':
    # Crear ventana principal de entrada de datos y título de la ventana.
    root = Tk()
    root.title('x126a')
    # Crear frame, el frame contendrá los widgets.
    contenedor = Frame(root)
    contenedor['borderwidth'] = 2
    contenedor['relief'] = 'sunken'
    contenedor.pack()
    # Combobox con los generos
    combo_sexo = ttk.Combobox(contenedor)
    combo_sexo['values'] = ('Sexo', 'Chico', 'Chica')
    # Opción por defecto del combobox
    combo_sexo.set('Sexo')
    combo_sexo.pack()
    # Label edad
    label_edad = Label(contenedor, text='Edad:', justify=LEFT)
    label_edad.pack()
    # Entry edad
    edad = StringVar()
    entry_edad = Entry(contenedor, textvariable=edad)
    entry_edad.pack()
    # Combobox condicion experimental
    combo_experimental = ttk.Combobox(contenedor, width=25)
    combo_experimental['values'] = ('Condición Experimental', 1, 2)
    combo_experimental.set('Condición Experimental')
    combo_experimental.pack()
    # Identificador de participante
    label_identificador = Label(contenedor, text='Participante:', justify=LEFT)
    label_identificador.pack()
    # Entry participante
    participante = StringVar()
    entry_participante = Entry(contenedor, textvariable=participante)
    entry_participante.pack()
    # Panel de información
    label_mensaje = Label(root, text="", fg="red")
    label_mensaje.pack()
    # Botón
    button = Button(root, text='Entrar', command=validar).pack()
    #mainloop()
    root.mainloop()
    sexo = combo_sexo.get()
    edad = entry_edad.get()
    condicionExperimental = combo_experimental.get()
    participante = entry_participante.get()
    print(sexo)
    print(edad)
    print(condicionExperimental)
    print(participante)
    root.destroy()
    main(sexo, edad, condicionExperimental, participante)
