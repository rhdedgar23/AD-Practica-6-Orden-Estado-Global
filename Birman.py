# Este archivo implementa la simulacion del algoritmo de 
# difusion de informacion con retroalimentacion (Propagation of Information with Feedback) de A. Segall

import sys
from event import Event
from model import Model
from process import Process
from simulator import Simulator
from simulation import Simulation

class AlgorithmBirman(Model):
    # Esta clase desciende de la clase Model e implementa los metodos
    # "init()" y "receive()", que en la clase madre se definen como abstractos
  
    def init(self):
        # Aqui se definen e inicializan los atributos particulares del algoritmo
        print("Inicio funciones [", self.id, "]")

        print("Mis vecinos son: ", end=" ")
        for neighbor in self.neighbors:
            print(neighbor, end=" ")
        print(" ")

        # Se inicializa el reloj vectorial
        self.relojVectorial = [0] * (len(self.neighbors) + 1)
        print("Mi reloj vectorial es: ", self.relojVectorial)

        # Lista para mensajes que esperan
        self.mensajesDiferidos = []
        print("Mi lista de mensajes diferidos es: ", self.mensajesDiferidos)

        self.vecinos = self.neighbors


    def receive(self, event):
        # Aqui se definen las acciones concretas que deben ejecutarse cuando se
        # recibe un evento
        print("T = ", self.clock, " Nodo [", self.id, "] Recibo :", event.getName(), "desde [", event.getSource(), "]")



# ----------------------------------------------------------------------------------------
# "main()"
# ----------------------------------------------------------------------------------------
# construye una instancia de la clase Simulation recibiendo como parametros el nombre del 
# archivo que codifica la lista de adyacencias de la grafica y el tiempo max. de simulacion

if len(sys.argv) != 2:
    print("Por favor dame el nombre del archivo con la grafica de comunicaciones")
    raise SystemExit(1)

maxtime= 100
experiment = Simulation(sys.argv[1], maxtime)#filename, maxtime

# imprime lista de nodos que se extraen del archivo
# experiment.graph[indice+1 == nodo] == vecino
print("Lista de nodos: ", experiment.graph)

# asocia un pareja proceso/modelo con cada nodo de la grafica
for i in range(1,len(experiment.graph)+1):
    m = AlgorithmBirman()
    experiment.setModel(m, i)

# inserta un evento semilla en la agenda y arranca
seed = Event("INICIA", 0.0, 1, 1)#name, time, target, source
experiment.init(seed)
experiment.run()
