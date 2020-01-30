import numpy as np 
import random as rn 

def procesa(inicio, final, iteraciones):
    global prob 
    y = []
    for x in range(6):
        y.append(prob[x][final])

    final = []
    valor = []
    for i in range(iteraciones):
        for m in range(6):
            mult = (prob[inicio][m]) * rn.choice(y)
            final.append(mult)
            valor.append(mult)
    
    return rn.choice(valor)

# estados posible
# 0 = se gradua
# 1 = abandona
# 2 = primer anio
# 3 = segundo anio
# 4 = tercer anio
# 5 = cuarto anio
estados = [0,1,2,3,4,5]

# matriz de probabilidades
prob = [[1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0.2, 0.15, 0.65, 0, 0],
        [0, 0.15, 0, 0.1, 0.75, 0],
        [0, 0.1, 0, 0, 0.05, 0.85],
        [0.9, 0.05, 0, 0, 0, 0.05]]

###########################################

print 'a)'
# CALCULA PROBABILIDADES DE QUE UN ESTUDIANTE DE 2 ANIO SE GRADUE Y DE QUE ABANDONE ANTES DE GRADUARSE
print "Probabilidad de que se gradue: %.5f" % procesa(3, 0, 1)
print "Probabilidad de que se abandone: %.5f" % procesa(3, 1, 1)

###########################################

print 'b)'
# CALCULA PROBABILIDAD DE QUE EN 600 ESTUDIANTES NO SE GRADUARAN (AFIRMA Q ES 50%)
graduen = procesa(2,1,600) * 100
print ("Probabilidad de que 600 estudiantes no se graduen: %.5f" % graduen)

###########################################

print 'c)'
# CALCULA PROBABILIDAD DE QUE EN 2000 ESTUDIANTES NO SE GRADUARAN
graduan_total = []

# 600 DE PRIMER ANIO
primero = procesa(2,0,600)
graduan_total.append(primero)
# 520 DE SEGUNDO ANIO
segundo = procesa(3,0,520)
graduan_total.append(segundo)
# 460 DE TERCER ANIO
tercero = procesa(4,0,460)
graduan_total.append(tercero)
# 420 DE CUARTO ANIO
cuarto = procesa(5,0,420)
graduan_total.append(cuarto)

general = np.mean(graduan_total)

print ("Probabilidad de que 2000 estudiantes se graduen: %.5f" % general)

