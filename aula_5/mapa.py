
mapa_romenia = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99),
              ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146),
                ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146),
                       ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138),
                ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101),
                  ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142),
                 ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

heuristica_bucareste = {
    'Arad' : 366, 'Bucharest' : 0, 'Craiova': 160, 'Drobeta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

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
    print(f'Cidade com mais estrada: {mais_estradas} \n Cidade com menos estradas: {menos_estradas}')
    return vizinhos_cidade
    

def vizinhos_de(grafo, cidade):
    return grafo.get(cidade, [])

def custo_do_caminho(grafo, caminho):
    total = 0
    for i in range(len(caminho) - 1 ):
        for vizinho, custo in grafo[caminho[i]]:
            if vizinho == caminho[i + 1]:
                total += custo
                break
    return total

if __name__ == '__main__':
    print('cidades:', len(mapa_romenia))

    print(vizinhos_de(mapa_romenia, 'Sibiu'))

    print(vizinhos_de(mapa_romenia, 'Lugano'))

    print(custo_do_caminho(mapa_romenia, ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']))

    print(custo_do_caminho(mapa_romenia, ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']))

    print(custo_do_caminho(mapa_romenia, ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']))

    vizinhos_por_cidade = grau(mapa_romenia)
    print(vizinhos_por_cidade)




fronteira = [
    (366, 'Arad'),
    (253, 'Sibiu'),
    (329, 'Timisoara'),
    (374, 'Zerind')
]

fronteira.sort(key=lambda item: item[0])
# print(fronteira[0])

melhor = fronteira.pop(0)
# print(melhor, len(fronteira))

def chave(item):
    return item[0]

fronteira.sort(key=chave)

# print(fronteira)

# print(sorted(fronteira, key=lambda item: item[1]))