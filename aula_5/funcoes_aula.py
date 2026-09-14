from mapa import mapa_romenia, heuristica_bucareste

# O deque foi uma forma "elegante" que achei de adcionar e remover itens de uma lista
from collections import deque

def estradas(mapa_estradas):
    menos_estradas = min(mapa_estradas.values())
    mais_estradas = max(mapa_estradas.values())

    cidades_com_mais = [chave for chave, valor in mapa_estradas.items() if valor == mais_estradas]
    cidades_com_menos = [chave for chave, valor in mapa_estradas.items() if valor == menos_estradas]

    return cidades_com_mais, cidades_com_menos

def grau(grafo):
    vizinhos_cidade = {}
    for cidade, vizinhos in grafo.items():
        vizinhos_cidade[cidade] = len(vizinhos)

    mais_estradas, menos_estradas = estradas(vizinhos_cidade)
    print(f'\nCidade com mais estrada: {mais_estradas} \nCidade com menos estradas: {menos_estradas}\n')
    return vizinhos_cidade

def cidades_alcancaveis(grafo, inicio, k):
    k = int(k)
    visitados = {inicio}
    alcance = {i: [] for i in range(1, k + 1)}

    fila = deque([(inicio, 0)])

    while fila:
        cidade_atual, estradas = fila.popleft()

        if estradas >= k:
            continue

        for vizinho, _ in grafo.get(cidade_atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                novo_nivel = estradas + 1

                alcance[novo_nivel].append(vizinho)

                fila.append((vizinho, novo_nivel))

    return alcance

def verificar_simetria(grafo):
    for a, conexao in grafo.items():
        for b, peso in conexao:
            if b not in grafo:
                return False

            caminho_volta = any(
                origem == a and peso_volta == peso
                for origem, peso_volta in grafo[a]
            )

            if not caminho_volta:
                return False

    return True



vizinhos_por_cidade = grau(mapa_romenia)
print(vizinhos_por_cidade)

resultado = cidades_alcancaveis(mapa_romenia, 'Arad', 2)

for estradas, cidades in resultado.items():
    print(f"Com exatas {estradas} estrada(s) você chega em: {cidades}")

print(f'\né simetrico? {verificar_simetria(mapa_romenia)}')

'''
 6 - A principal diferença é que append modifica a lista original enquanto 'caminho + [vizinho];' cria uma copia, justamente se voce quer preservar os dados originais o aconselhavel é usar a segunda opcção mas se quiser performance e 'economia' de memoria o melhor seria a primeira opção

'''