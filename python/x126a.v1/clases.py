# -*- coding: utf-8 *-*

'''Clase que recoge la posición, color y orientación de los elementos mostrados
en la tarea (outcome y distractores
'''


class Elemento:

    def __init__(self, pos, color, ori):
        self.__posicion = pos
        self.__color = color
        self.__rotacion = ori

    def cambiar_posicion(self, pos):
        self.__posicion = pos

    def cambiar_color(self, color):
        self.__color = color

    def cambiar_rotacion(self, ori):
        self.__rotacion = ori

    def devolver_posicion(self):
        return self.__posicion

    def devolver_color(self):
        return self.__color

    def devolver_rotacion(self):
        return self.__rotacion

    def mostrar_elemento(self):
        print(self.__posicion, self.__color, self.__rotacion)


    def devolver_elemento(self):
        return self


#Clase que define un ensayo.


class Ensayo:

    def __init__(self, tipo=None, posicion=None, color=None, grados=None,\
    distractores=None, id=None):

        if tipo is None:
            self.__tipo = ""
        else:
            self.__tipo = tipo
        if posicion is None and color is None and grados is None:
            self.__outcome = Elemento(posicion, color, grados)
        else:
            self.__outcome = Elemento(posicion, color, grados)
        if distractores is None:
            self.__distractores = []
        else:
            self.__distractores = distractores[:]
        self.__respuesta = 0
        self.__correcto = 0
        self.__tiempo_respuesta = 0
        self.__id = id

    def __del__(self):
        del(self)

    def asignar_tipo(self, tipo):
        self.__tipo = tipo

    def asignar_outcome(self, out):
        self.__outcome = out

    def asignar_posicion_outcome(self, posicion):
        self.__outcome.cambiar_posicion(posicion)

    def asignar_rotacion_outcome(self, rotacion):
        self.__outcome.cambiar_rotacion(rotacion)

    def asignar_color_outcome(self, color):
        self.__outcome.cambiar_color(color)

    def asignar_distractores(self, lista):
        self.__distractores = lista[:]

    def asignar_distractor(self, distractor):
        self.__distractores.append(distractor)

    def asignar_respuesta(self, respuesta):
        self.__respuesta = respuesta

    def asignar_correcto(self, correcto):
        self.__correcto = correcto

    def asignar_tiempo_respuesta(self, tiempo):
        self.__tiempo_respuesta = tiempo

    def asignar_id(self, id):
        self.__id = id

    def devolver_ensayo(self):
        return self

    def devolver_tipo(self):
        return self.__tipo

    def devolver_outcome(self):
        return self.__outcome

    def devolver_posicion_outcome(self):
        return self.__outcome.devolver_posicion()

    def devolver_rotacion_outcome(self):
        return self.__outcome.devolver_rotacion()

    def devolver_color_outcome(self):
        return self.__outcome.devolver_color()

    def devolver_distractores(self):
        return self.__distractores

    def devolver_posiciones_distractores(self):
        posiciones = []
        for item in self.__distractores:
            posiciones.append(item.devolver_posicion())
        posiciones.sort()
        return posiciones

    def devolver_respuesta(self):
        return self.__respuesta

    def devolver_correcto(self):
        return self.__correcto

    def devolver_tiempo_respuesta(self):
        return self.__tiempo_respuesta

    def devolver_id(self):
        return self.__id

    def mostrar_ensayo(self):
        print(self.__id)
        print(self.__tipo)
        self.__outcome.mostrar_elemento()
        for i in range(len(self.__distractores)):
            self.__distractores[i].mostrar_elemento()
        print(self.__respuesta)
        print(self.__correcto)
        print(self.__tiempo_respuesta)
