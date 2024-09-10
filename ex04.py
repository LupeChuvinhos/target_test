faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

#Total
faturamento_total = sum(faturamento.values())

#Porcentagem
for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print(f"Percentual de {estado}: {percentual:.2f}%")