resultados = [
    ("Equipe A", [85, 90, 88]),
    ("Equipe B", [78, 82, 84]),
    ("Equipe C", [92, 88, 95]),
    ("Equipe D", [70, 75, 80]),
    ("Equipe E", [88, 90, 85])
]

medias = [(equipe[0], sum(equipe[1]) / len(equipe[1])) for equipe in resultados]

medias.sort(key=lambda x: x[1], reverse=True)

classificacao = [(equipe, media) for equipe, media in medias]

print("Classificação Final:")
for posicao, (equipe, media) in enumerate(classificacao, start=1):
    print(f"{posicao}. {equipe} - Média: {media:.2f}")
