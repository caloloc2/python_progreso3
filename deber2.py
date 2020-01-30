import random
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def funcion_a_evaluar(x):
    # funcion a evaluar
    return (-1*(0.1 + pow((1-x), 2) - (0.1*(math.cos((6*math.pi)*(1-x)))))) + 2

def graficar():
    x = np.arange(0, 200, 0.01)
    f = []
    for i in range(200):            
        f.append(funcion_a_evaluar(x[i]))
    # Dibuja la funcion
    plt.plot(f)
    plt.show()

def evalua_iteraciones(poblacion):
    # evalua cada iteracion de los valores de la funcion para determinar el maximo de la funcion
    scores = []
    total = 0
    for individual in poblacion:        
        r = funcion_a_evaluar(individual[0])
        scores.append(r)
        total += r        
    avg = total / len(scores)
    return scores, avg

def mutar(individual):
    new = []
    for attribute in individual:
        new.append(attribute + random.normalvariate(0, attribute + .1))  # Crea un factor aleatorio de una distribucion normal
    return new

def busca_maximo(poblacion):
    # dependiendo de la poblacion creada geneticamente, regresa el mejor valor 
    best = None
    val = None
    for individual in poblacion:        
        r = funcion_a_evaluar(individual[0])
        try:
            if r > val:
                best = individual
                val = r
        except:
            best = individual
            val = r        
    return best, val

def inicia_matriz(n, p):
    # crea la poblacion creada geneticamente
    pop = [[0] * n]
    for i in range(p):
        pop.append(mutar(pop[0]))
    return pop

if __name__ == "__main__":
    if len(sys.argv) != 5: # Verifica q se ingresen todos los parametros
        print("Error: Debe ingresar 4 parametros => ind_size, n_ind, n_gen, p_mut")
        exit()
    
    n_ind = int(sys.argv[1])
    ind_size = int(sys.argv[2])
    n_gen = int(sys.argv[3])
    p_mut = float(sys.argv[4])

    poblacion = inicia_matriz(n_ind, ind_size)

    for iteration in range(n_gen):
        scores, avg = evalua_iteraciones(poblacion)
        deleted = 0
        nueva_poblacion = []
        for i in range(len(poblacion)):
            if scores[i] < avg:
                deleted += 1
            else:
                nueva_poblacion.append(poblacion[i])
        for i in range(deleted):
            nueva_poblacion.append(mutar(nueva_poblacion[i % len(nueva_poblacion)]))
        poblacion = nueva_poblacion
        
    best, val = busca_maximo(poblacion)

    print("Best individual : ", round(val, 5))

    graficar()