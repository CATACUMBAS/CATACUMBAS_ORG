from mapa import mapa_romenia

def busca_generica(grafo, inicio, objetivo):
    fronteira = [(0, inicio, [inicio])]
    visitados = set()

    while fronteira:
        fronteira.sort(key=lambda item: item[0])
        valor, atual, caminho = fronteira.pop(0)
        print(f'expandido {atual:16} valor={valor}')

        if atual == objetivo:
            return caminho, valor

        if atual not in visitados:
            visitados.add(atual)
            for vizinho, custo in grafo.get(atual, []):
                if vizinho not in visitados:
                    fronteira.append(
                        (valor + custo, vizinho, caminho + [vizinho])
                    )
    return None, float('inf')

    if __name__ == '__main__':
        caminho, custo = busca_generica(mapa_romenia, 'Arad', 'Bucharest')
        print(' -> '.join(caminho))
        print(f'{custo} km em {len(caminho) - 1} passos')