from numpy import matrix

# matriz de probabilidades
prob = matrix([[1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0.2, 0.15, 0.65, 0, 0],
        [0, 0.15, 0, 0.1, 0.75, 0],
        [0, 0.1, 0, 0, 0.05, 0.85],
        [0.9, 0.05, 0, 0, 0, 0.05]])

def analiza(inicio, fin, pasos, itera):
    global prob

    # estados posibles
    # 0 = se gradua
    # 1 = abandona
    # 2 = primer anio
    # 3 = segundo anio
    # 4 = tercer anio
    # 5 = cuarto anio
    estados = [0,1,2,3,4,5]

    # rota la matriz de probabilidades
    inv = prob.T

    # estado actual
    estado = matrix ([[0], [0], [0], [0], [0], [0]])
    estado[inicio][0] = 1 # selecciona el estado actual

    # repite el numero de veces necesarias
    for i in range(itera):
        # multiplica la matriz por cada uno de los estados obtenidos
        for veces in range(pasos):
            estado = inv * estado

    # print estado
    return estado[fin][0]

# item 1
# a
graduan = float(analiza(3, 0, 3, 1)) * 100  # prob de q estudiantes de 2 anio puedan graduarse
abandonan = float(analiza(3, 1, 3, 1)) * 100 # prob de q estudiantes de 2 anio no se graduen
print "se graduan: " + str(graduan)
print "abandonan: " + str(abandonan)

# item 2
abandonan = float(analiza(2, 1, 4, 600)) * 100 # prob de q 600 est de 1 anio no se graduen
print "600 estudiantes abandonan: " + str(abandonan)

# item 3
prob_uni = 0
prob_uni += float(analiza(2, 0, 4, 600)) # prob de q 600 est de 1 anio se graduen
prob_uni += float(analiza(3, 0, 3, 520)) # prob de q 520 est de 2 anio se graduen
prob_uni += float(analiza(4, 0, 2, 460)) # prob de q 460 est de 3 anio se graduen
prob_uni += float(analiza(5, 0, 1, 420)) # prob de q 420 est de 4 anio se graduen

prom = (prob_uni / 4) * 100 # obtiene promedio y porcentaje

print "2000 estudiantes puedan graduarse: " + str(prom)