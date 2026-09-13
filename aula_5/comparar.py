from mapa import mapa_romenia, heuristica_bucareste

h = heuristica_bucareste

def busca(grafo, inicio, objetivo, prioridade):
    fronteira = [(0,0, inicio, [inicio])]
    visitados = set()

    while fronteira:
        fronteira.sort(key=lambda item: item[0])
        chave, g, atual, caminho = fronteira.pop(0)

        if atual == objetivo:
            return caminho, g

        if atual not in visitados:
            return caminho, g

        if atual not in visitados:
            visitados.add(atual)
            for vizinho, custo in grafo.get(atual, []):
                novo_g = g + custo
                passos = len(caminho)
                fronteira.append((prioridade(novo_g, vizinho, passos), novo_g, vizinho, caminho + [vizinho]))

    return None, float('inf')


