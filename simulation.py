# Este archivo contiene la implementacion de la clase Simulation (11.11.10)
""" Un objeto de la clase Simulation representa un experimento en el que
se ejecuta un algoritmo distribuido sobre una grafica de comunicaciones """

from process import Process
from simulator import Simulator
# ----------------------------------------------------------------------------------------
class Simulation:                   # Descendiente de la clase "object" (default)
    """ Atributos: "engine", "graph", "table", contiene tambien un
    constructor y los metodos "setModel()", "init()", "run()" """
	
    def __init__(self, filename, maxtime):
        """ construye su motor de simulacion, la grafica de comunicaciones y
        la tabla de procesos """
        self.engine = Simulator(maxtime)

        #abre el archivo (grafo); lee linea por linea; cada linea la guarda en la lista lines
        f = open(filename)
        lines = f.readlines()
        f.close()
        self.graph = []
        for line in lines:
            fields = line.split()#en cada linea, separa los valores por el espacio vacio
            #guarda los valores en la lista fields
            neighbors = []#por cada linea del archivo, se crea un arreglo de neighbors
            for f in fields:
                neighbors.append(int(f))#se guarda cada valor en la lista neighbors
            self.graph.append(neighbors)#esta lista de valores se concatena al arreglo graph

        self.table  = [[]]          # la entrada 0 se deja vacia
        for i,row in enumerate(self.graph):
            newprocess = Process(row, self.engine, i+1)
            self.table.append(newprocess)
        		
    def setModel(self, model, id):
        """ asocia al proceso con el modelo que debe ejecutar y viceversa """
        process = self.table[id]
        process.setModel(model)
 		
    def init(self, event):
        """ inserta un evento semilla en la agenda """
        self.engine.insertEvent(event)

    def run(self):	
        """ arranca el motor de simulacion """
        while self.engine.isOn():
            nextevent = self.engine.returnEvent()
            target = nextevent.getTarget()
            nextprocess = self.table[target]
            nextprocess.setTime(nextevent.getTime())
            nextprocess.receive(nextevent)
