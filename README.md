# Desafio de Desconto Máximo em Compras

Este projeto resolve o problema de cálculo do desconto máximo que Lindsay, uma compradora compulsiva, pode obter ao comprar itens em uma promoção de "pague 2, leve 3". O código lê o número de itens e os preços e calcula o maior desconto possível seguindo a regra de selecionar o item mais barato como o item grátis a cada três itens.

## Descrição do Problema

Lindsay participa de uma promoção onde, para cada três itens comprados, o mais barato é gratuito. Dado o número de itens e seus respectivos preços, precisamos calcular o desconto máximo aplicável ao valor total de sua compra. Cada caso de teste consiste em um número de itens seguido de uma lista dos preços dos itens.

### Exemplo de Entrada

```
1
6
400 100 200 350 300 250
```

### Exemplo de Saída

```
400
```

## Explicação da Solução

Para resolver o problema, seguimos a seguinte lógica:

1. **Organizar os Preços**: Ordenamos os preços dos itens em ordem decrescente, para garantir que os itens mais caros fiquem no início.
  
2. **Calcular o Desconto**: Percorremos a lista e selecionamos a cada grupo de três itens o item mais barato para aplicar o desconto. Como os itens estão ordenados do maior para o menor, o terceiro item de cada conjunto de três é sempre o mais barato daquele grupo e, portanto, é o item "gratuito".

3. **Iteração**: Calculamos o desconto em grupos de três, somando o preço do terceiro item de cada grupo até o final da lista de preços.

## Estrutura do Código

### Função `calcular_desconto_maximo`

Essa função recebe a lista de preços e calcula o desconto máximo possível.

```python
def calcular_desconto_maximo(precos):
    precos.sort(reverse=True)
    desconto = sum(precos[i] for i in range(2, len(precos), 3))
    return desconto
```

### Função Principal

Lê os dados de entrada, processa cada caso de teste e exibe o desconto máximo para cada um.

```python
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        precos = list(map(int, input().split()))
        print(calcular_desconto_maximo(precos))
```

## Como Executar o Código

1. Salve o código em um arquivo chamado `desconto_maximo.py`.
2. Execute o código em um ambiente Python com o comando:
   ```bash
   python desconto_maximo.py
   ```
3. Insira o número de cenários e as listas de preços conforme solicitado.

## Exemplo de Uso

Para a entrada:
```
1
6
400 100 200 350 300 250
```

O código retornará:
```
400
```

## Observações

- Este código supõe que os itens são positivos e que o número de itens e os valores de cada item estão dentro dos limites especificados.
- O código tem uma complexidade de `O(n log n)`, devido à ordenação dos preços, o que é eficiente o suficiente para o limite dado no problema.
