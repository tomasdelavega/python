# -*- coding: utf-8 *-*

import math
import random
import copy
from datetime import date
from clases import Elemento, Ensayo


def generar_cuadrantes():
    '''función que retorna una lista con los cuadrantes revueltos'''
    cuadrantes = [1, 2, 3, 4]
    random.shuffle(cuadrantes)
    return cuadrantes


def generar_fijos(limit):
    '''función que retorna una lista revuelta con los tipos fijos'''
    lista = []
    for i in range(limit):
        cadena = str(i + 1)
        lista.append('F' + cadena)
    random.shuffle(lista)
    return lista


def generar_variables(limit):
    '''función que retorna una lista revuelta con los tipos variables'''
    lista = []
    for i in range(limit):
        cadena = str(i + 1)
        lista.append('V' + cadena)
    random.shuffle(lista)
    return lista


def colores_outcomes():
    '''función que devuelve una lista de colores revuelta, se empleará para
    retornar los colores de los outcomes'''
    lista = ['amarillo', 'azul', 'rojo', 'verde']
    random.shuffle(lista)
    return lista


def generar_colores(color):
    '''función que devuelve una lista de colores revuelta para los
    distractores'''
    colores = ['amarillo', 'amarillo', 'amarillo', 'azul', 'azul', 'azul', \
                'rojo', 'rojo', 'rojo', 'verde', 'verde', 'verde']
    colores.remove(color)
    random.shuffle(colores)
    return colores


def generar_rotaciones_outcome(numero_elementos):
    '''Función que recibe el número de ensayos y devuelve una lista con n
    elementos de los cuales n/2 son 90 y los otros n/2 son 270.'''
    numero_veces = int(numero_elementos / 2)
    rotaciones = [90, 270] * numero_veces
    random.shuffle(rotaciones)
    return rotaciones


def generar_rotacion():
    '''Función que devuelve una rotación al azar de la lista'''
    rotate = [0, 90, 180, 270]
    random.shuffle(rotate)
    return rotate.pop()


def generar_rotaciones():
    '''funcion que retorna una lista  de 11 elementos aleatorizada con las
    distintas rotaciones de cada distractor'''
    rotate = [0, 90, 180, 270]
    matriz = [rotate[random.randrange(4)], rotate[random.randrange(4)], \
                rotate[random.randrange(4)], rotate[random.randrange(4)], \
                rotate[random.randrange(4)], rotate[random.randrange(4)], \
                rotate[random.randrange(4)], rotate[random.randrange(4)], \
                rotate[random.randrange(4)], rotate[random.randrange(4)], \
                rotate[random.randrange(4)]]
    random.shuffle(matriz)
    return matriz


def generar_posiciones():
    '''función que devuelve una lista de 4 elementos, cada elemento hace
    referencia a cada uno de los 4 cuadrantes en que se divide la matriz.
    Cada elemento contiene una lista con las 16 posiciones de cada cuadrante
    aleatorizadas.'''
    matriz = [list(range(1, 17)), list(range(17, 33)), list(range(33, 49)),\
              list(range(49, 65))]
    for i in range(len(matriz)):
        random.shuffle(matriz[i])
    return matriz


def obtener_cuadrante(pos):
    '''Función que recibe una posición y devuelve el cuadrante al cual
    pertence'''
    if pos < 17:
        cuadrante = 1
    elif pos > 16 and pos < 33:
        cuadrante = 2
    elif pos > 32 and pos < 49:
        cuadrante = 3
    elif pos > 48:
        cuadrante = 4
    return cuadrante


def generar_lista_outcomes(n_fijos, n_var, n_prac):
    '''Función que recibe tres enteros los cuales indican el número de
    ensayos fijos, variables y ensayos para la fase de prácticas. Los ensayos
    de tipo fijo y variable generados en esta función son las semillas a partir
    de las cuales se generan los ensayos de tipo fijo y variable en las
    sucesivas fases(Búsqueda y Generación(Estándar e Incompleta)).'''
    # Lista de posiciones aleatorizadas por cuadrante
    posiciones = generar_posiciones()
    lista = []
    fijos = []
    variables = []
    # Lista de posiciones para ensayos fijos
    for i in range(math.trunc(n_fijos / 4)):
        fijos.append(posiciones[0].pop())
        fijos.append(posiciones[1].pop())
        fijos.append(posiciones[2].pop())
        fijos.append(posiciones[3].pop())
    if int(math.fmod(n_fijos, 4)) != 0:
        cuadrantes = [0, 1, 2, 3]
        random.shuffle(cuadrantes)
        for i in range(int(math.fmod(n_fijos, 4))):
            fijos.append(posiciones[cuadrantes.pop()].pop())
    # Lista de posiciones para ensayos variables
    for i in range(math.trunc(n_var / 4)):
        variables.append(posiciones[0].pop())
        variables.append(posiciones[1].pop())
        variables.append(posiciones[2].pop())
        variables.append(posiciones[3].pop())
    if int(math.fmod(n_var, 4)) != 0:
        for i in range(int(math.fmod(n_var, 4))):
            if len(cuadrantes) == 0:
                cuadrantes = [0, 1, 2, 3]
                random.shuffle(cuadrantes)
            variables.append(posiciones[cuadrantes.pop()].pop())
    # Lista de posiciones para ensayos en la fase de prácticas
    practica = []
    for i in range(n_prac):
        practica.append(posiciones[random.randrange(4)].pop())
    random.shuffle(fijos)
    random.shuffle(variables)
    lista.append(practica)
    lista.append(fijos)
    lista.append(variables)
    return lista


