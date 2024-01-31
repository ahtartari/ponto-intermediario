import math

def distancia_entre_pontos(ponto1, ponto2):
    # ponto1 e ponto2 devem ser tuplas ou listas contendo as coordenadas (x, y, z)
    return math.sqrt((ponto2[0] - ponto1[0]) ** 2 + (ponto2[1] - ponto1[1]) ** 2 + (ponto2[2] - ponto1[2]) ** 2)

def ponto_intermediario(ponto1, ponto2, correcao):
    distancia_original = distancia_entre_pontos(ponto1, ponto2)
    proporcao = (distancia_original - correcao) / distancia_original

    ponto_intermediario = (
        ponto1[0] + proporcao * (ponto2[0] - ponto1[0]),
        ponto1[1] + proporcao * (ponto2[1] - ponto1[1]),
        ponto1[2] + proporcao * (ponto2[2] - ponto1[2])
    )

    ponto_intermediario_formatado = tuple(round(coord, 3) for coord in ponto_intermediario)
    return ponto_intermediario_formatado


# Exemplo de uso
ponto1 = (0, 0, 0)
ponto2 = (1, 1, 0)
correcao1 = 1
correcao2 = 0.25

correcao = correcao1 + correcao2

distancia = distancia_entre_pontos(ponto1, ponto2)
ponto3 = ponto_intermediario(ponto1, ponto2, correcao)

print(f'Distância entre {ponto1} e {ponto2}: {distancia:.2f}')
print(f'Ponto intermediário: {ponto3}')