"""
Por: Juan Felipe Borbón Melo
Fecha: 18/05/2025
Profesor: Frank Darwin Valencia Posso

"""

from sys import stdin


def buscar_raiz(padre, x):

    if padre[x] != x:
        padre[x] = buscar_raiz(padre, padre[x])
    return padre[x]


def union(padre, rango, size, x, y):

    root_x = buscar_raiz(padre, x)
    root_y = buscar_raiz(padre, y)
    
    if root_x == root_y:
        return
    
    if rango[root_x] < rango[root_y]:
        padre[root_x] = root_y
        size[root_y] += size[root_x]
    elif rango[root_x] > rango[root_y]:
        padre[root_y] = root_x
        size[root_x] += size[root_y]
    else:
        padre[root_y] = root_x
        size[root_x] += size[root_y]
        rango[root_x] += 1


def calcular_particiones():

    MOD = 1000000007
    tabla = [0] * 51
    tabla[0] = 1
    
    for i in range(1, 51):
        for j in range(i, 51):
            tabla[j] = (tabla[j] + tabla[j-i]) % MOD
    
    return tabla

def main():

    particiones = calcular_particiones()
    
    lines = stdin.readlines()
    index = 0
    
    t = int(lines[index].strip())
    index += 1
    
    for _ in range(t):
        n, m = map(int, lines[index].strip().split())
        index += 1
        
        padre = [i for i in range(n + 1)]
        rango = [0] * (n + 1)
        size = [1] * (n + 1)
        
        for _ in range(m):
            operacion = lines[index].strip().split()
            index += 1
            
            if operacion[0] == "union":
                x, y = int(operacion[1]), int(operacion[2])
                union(padre, rango, size, x, y)
            elif operacion[0] == "partitions":
                x = int(operacion[1])
                root = buscar_raiz(padre, x)
                set_size = size[root]
                print(particiones[set_size])

main()