def generar_semillas(pos_fijos, pos_variables):
    '''Función que devuelve las semillas a partir de las cuales se generan los
    bloques de ensayos fijos y variables. Devuelve una lista de dos elementos
    el primer elemento contiene una lista con las semillas de los tipos fijos,
    el segundo elemento contiene una lista con las semillas de los tivpos
    variables.'''
    semillas = []
    lista_fijos = []
    lista_variables = []
    colores = colores_outcomes()
    tipos = generar_fijos(len(pos_fijos))
    for i in range(len(pos_fijos)):
        tipo = tipos.pop()
        posicion = pos_fijos.pop()
        if len(colores) == 0:
            colores = colores_outcomes()
        color = colores.pop()
        distractores = generar_lista_distractores(color, \
                        obtener_cuadrante(posicion), posiciones=[posicion])
        lista_fijos.append(Ensayo(tipo, posicion, color, None,\
                                distractores))
    # Variables
    tipos = generar_variables(len(pos_variables))
    #rotaciones = generar_rotaciones_outcome(len(pos_variables))
    for i in range(len(pos_variables)):
        tipo = tipos.pop()
        posicion = pos_variables.pop()
        if len(colores) == 0:
            colores = colores_outcomes()
        color = colores.pop()
        lista_variables.append(Ensayo(tipo, posicion, color))

    semillas.append(lista_fijos)
    semillas.append(lista_variables)
    return semillas


def generar_fase_practica(posiciones):
    '''Devuelve la lista de ensayos que componen la fase de práctica.
    Posiciones es una lista con las posiciones de cada outcome.'''
    lista = []
    colores = colores_outcomes()
    rota_out = generar_rotaciones_outcome(len(posiciones))
    for i in range(len(posiciones)):
        tipo = 'Practica'
        posicion = posiciones.pop()
        if len(colores) == 0:
            colores = colores_outcomes()
        color = colores.pop()
        rotacion = rota_out.pop()
        distractores = generar_lista_distractores(color, \
                        obtener_cuadrante(posicion), posiciones=[posicion])
        lista.append(Ensayo(tipo, posicion, color, rotacion, distractores))
    return lista


def generar_fase_busqueda(n_bloques, fijos, variables):
    '''Función que genera y devuelve los ensayos que forman la fase
    de búsqueda. Recibe tres parámetros n_bloques = número de bloques que
    forman la fase. fijos =  lista de semillas a partir de las cuales se
    formarán los ensayos de tipo fijo en la fase.
    variables = lista de semillas a partir de las cuales se formarán los
    ensayos de tipo variable en la fase.'''
    # Lista con los bloques de la fase
    bloque = []



    # Lista de n elementos con las rotaciones de cada outcome fijo
    rotaciones_fijos = generar_matriz_rotaciones(n_bloques)
    # Lista de n elementos con las rotaciones de cada outcome variable
    rotaciones_variables = generar_matriz_rotaciones(n_bloques)
    '''añadido de forma temporal para controlar visualizar matriz
    print()
    for item in generar_matriz_traspuesta(rotaciones_fijos):
        print(item)
    print('VARIABLES')
    for item in generar_matriz_traspuesta(rotaciones_variables):
        print(item)
    '''
    # Recorremos la lista de bloques
    for i in range(n_bloques):
        rot_fijos = rotaciones_fijos[i]
        rot_var = rotaciones_variables[i]
        l_aux = []
        for elem in fijos:
            tipo = elem.devolver_tipo()
            #cadena es el id
            cadena = tipo + 'B' + str(i + 1)
            posicion = elem.devolver_posicion_outcome()
            color = elem.devolver_color_outcome()
            grados = rot_fijos[int(tipo[1:]) - 1]
            #elem.devolver_distractores()
            l_aux.append(Ensayo(tipo, posicion, color, grados, \
                            elem.devolver_distractores(), cadena))
        for elem in variables:
            tipo = elem.devolver_tipo()
            cadena = tipo + 'B' + str(i + 1)
            posicion = elem.devolver_posicion_outcome()
            color = elem.devolver_color_outcome()
            grados = rot_var[int(tipo[1:]) - 1]
            cuadrante = obtener_cuadrante(posicion)
            posiciones = [posicion]
            distractores = generar_lista_distractores(color, cuadrante, \
                                                        posiciones)
            l_aux.append(Ensayo(tipo, posicion, color, grados, \
                                    distractores, cadena))
        random.shuffle(l_aux)
        bloque.append(l_aux)
    return bloque


def generar_matriz_rotaciones(orden):
    '''Función que recibe el orden de la matriz y genera una matriz con
    las rotaciones de los outcomes para la fase de busqueda.
    Matriz cuadrada de orden 12 o 24, donde las columnas se corresponden
    con los bloques y las filas con los tipos.'''
    matriz = []
    columnas = orden
    filas = int(orden / 2)
    limite = int(filas / 2)
    tipos = []
    #matriz fijos
    for i in range(filas):
        tipos.append(copy.deepcopy([90, 270] * filas))
    for i in range(columnas):
        bloque = [0] * filas
        contador90 = 0
        contador270 = 0
        tipos90 = []
        tipos270 = []
         #bucle que cuenta el número de elementos de 90 y 270 por cada tipo
        for item in tipos:
            tipos90.append(item.count(90))
            tipos270.append(item.count(270))
        #miramos si ya no hay más elementos de 90 o 270 en cada tipo,
        #en caso de que no los haya solo podemos agregar al bloque
        #el otro valor
        for i in range(filas):
            if tipos90[i] == 0:
                bloque[i] = 270
                contador270 = contador270 + 1
                tipos[i].remove(270)
            elif tipos270[i] == 0:
                bloque[i] = 90
                contador90 = contador90 + 1
                tipos[i].remove(90)
        for i in range(filas):
            if bloque[i] == 0:
                    if contador90 == limite:
                        bloque[i] = 270
                        contador270 = contador270 + 1
                        tipos[i].remove(270)
                    elif contador270 == limite:
                        bloque[i] = 90
                        contador90 = contador90 + 1
                        tipos[i].remove(90)
                    else:
                        rotacion = random.choice([90, 270])
                        bloque[i] = rotacion
                        if rotacion == 90:
                            contador90 = contador90 + 1
                            tipos[i].remove(90)
                        elif rotacion == 270:
                            contador270 = contador270 + 1
                            tipos[i].remove(270)
        matriz.append(copy.deepcopy(bloque))
    return matriz


def ver_matriz(matriz):
    '''Función que recibe una matriz bidimensional y la muestra por pantalla'''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print((matriz[i][j]))


