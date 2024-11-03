import numpy as np

tempo = np.full((4, 4), None)

tempo[0] = ['PILOTO', 'VOLTA 1', 'VOLTA 2', 'VOLTA 3']
tempo[1] = ['Francisco', 7, 8, 10]
tempo[2] = ['Camila', 4, 6, 7]
tempo[3] = ['Billy', 10, 4, 8]

print(tempo)

dicPiloto = {}

for i in range(1, 4):
    piloto = tempo[i][0]
    dicPiloto[piloto] = np.sum(tempo[i][1:])

print(dicPiloto)