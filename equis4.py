import RPi.GPIO as IO #Importa librería RPi.GPIO para controlar puertos GPIO de la Raspberry
import time           #Importa librería de delays
IO.setwarnings(False) #Desactiva las advertencias
IO.setmode(IO.BCM)    #Activa númeración BCM de los puertos GPIO

                      #Pines de entrada
IO.setup(14,IO.IN)    #GPIO 14 ->Sensor del extremo izquierda entrada
IO.setup(15,IO.IN)    #GPIO 15 ->Sensor izquierda entrada
IO.setup(4,IO.IN)     #GPIO 4  ->Sensor derecha entrada
IO.setup(17, IO.IN)   #GPIO 17 ->Sensor del extremo derecha entrada

                      #Pines de salida
IO.setup(5,IO.OUT)    #GPIO 5 -> Motor 1 terminal A
IO.setup(6,IO.OUT)    #GPIO 6 -> Motor 1 terminal B

IO.setup(13,IO.OUT)   #GPIO 13 -> Motor Left terminal A
IO.setup(19,IO.OUT)   #GPIO 19 -> Motor Left terminal B

def adelante():                 #Función adelante
    IO.output(5,True) #1A+
    IO.output(6,False) #1B-

    IO.output(13,True) #2A+
    IO.output(19,False) #2B-
    
def reversa():                  #Función reversa
    IO.output(5,False) #1A+
    IO.output(6,True) #1B-

    IO.output(13,False) #2A+
    IO.output(19,True) #2B-

def derecha():                  #Función derecha 
    IO.output(5,True) #1A+
    IO.output(6,False) #1B-

    IO.output(13,False) #2A+
    IO.output(19,True) #2B-

def izquierda():                #Función izquierda
    IO.output(5,False) #1A+
    IO.output(6,True) #1B-

    IO.output(13,True) #2A+
    IO.output(19,False) #2B-
 
def freno():                    #Función freno
    IO.output(5,True) #1A+
    IO.output(6,True) #1B-

    IO.output(13,True) #2A+
    IO.output(19,True) #2B-
     
     
try:
    while (True):
        if(IO.input(14)==True and IO.input(15)==True and IO.input(4)==False and IO.input(17)==True):   #Giro hacia la derecha
            
            derecha()
            
            
        elif(IO.input(14)==True and IO.input(15)==False and IO.input(4)==True and IO.input(17)==True): #Giro hacia la izquierda
           
            izquierda()
            

        elif(IO.input(14)==False and IO.input(15)==True and IO.input(4)==True and IO.input(17)==True): #Giro hacia la izquierda
            
            izquierda()
            

        elif(IO.input(14)==True and IO.input(15)==True and IO.input(4)==False and IO.input(17)==True): #Giro hacia la derecha
            
            derecha()
           

	#elif(IO.input(14)==False and IO.input(15)==True and IO.input(4)==True and IO.input(17)==True): 
            #freno()
	    #time.sleep(0.10)
            #derecha()
            #time.sleep(0.10)

	elif(IO.input(17)==False): #Giro de 90 grados

	    while(IO.input(15)==True):
    	     derecha()


          
        else:
            
            adelante()

finally:
	IO.cleanup() #Limpiar puertos GPIO al finalizar el programa