def generar_lista_distractores(color, cuadrante, posiciones=None):
    '''
    Función que devuelve una lista de distractores. Recibe como parámetros
    el color del outcome, el cuadrante correspondiente a la posición del
    outcome y puede que una lista con las posiciones restringidas (formada
    por la posición del outcome y las sucesivas posiciones que se van generando
    para cada distractor).
    '''
    colores = generar_colores(color)
    rotaciones = generar_rotaciones()
    lista = []
    if cuadrante == 1:
        cuadrantes = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
    elif cuadrante == 2:
        cuadrantes = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4]
    elif cuadrante == 3:
        cuadrantes = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4]
    elif cuadrante == 4:
        cuadrantes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
    if posiciones is None:
        pos_restringidas = []
    else:
        pos_restringidas = posiciones[:]
    for i in range(11):
        posicion = generar_posicion(cuadrantes.pop(0), pos_restringidas)
        pos_restringidas.append(posicion)
        lista.append(Elemento(posicion, colores.pop(), rotaciones.pop()))
    return lista


def generar_posicion(cuadrante, l_posiciones_restringidas):
    '''
    Función que devuelve una posción, recibe como parámetros el cuadrante
    al cual tiene que pertencer la posición generada y una lista con las
    posiciones restringidas.
    '''
    if cuadrante == 1:
        limite_inferior = 1
        limite_superior = 16
    elif cuadrante == 2:
        limite_inferior = 17
        limite_superior = 32
    elif cuadrante == 3:
        limite_inferior = 33
        limite_superior = 48
    elif cuadrante == 4:
        limite_inferior = 49
        limite_superior = 64
    random.seed()
    posicion = random.randint(limite_inferior, limite_superior)
    while l_posiciones_restringidas.count(posicion) != 0:
        posicion = random.randint(limite_inferior, limite_superior)
    return posicion


def generar_fase_generacion_estandar(semillas, fase):
    '''Función que recibe semillas(ensayos a partir de los cuales se
    generan todos los demás) y fase (la fase de búsqueda).
    Devuelve una lista con los ensayos de la fase de generación
    estándar.'''
    # Hacemos una copia profunda de los fijos para que no apunten a la misma
    # dirección de memoria.
    fijos = copy.deepcopy(semillas[0])
    # Añadimos a los fijos el id
    for item in fijos:
        cadena = item.devolver_tipo()
        item.asignar_id(cadena)
        item.asignar_rotacion_outcome(generar_rotacion())
    # Se crea la matriz que contendrá los bloques y ensayos de la fase de
    # generación  estándar.
    fase_generacion_estandar = []
    variables = []
    variables_bloque1 = []
    variables_bloque2 = []
    posiciones = []
    # Recorremos las semillas variables.
    for i in range(len(semillas[1])):
        posiciones.append(semillas[1][i].devolver_posicion_outcome())
    variables = devolver_ensayos_ge(fase, posiciones)
    variables_bloque1 = variables[:(int(len(fase) / 2))]
    variables_bloque2 = variables[int(len(fase) / 2):]
    #lista = fijos[:]
    lista = copy.deepcopy(fijos)
    lista.extend(variables_bloque1)
    random.shuffle(lista)
    fase_generacion_estandar.append(lista)
    #lista = fijos[:]
    lista = copy.deepcopy(fijos)
    lista.extend(variables_bloque2)
    random.shuffle(lista)
    fase_generacion_estandar.append(lista)
    return fase_generacion_estandar


def devolver_ensayos_ge(bloques, pos_variables):
    '''Función que selecciona los ensayos que compondrán la fase
    de generación estándar. Recibe como parámetros la fase de
    búsqueda y una lista con las posiciones de los outcomes a partir
    de las cuales se seleccionarán los ensayos que compondrán la fase.'''
    #print('Dentro de devolver ensayos ge')
    lista = []
    limit = int(len(bloques))
    n_veces = int(limit / len(pos_variables))
    posiciones = []
    for i in range(n_veces):
        random.shuffle(pos_variables)
        for j in range(len(pos_variables)):
            posiciones.append(pos_variables[j])
    cont = 0
    while cont < limit:
        indice = random.randrange(limit)
        posicion = posiciones.pop()
        encontrado = False
        while encontrado == False:
            for i in range(len(bloques[indice])):
                tipo = bloques[indice][i].devolver_tipo()
                id = str(indice + 1)
                #id = bloques[indice][i].devolver_id() + 'GE'
                pos = bloques[indice][i].devolver_posicion_outcome()
                color = bloques[indice][i].devolver_color_outcome()
                if posicion == pos:
                    lista.append(Ensayo(tipo, posicion, color, \
                    generar_rotacion(), \
                    bloques[indice][i].devolver_distractores(), id))
                    encontrado = True
                    del bloques[indice][i]
                    break
            if encontrado == False:
                indice = random.randrange(limit)
        cont = cont + 1
    return lista


def generar_fase_generacion_incompleta(semillas, bloques):
    '''Función que se encarga de generar la fase de generación incompleta.
    Recibe como parámetros semillas y bloques, semillas son los ensayos
    a partir de los cuales se generán los ensayos de la fase de búsqueda.
    Bloques son los bloques que forman la fase de búsqueda.'''
    #declaro variables
    fase_generacion_incompleta = []
    variables = []
    variables_bloque1 = []
    variables_bloque2 = []
    posiciones = []
    fijos = copy.deepcopy(semillas[0])
    #Asigna el id a los ensayos fijos
    for item in fijos:
        cadena = item.devolver_tipo()
        item.asignar_id(cadena)
    #Recupero lista de ensayos variables
    for item in semillas[1]:
        posiciones.append(item.devolver_posicion_outcome())
    variables = devolver_ensayos_gi(bloques, posiciones)
    #Eliminamos outcome y distractores cuadrantes restantes
    for item in fijos:
        item = distractores_gi(item)
    for item in variables:
        item = distractores_gi(item)
    #Los ensayos variables los divido en dos bloques
    variables_bloque1 = variables[:(int(len(bloques) / 2))]
    variables_bloque2 = variables[int(len(bloques) / 2):]
    #lista = fijos[:]
    lista = copy.deepcopy(fijos)
    lista.extend(variables_bloque1)
    random.shuffle(lista)
    fase_generacion_incompleta.append(lista)
    #lista = fijos[:]
    lista = copy.deepcopy(fijos)
    lista.extend(variables_bloque2)
    random.shuffle(lista)
    fase_generacion_incompleta.append(lista)
    return (fase_generacion_incompleta)


