def calcular_desconto(t, casos):
    resultados = []
    for i in range(t):
        n = casos[i][0]
        precos = casos[i][1]
        
        # Ordena os preços em ordem decrescente
        precos.sort(reverse=True)
        
        desconto_total = 0
        # Itera a cada terceiro item, somando o preço ao desconto total
        for j in range(2, n, 3):
            desconto_total += precos[j]
        
        resultados.append(desconto_total)
    return resultados

# Leitura de entrada
t = int(input())
casos = []
for _ in range(t):
    n = int(input())
    precos = list(map(int, input().split()))
    casos.append((n, precos))

# Calcula o desconto para cada caso e imprime o resultado
resultados = calcular_desconto(t, casos)
for resultado in resultados:
    print(resultado)
