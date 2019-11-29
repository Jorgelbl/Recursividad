# se declara la clase determinar matriz
class DeterminarMatriz:

    # se creo el metodo determinante
    def determinante_rec(self, matriz):
        # se utilizo un ciclo de decicion if-else
        if len(matriz) == 1:
            result = matriz[0][0]
        elif len(matriz) == 2:
            result = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        else:
            result = 0
            i = 0
            sig = +1
            # se utilizo un clico while para realizar dicho proceso
            while i < len(matriz):
                mm = (matriz, i, 0)
                result += sig * matriz[i][0] * DeterminarMatriz(mm)
                sig = - sig
                i += 1
        # se retornan valores
        return result


# resultados
deter = DeterminarMatriz()
matriz = [[0, 1, 3], [1, 2, 3], [2, 0, 1]]
M = deter.determinante_rec((matriz))
print(M)