def devolver_ensayos_gi(bloques, pos_variables):
    '''Función que selecciona los ensayos que van a formar la
    fase de generación incompleta. Recibe como parámetros
    los bloques que componen la fase de búsqueda y las posiciones
    de los outcomes.'''
    lista = []
    limit = int(len(bloques))
    n_veces = int(limit / len(pos_variables))
    posiciones = []
    for i in range(n_veces):
        random.shuffle(pos_variables)
        for j in range(len(pos_variables)):
            posiciones.append(pos_variables[j])
    cont = 0
    while cont < limit:
        indice = random.randrange(limit)
        posicion = posiciones.pop()
        encontrado = False
        while encontrado == False:
            for i in range(len(bloques[indice])):
                tipo = bloques[indice][i].devolver_tipo()
                id = str(indice + 1)
                #id = bloques[indice][i].devolver_id() + 'GI'
                pos = bloques[indice][i].devolver_posicion_outcome()
                color = bloques[indice][i].devolver_color_outcome()
                rotacion = bloques[indice][i].devolver_rotacion_outcome()
                if posicion == pos:
                    lista.append(Ensayo(tipo, posicion, color, \
                    rotacion, \
                    bloques[indice][i].devolver_distractores(), id))
                    encontrado = True
                    del bloques[indice][i]
                    break
            if encontrado == False:
                indice = random.randrange(limit)
        cont = cont + 1
    return lista


def distractores_gi(ensayo):
    '''Función que recibe un ensayo de la fase de generación incompleta y lo
    modela dejando solo dos distractores por cada cuadrante'''
    cuadrante = obtener_cuadrante(ensayo.devolver_posicion_outcome())
    cuadrantes = generar_cuadrantes()
    cuadrantes.remove(cuadrante)
    if cuadrante == 1:
        posiciones = [random.randint(2, 4), random.randint(5, 7), \
                      random.randint(8, 10)]
    elif cuadrante == 2:
        posiciones = [random.randint(0, 2), random.randint(5, 7), \
                      random.randint(8, 10)]
    elif cuadrante == 3:
        posiciones = [random.randint(0, 2), random.randint(3, 5), \
                      random.randint(8, 10)]
    else:
        posiciones = [random.randint(0, 2), random.randint(3, 5), \
                      random.randint(6, 8)]
    '''
    distractores = ensayo.devolver_distractores()
    distractores.pop(posiciones[2])
    distractores.pop(posiciones[1])
    distractores.pop(posiciones[0])
    ensayo.asignar_distractores(distractores)
    '''
    distractores = ensayo.devolver_distractores()
    for pos in posiciones:
        distractores[pos].cambiar_posicion(' ')
        distractores[pos].cambiar_color(' ')
        distractores[pos].cambiar_rotacion(' ')
    ensayo.asignar_distractores(distractores)
    #ensayo.asignar_posicion_outcome(None)
    #ensayo.asignar_color_outcome(None)
    #ensayo.asignar_rotacion_outcome(None)
    return ensayo


def generar_fases(grupo):
    '''Función que recibe el grupo y devuelve una lista con las fases del
    experimento.'''
    ensayos_practica = 10
    if grupo == 1:
        #SCE
        bloques = 24
        ensayos_f_v = 12
    elif grupo == 2:
        #SCR
        bloques = 12
        ensayos_f_v = 6
    '''Posiciones es una lista de con las posiciones de los ensayos
    de prácticas, de tipo fijo y variables.'''
    posiciones = generar_lista_outcomes(ensayos_f_v, ensayos_f_v,
                                                 ensayos_practica)
    semillas = generar_semillas(copy.deepcopy(posiciones[1]), \
                                        copy.deepcopy(posiciones[2]))
    #LOG
    #Lista que contiene los ensayos de la fase de práctica
    print('Creando Fase de Práctica...')
    fase_practica = generar_fase_practica(copy.deepcopy(posiciones[0]))
    ordenar_distractores(fase_practica[0])
    print('Fase de Práctica creada')
    #Lista que contiene la fase de búsqueda
    '''fase_busqueda = generar_fase_busqueda(bloques, \
        copy.deepcopy(semillas[0]), copy.deepcopy(semillas[1]))'''
    print('Creando Fase de Búsqueda...')
    fase_busqueda = generar_fase_busqueda(bloques, semillas[0],
                            semillas[1])
    copia_fase_busqueda = copy.deepcopy(fase_busqueda)
    print('Fase de Búsqueda creada')
    #Lista que contiene los ensayos de la fase de Generación Estándar
    print('Creando Fase de Generación Estándar...')
    fase_generacion_estandar = generar_fase_generacion_estandar(semillas, \
            copia_fase_busqueda)
    print('Fase de Generación Estándar creada')
    #Lista que contiene los ensayos de la fase de Generación Incompleta
    print('Creando Fase de Generación Incompleta...')
    fase_generacion_incompleta = generar_fase_generacion_incompleta(semillas, \
            copia_fase_busqueda)
    print('Fase de Generación Incompleta Creada')
    # Chequeo fase práctica con la fase de búsqueda
    print ('Chequeando fase práctica')
    chequear_fase_practica(fase_practica, fase_busqueda)
    salida = []
    salida.append(fase_practica)
    salida.append(fase_busqueda)
    salida.append(fase_generacion_estandar)
    salida.append(fase_generacion_incompleta)
    return salida


