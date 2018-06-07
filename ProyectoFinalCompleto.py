import RPi.GPIO as IO #Llamando a librería de los puertos GPIO
import time           #Importar librería delays
IO.setwarnings(False) #Apagar advertancias
IO.setmode(IO.BCM)    #Modo de pines Broadcom

                    #  Pines de entrada de la Raspberry
IO.setup(14,IO.IN)  #    
IO.setup(15,IO.IN)  #
IO.setup(4,IO.IN)   #
IO.setup(17,IO.IN)  #
                    #  Pines de salida hacía el puente en H
IO.setup(5,IO.OUT)  #  Terminal de Motor 1 A  IZQUIERDO  
IO.setup(6,IO.OUT)  #  Terminal de Motor 1 B  IZQUIERDO
IO.setup(13,IO.OUT) #  Terminal de Motor 2 A  DERECHO
IO.setup(19,IO.OUT) #  Terminal de Motor 2 B  DERECHO

if(IO.input(14)==True and IO.input(15)==False and IO.input(4)==False and IO.input(17)==True): #Movimiento hacia adelante
	IO.output(5,True)   #1A+ Motor 1 encendido hacia adelante
	IO.outpu(6,False)   #1B-

	IO.output(13,True)  #2A+ Motor 2 encendido hacia adelante
	IO.output(19,False) #2B-

elif(IO.input(14)==True and IO.input(15)==True): #Girar a la derecha
	IO.output(5,True)   #1A+
	IO.output(6,True)   #1A-

	IO.output(13,True)  #2A+
	IO.output(19,False) #2A-

elif(IO.input(4)==True and IO.input(17)==True): #Girar a la izquierda
	IO.output(5,True)   #1A+
	IO.output(6,False)	#1A-
	
	IO.output(13,True)  #2B+
	IO.output(19,True)  #2B-

elif(IO.input(14)==True and IO.input(15)==True and IO.input(4)==True and IO.input(17)==True): #Girar hasta encontrar una línea
	 IO.output(5,True)   #1A+
	IO.output(6,True)   #1A-

	IO.output(13,True)  #2A+
	IO.output(19,False) #2A-

IO.cleanup() #Limpiar puertos al finalizar el programa