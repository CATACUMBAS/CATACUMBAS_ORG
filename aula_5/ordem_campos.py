from mapa import heuristica_bucareste

h = heuristica_bucareste
g = 140

item_guloso = (h['Sibiu'], 'Sibiu', ['Arad', 'Sibiu'])

item_a_estrela = (g + h['Sibiu'], g, 'Sibiu', ['Arad', 'Sibiu'])

print(item_guloso[0], item_a_estrela[0])

valor_h, cidade, caminho = item_guloso
valor_f, g_ate_aqui, cidade, caminho = item_a_estrela
print(valor_f, g_ate_aqui, cidade, caminho)