def guardar_fase_practica(fase, condicion):
    '''Función que graba en un fichero la fase de práctica.'''
    try:
        f = open('salida', 'a')
    except IOError:
        "Error al abrir el fichero."
    '''
    cadena = 'Salida de datos: B(Bloque),T(Target)/Ds(Distractores),' \
             'posición(1-64),color(Am=1,Az=2,R=3,V=4),' \
             'rotación(0,90,180,270)'
    f.write('\n')
    f.write('**********************************')
    f.write('FASE PRACTICA')
    f.write('**********************************')
    f.write('\n')
    f.write(cadena)
    f.write('\n\n')
    '''
    fecha = date.today()
    experimento = 'x126'
    subject = 0
    phase = '1'
    block = 0

    for item in fase:
        f.write(str(fecha))
        f.write(',')
        f.write(experimento)
        f.write(',')
        f.write(str(subject))
        f.write(',')
        f.write(str(condicion))
        f.write(',')
        f.write(phase)
        f.write(',')
        f.write(str(block))
        f.write(',')
        f.write(str(item.devolver_id()).rjust(3))
        f.write(',')
        f.write(item.devolver_tipo())
        f.write(',')
        #f.write('T,')
        f.write(str(item.devolver_posicion_outcome()).rjust(2))
        f.write(',')
        color = item.devolver_color_outcome()
        if color == 'amarillo':
            color = '1'
        elif color == 'azul':
            color = '2'
        elif color == 'rojo':
            color = '3'
        elif color == 'verde':
            color = '4'
        else:
            color = 'None'
        f.write(color)
        f.write(',')
        f.write(str(item.devolver_rotacion_outcome()).rjust(3))
        f.write(',')
        f.write(str(item.devolver_respuesta()))
        f.write(',')
        f.write(str(item.devolver_correcto()))
        f.write(',')
        f.write(str(item.devolver_tiempo_respuesta()).rjust(4))
        f.write(',')
        distractores = item.devolver_distractores()
        #f.write('Ds,')
        for elem in distractores:
            f.write(str(elem.devolver_posicion()).rjust(2))
            f.write(',')
            color = elem.devolver_color()
            if color == 'amarillo':
                color = '1'
            elif color == 'azul':
                color = '2'
            elif color == 'rojo':
                color = '3'
            elif color == 'verde':
                color = '4'
            else:
                color = '-'
            f.write(color)
            f.write(',')
            f.write(str(elem.devolver_rotacion()).rjust(3))
            f.write(',')
            f.write('   ')
        f.write('\n')
    f.close()


def grabar_cabeceras(fichero):
    fichero.write('date,')
    fichero.write('hour,')
    fichero.write('exp,')
    fichero.write('group,')
    fichero.write('subj,')
    fichero.write('sex,')
    fichero.write('age,')
    fichero.write('phase,')
    fichero.write('block,')
    fichero.write('block(origin),')
    fichero.write('instruct,')
    fichero.write('type,')
    fichero.write('num,')
    fichero.write('R,')
    fichero.write('acc,')
    fichero.write('RT,')
    fichero.write('posT,')
    fichero.write('colT,')
    fichero.write('rotT,')
    count = 0
    for i in range(11):
        count += 1
        pos = "posD" + str(count)
        col = 'colD' + str(count)
        rot = 'rotD' + str(count)
        fichero.write(pos)
        fichero.write(",")
        fichero.write(col)
        fichero.write(",")
        fichero.write(rot)
        fichero.write(",")
    fichero.write('\n')


def grabar_cabeceras_pre(fichero):
    fichero.write('group,')
    fichero.write('subj,')
    fichero.write('phase,')
    fichero.write('block,')
    fichero.write('block(origin),')
    fichero.write('type,')
    fichero.write('num,')
    fichero.write('posT,')
    fichero.write('colT,')
    fichero.write('rotT,')
    for i in range(11):
        pos = "posD" + str(i + 1)
        col = "colD" + str(i + 1)
        rot = "rotD" + str(i + 1)
        fichero.write(pos)
        fichero.write(",")
        fichero.write(col)
        fichero.write(",")
        fichero.write(rot)
        fichero.write(",")
    fichero.write('\n')


def grabar_flujo(fases, lista):
     # Abrir fichero
    try:
        fichero = open('datos', 'a')
    except IOError:
        print('Error al abrir el fichero.')
    # Grabar cabeceras
    grabar_cabeceras_pre(fichero)
    # Grabar fase de práctica
    for item in fases[0]:
        # Grupo
        fichero.write(lista[0])
        fichero.write(',')
        # Sujeto
        fichero.write(lista[1])
        fichero.write(',')
        # Fase
        fichero.write("pr,")
        # Bloque
        fichero.write(" ,")
        # Bloque Origen
        fichero.write(" ,")
        # Tipo
        fichero.write(" ,")
        # Número
        fichero.write(" ,")
        # Posición Target
        fichero.write(str(item.devolver_posicion_outcome()))
        fichero.write(",")
        # Color Target
        grabar_color(fichero, item.devolver_color_outcome())
        # Rotación Target
        fichero.write(str(item.devolver_rotacion_outcome()))
        fichero.write(',')
        # Distractores
        distractores = item.devolver_distractores()
        for distractor in distractores:
            # Posición
            fichero.write(str(distractor.devolver_posicion()))
            fichero.write(",")
            # Color
            grabar_color(fichero, distractor.devolver_color())
            # Rotación
            fichero.write(str(distractor.devolver_rotacion()))
            fichero.write(",")
        fichero.write("\n")
    # Grabar fase de búsqueda
    bloque_actual = 0
    for bloque in fases[1]:
        bloque_actual += 1
        for item in bloque:
            # Grupo
            fichero.write(lista[0])
            fichero.write(',')
            # Sujeto
            fichero.write(lista[1])
            fichero.write(',')
            # Fase
            fichero.write("bu,")
            # Bloque
            fichero.write(str(bloque_actual))
            fichero.write(",")
            # Bloque Origen
            fichero.write(" ,")
            # Tipo
            tipo = item.devolver_tipo()
            fichero.write(tipo[0])
            fichero.write(" ,")
            # Número
            fichero.write(tipo[1:])
            fichero.write(",")
            # Posición Target
            fichero.write(str(item.devolver_posicion_outcome()))
            fichero.write(",")
            # Color Target
            grabar_color(fichero, item.devolver_color_outcome())
            # Rotación Target
            fichero.write(str(item.devolver_rotacion_outcome()))
            fichero.write(',')
            # Distractores
            distractores = item.devolver_distractores()
            for distractor in distractores:
                # Posición
                fichero.write(str(distractor.devolver_posicion()))
                fichero.write(",")
                # Color
                grabar_color(fichero, distractor.devolver_color())
                # Rotación
                fichero.write(str(distractor.devolver_rotacion()))
                fichero.write(",")
            fichero.write("\n")
    # Grabar fase de generación estándar
    bloque_actual = 0
    for bloque in fases[2]:
        bloque_actual += 1
        for item in bloque:
            # Grupo
            fichero.write(lista[0])
            fichero.write(',')
            # Sujeto
            fichero.write(lista[1])
            fichero.write(',')
            # Fase
            fichero.write("ge,")
            # Bloque
            fichero.write(str(bloque_actual))
            fichero.write(",")
            # Bloque Origen
            tipo = item.devolver_tipo()
            if tipo[0] != 'F':
                origen = int(item.devolver_id()) + 1
            else:
                origen = 100
            fichero.write(str(origen))
            fichero.write(',')
            # Tipo
            fichero.write(tipo[0])
            fichero.write(" ,")
            # Número
            fichero.write(tipo[1:])
            fichero.write(",")
            # Posición Target
            fichero.write(str(item.devolver_posicion_outcome()))
            fichero.write(",")
            # Color Target
            grabar_color(fichero, item.devolver_color_outcome())
            # Rotación Target
            fichero.write(str(item.devolver_rotacion_outcome()))
            fichero.write(',')
            # Distractores
            distractores = item.devolver_distractores()
            for distractor in distractores:
                # Posición
                fichero.write(str(distractor.devolver_posicion()))
                fichero.write(",")
                # Color
                grabar_color(fichero, distractor.devolver_color())
                # Rotación
                fichero.write(str(distractor.devolver_rotacion()))
                fichero.write(",")
            fichero.write("\n")
    # Grabar fase de generación incompleta
    bloque_actual = 0
    for bloque in fases[2]:
        bloque_actual += 1
        for item in bloque:
            # Grupo
            fichero.write(lista[0])
            fichero.write(',')
            # Sujeto
            fichero.write(lista[1])
            fichero.write(',')
            # Fase
            fichero.write("gi,")
            # Bloque
            fichero.write(str(bloque_actual))
            fichero.write(",")
            # Bloque Origen
            tipo = item.devolver_tipo()
            if tipo[0] != 'F':
                origen = int(item.devolver_id()) + 1
            else:
                origen = 100
            fichero.write(str(origen))
            fichero.write(',')
            # Tipo
            fichero.write(tipo[0])
            fichero.write(" ,")
            # Número
            fichero.write(tipo[1:])
            fichero.write(",")
            # Posición Target
            fichero.write(str(item.devolver_posicion_outcome()))
            fichero.write(",")
            # Color Target
            grabar_color(fichero, item.devolver_color_outcome())
            # Rotación Target
            fichero.write(str(item.devolver_rotacion_outcome()))
            fichero.write(',')
            # Distractores
            distractores = item.devolver_distractores()
            for distractor in distractores:
                # Posición
                fichero.write(str(distractor.devolver_posicion()))
                fichero.write(",")
                # Color
                grabar_color(fichero, distractor.devolver_color())
                # Rotación
                fichero.write(str(distractor.devolver_rotacion()))
                fichero.write(",")
            fichero.write("\n")
    # Separación de datos
    for i in range(3):
        for j in range(200):
            fichero.write("#")
        fichero.write("\n")
    fichero.close()


def grabar_instrucciones(fichero, lista, cod, tiempo):
    # Fecha ,hora,exp,grupo,sujeto,sexo,edad
    for item in lista:
        fichero.write(item)
        fichero.write(',')
    # Fase, bloque,bloque origen
    for i in range(3):
        fichero.write(' ,')
    # Código instrucción
    fichero.write(cod)
    fichero.write(',')
    # Tipo,número,respuesta,acierto
    for i in range(4):
        fichero.write(' ,')
    # Tiempo de espera
    fichero.write(str(tiempo))
    fichero.write(',')
    # Posición, color y rotación outcome y distractores
    for i in range(36):
        fichero.write(' ,')
    fichero.write('\n')


def grabar_tiempo_entre_bloques(fichero, lista, cod, tiempos):
    for tiempo in tiempos:
        # Fecha ,hora,exp,grupo,sujeto,sexo,edad
        for item in lista:
            fichero.write(item)
            fichero.write(',')
        # Fase, bloque,bloque origen
        for i in range(3):
            fichero.write(' ,')
        # Código instrucción
        fichero.write(cod)
        fichero.write(',')
        # Tipo,número,respuesta,acierto
        for i in range(4):
            fichero.write(' ,')
        # Tiempo de espera
        fichero.write(str(tiempo))
        fichero.write(',')
        # Posición, color y rotación outcome y distractores
        for i in range(36):
            fichero.write(' ,')
        fichero.write('\n')


def grabar_color(fichero, color):
    if color == 'amarillo':
        fichero.write('1,')
    elif color == 'azul':
        fichero.write('2,')
    elif color == 'rojo':
        fichero.write('3,')
    elif color == 'verde':
        fichero.write('4,')
    else:
        fichero.write(' ,')


def grabar_fase_practica(fichero, lista, fase, hour):
    # Asigno hora de inicio de la fase
    lista[1] = hour
    for item in fase:
        # Fecha ,hora,exp,grupo,sujeto,sexo,edad
        for elemento in lista:
            fichero.write(elemento)
            fichero.write(',')
        fichero.write('pr,')
        # Bloque
        fichero.write('1,')
        # Bloque origen,instrucciones,trial y numero
        for i in range(4):
            fichero.write(' ,')
        # Respuesta (z->l,m->r)
        if item.devolver_respuesta() == 'z':
            fichero.write('l,')
        else:
            fichero.write('r,')
        # Acierto
        fichero.write(str(item.devolver_correcto()))
        fichero.write(',')
        # Tiempo de respuesta
        fichero.write(str(item.devolver_tiempo_respuesta()))
        fichero.write(',')
        # Outcome posición,color y rotación
        fichero.write(str(item.devolver_posicion_outcome()))
        fichero.write(',')
        grabar_color(fichero, item.devolver_color_outcome())
        fichero.write(str(item.devolver_rotacion_outcome()))
        fichero.write(',')
        # Distractores
        distractores = item.devolver_distractores()
        for elem in distractores:
            fichero.write(str(elem.devolver_posicion()))
            fichero.write(',')
            grabar_color(fichero, elem.devolver_color())
            fichero.write(str(elem.devolver_rotacion()))
            fichero.write(',')
        fichero.write('\n')


def grabar_fase_busqueda(fichero, lista, fase, hour):
    bloque_actual = 1
    # Asigno hora de inicio de la fase
    lista[1] = hour
    for bloque in fase:
        bloque_actual += 1
        for item in bloque:
            # Fecha ,hora,exp,grupo,sujeto,sexo,edad
            for elemento in lista:
                fichero.write(elemento)
                fichero.write(',')
            # Fase
            fichero.write('bu,')
            # Bloque
            fichero.write(str(bloque_actual))
            fichero.write(',')
            # Bloque origen y instrucciones
            for i in range(2):
                fichero.write(' ,')
            # Tipo
            tipo = item.devolver_tipo()
            fichero.write(tipo[0])
            fichero.write(',')
            # Número
            fichero.write(tipo[1:])
            fichero.write(',')
             # Respuesta (z->l,m->r)
            if item.devolver_respuesta() == 'z':
                fichero.write('l,')
            else:
                fichero.write('r,')
            # Acierto
            fichero.write(str(item.devolver_correcto()))
            fichero.write(',')
            # Tiempo de respuesta
            fichero.write(str(item.devolver_tiempo_respuesta()))
            fichero.write(',')
            # Outcome posición,color y rotación
            fichero.write(str(item.devolver_posicion_outcome()))
            fichero.write(',')
            grabar_color(fichero, item.devolver_color_outcome())
            fichero.write(str(item.devolver_rotacion_outcome()))
            fichero.write(',')
            # Distractores
            distractores = item.devolver_distractores()
            for elem in distractores:
                fichero.write(str(elem.devolver_posicion()))
                fichero.write(',')
                grabar_color(fichero, elem.devolver_color())
                fichero.write(str(elem.devolver_rotacion()))
                fichero.write(',')
            fichero.write('\n')


def grabar_fase_generacion_estandar(fichero, lista, fase, condicion, hour):
    if condicion == '1':
        bloque_actual = 25
    else:
        bloque_actual = 13
    # Asigno hora de inicio de la fase
    lista[1] = hour
    for bloque in fase:
        bloque_actual += 1
        for item in bloque:
            # Fecha ,hora,exp,grupo,sujeto,sexo,edad
            for elemento in lista:
                fichero.write(elemento)
                fichero.write(',')
            # Fase
            fichero.write('ge,')
            # Bloque
            fichero.write(str(bloque_actual))
            fichero.write(',')
            # Bloque origen
            tipo = item.devolver_tipo()
            if tipo[0] != 'F':
                origen = int(item.devolver_id()) + 1
            else:
                origen = 100
            fichero.write(str(origen))
            fichero.write(',')
            # Instrucciones
            fichero.write(' ,')
            # Tipo
            fichero.write(tipo[0])
            fichero.write(',')
            # Número
            fichero.write(tipo[1:])
            fichero.write(',')
            # Respuesta (q->1,o->2,s->3,k->4)
            if item.devolver_respuesta() == 'q':
                fichero.write('1,')
            elif item.devolver_respuesta() == 'o':
                fichero.write('2,')
            elif item.devolver_respuesta() == 's':
                fichero.write('3,')
            elif item.devolver_respuesta() == 'k':
                fichero.write('4,')
            # Acierto
            fichero.write(str(item.devolver_correcto()))
            fichero.write(',')
            # Tiempo de respuesta
            fichero.write(str(item.devolver_tiempo_respuesta()))
            fichero.write(',')
            # Outcome posición,color y rotación
            fichero.write(str(item.devolver_posicion_outcome()))
            fichero.write(',')
            grabar_color(fichero, item.devolver_color_outcome())
            fichero.write(str(item.devolver_rotacion_outcome()))
            fichero.write(',')
            #fichero.write(',')
            # Distractores
            distractores = item.devolver_distractores()
            for elem in distractores:
                fichero.write(str(elem.devolver_posicion()))
                fichero.write(',')
                grabar_color(fichero, elem.devolver_color())
                fichero.write(str(elem.devolver_rotacion()))
                fichero.write(',')
            fichero.write('\n')


def grabar_fase_generacion_incompleta(fichero, lista, fase, condicion, hour):
    if condicion == '1':
        bloque_actual = 27
    else:
        bloque_actual = 15
    # Asigno hora de inicio de la fase
    lista[1] = hour
    for bloque in fase:
        bloque_actual += 1
        for item in bloque:
            # Fecha ,hora,exp,grupo,sujeto,sexo,edad
            for elemento in lista:
                fichero.write(elemento)
                fichero.write(',')
            # Fase
            fichero.write('gi,')
            # Bloque
            fichero.write(str(bloque_actual))
            fichero.write(',')
            # Bloque origen
            tipo = item.devolver_tipo()
            if tipo[0] != 'F':
                origen = int(item.devolver_id()) + 1
            else:
                origen = 100
            fichero.write(str(origen))
            fichero.write(',')
            # Instrucciones
            fichero.write(' ,')
            # Tipo
            fichero.write(tipo[0])
            fichero.write(',')
            # Número
            fichero.write(tipo[1:])
            fichero.write(',')
            # Respuesta (q->1,o->2,s->3,k->4)
            if item.devolver_respuesta() == 'q':
                fichero.write('1,')
            elif item.devolver_respuesta() == 'o':
                fichero.write('2,')
            elif item.devolver_respuesta() == 's':
                fichero.write('3,')
            elif item.devolver_respuesta() == 'k':
                fichero.write('4,')
            # Acierto
            fichero.write(str(item.devolver_correcto()))
            fichero.write(',')
            # Tiempo de respuesta
            fichero.write(str(item.devolver_tiempo_respuesta()))
            fichero.write(',')
            # Outcome posición,color y rotación
            fichero.write(str(item.devolver_posicion_outcome()))
            fichero.write(',')
            grabar_color(fichero, item.devolver_color_outcome())
            fichero.write(str(item.devolver_rotacion_outcome()))
            fichero.write(',')
            # Distractores
            distractores = item.devolver_distractores()
            for elem in distractores:
                fichero.write(str(elem.devolver_posicion()))
                fichero.write(',')
                grabar_color(fichero, elem.devolver_color())
                fichero.write(str(elem.devolver_rotacion()))
                fichero.write(',')
            fichero.write('\n')


def guardar_datos(fases, lista, t_i_i, t_f_p, t_i_b, l_f_b, t_i_g_e, l_f_g_e, \
                  t_i_g_i, l_f_g_i, start_phases):
    # Abrir fichero
    try:
        fichero = open('datos', 'a')
    except IOError:
        print('Error al abrir el fichero.')
    # Gabar cabeceras
    grabar_cabeceras(fichero)
    # ##########################################################################
    # ##################Grabar instrucciones iniciales##########################
    # ##########################################################################
    grabar_instrucciones(fichero, lista, 'inst_ini', t_i_i)
    # ##########################################################################
    # #############Grabar Resultados Fase Práctica##############################
    # ##########################################################################
    grabar_instrucciones(fichero, lista, 'dat_f_p', t_f_p)
    # ##########################################################################
    # #####################Grabar instrucciones experimentales##################
    # ##########################################################################
    grabar_instrucciones(fichero, lista, 'inst_exp', t_i_b)
    # ##########################################################################
    # #########Grabar tiempos de respuesta entre bloques Fase Búsqueda##########
    # ##########################################################################
    grabar_tiempo_entre_bloques(fichero, lista, 'tr_bus', l_f_b)
    # ##########################################################################
    # ############Grabar instrucciones generación estandar######################
    # ##########################################################################
    grabar_instrucciones(fichero, lista, 'inst_ge', t_i_g_e)
    # ##########################################################################
    # ####Grabar tiempos de respuesta entre bloques Fase Generación Estándar####
    # ##########################################################################
    grabar_tiempo_entre_bloques(fichero, lista, 'tr_ge', l_f_g_e)
    # ##########################################################################
    # #############Grabar instrucciones generación incompleta###################
    # ##########################################################################
    grabar_instrucciones(fichero, lista, 'inst_gi', t_i_g_i)
    # ##########################################################################
    # ###Grabar tiempos de respuesta entre bloques Fase Generación Incompleta###
    # ##########################################################################
    grabar_tiempo_entre_bloques(fichero, lista, 'tr_gi', l_f_g_i)
    # ##########################################################################
    # ######################Grabar fase práctica################################
    # ##########################################################################
    grabar_fase_practica(fichero, lista, fases[0], start_phases[0])
    # ##########################################################################
    # ########################Grabar fase de búsqueda###########################
    # ##########################################################################
    grabar_fase_busqueda(fichero, lista, fases[1], start_phases[1])
    # ##########################################################################
    # ######################Grabar fase de generación estándar##################
    # ##########################################################################
    # Lista de 3 contiene la condición experimental, calcular el bloque
    grabar_fase_generacion_estandar(fichero, lista, fases[2], lista[3], \
        start_phases[2])
    # ##########################################################################
    # ###################Grabar fase de generación incompleta###################
    # ##########################################################################
    grabar_fase_generacion_incompleta(fichero, lista, fases[3], lista[3], \
        start_phases[3])
    # Grabar tiempo de finalización de la tarea
    for i in range(52):
        if i == 1:
            fichero.write(start_phases[4])
            fichero.write(",")
        else:
            fichero.write(" ,")
    fichero.write("\n")
    # Separador
    for i in range(5):
        if i != 2:
            for j in range(200):
                fichero.write("#")
        fichero.write("\n")
    # Cerrar fichero
    fichero.close()


def separador_fichero():
    try:
        f = open('salida', 'a')
    except IOError:
        print('Error al abrir el fichero.')
    # Líneas
    for i in range(2):
        for j in range(200):
            f.write('*')
        f.write('\n')


'''CONJUNTO DE FUNCIONES PARA VALIDAR QUE LOS DISTRACTORES DE LOS
ENSAYOS DE LA FASE DE PRACTICA SEAN DISTINTOS A LOS DE LA FASE DE
BUSQUEDA'''


def ordenar_distractores(ensayo):
    # Función que devuelve una lista de distractores ordenados por posición
    distractores = ensayo.devolver_distractores()
    posiciones = ensayo.devolver_posiciones_distractores()
    lista = []
    for posicion in posiciones:
        for item in distractores:
            if posicion == item.devolver_posicion():
                lista.append(item)
    return lista


def chequear_distractores(object1, object2):
    # Función que comprueba que los distractores de ambos ensayos son distintos
    cont = 0
    d1 = ordenar_distractores(object1)
    d2 = ordenar_distractores(object2)
    for i in range(11):
        if d1[i].devolver_posicion() == d2[i].devolver_posicion() and \
            d1[i].devolver_color() == d2[i].devolver_color() and \
            d1[i].devolver_rotacion() == d2[i].devolver_rotacion():
                cont = cont + 1
        else:
            return False
    if cont == 11:
        return True


def chequear_fase_practica(f_p, f_b):
    # Función que recibe dos listas y comprueba que los distractores de los
    #  ensayos de la fase de práctica sean distintos a los de
    # la fase de búsqueda
    # f_p = fase de práctica y f_b = fase de búsqueda
    # obtener ensayos fijos
    fijos = []
    for item in f_b[0]:
        tipo = item.devolver_tipo()
        if tipo[0] == 'F':
            fijos.append(item)
    # obtener ensayos variables
    variables = []
    for bloque in f_b:
        for item in bloque:
            tipo = item.devolver_tipo()
            if tipo[0] == 'V':
                variables.append(item)
    # lista de distractores de la fase de práctica
    for ensayo in f_p:
        #iguales = False
        bucle = True
        while bucle == True:
            iguales = False
            # recorro los ensayos fijo
            for fijo in fijos:
                if chequear_distractores(ensayo, fijo) == True:
                    iguales = True
            # Si no hay coincidencia miro en los variables
            if iguales == False:
                for variable in variables:
                    if chequear_distractores(ensayo, variable) == True:
                        iguales = True
            # Al haber coincidencia genero una nueva lista de
            # distractores para el ensayo
            if iguales == True:
                color = ensayo.devolver_color_outcome()
                posicion = ensayo.devolver_posicion_outcome()
                ensayo.asignar_distractores(generar_lista_distractores(color, \
                        obtener_cuadrante(posicion), posiciones=[posicion]))
                bucle = True
            else:
                bucle = False
