# ia_trabalho_buscas

## 🗺 MAPA
- Coordenadas inteiras
- Quadrante superior do plano cartesiano:
```plain
y+
|
|
|
|__________x+
```
- Tamanho do mapa é 30x30(900 células)
- Algumas células possuem rótulos especiais como "mercado", "farmácia"...
    - Generalizar os estados do espaço como: (x, y, rótulo(opcional))

## 🤖 AGENTE
- Ações: Norte (+1, 0), Sul (-1, 0), Leste (0, +1), Oeste (0, -1)
- Em alguns casos as ações terão custo (algumas variando com a profundidade)

## 🔎 FUNÇÕES HEURÍSTICAS
- Usadas nos algoritmos Busca Gulosa e A* 
- (H1) Distância Euclidiana : 10*sqrt(pow(abs(x1-x2),2)-pow(abs(y1-y2),2))
- (H2) Distância Manhattan : 10*abs(x1-x2)+abs(y1-y2)
- A multiplicação por 10 pois cada ação vale 10

## 📤 SAIDAS DO CÓDIGO
1. Estado inical
2. Objetivo da busca
3. Caminho / Erro
4. Custo do Caminho / null 
5. Quantidade de nós gerados
6. Quantidade de nós visitados
--- Saídas Opcionais (verbose) ---
7. Algoritmo utilizado (DFS, BFS, UCS, Greedy, A*)
8. Função de custo (C1, C2, C3, C4)
9. Heurísticas (H1, H2)

## 🧾 REQUISITOS DA IMPLEMENTAÇÃO (Definido por Gurgel)
- Apresentar boa documentação
- Apresentar um README.md explicando como rodar cada experimento
- Deve emitir uma saída para cada entrada de:
    1. Algoritmo de busca
    2. Estado inical
    3. Objetivo da busca
    4. Função de custo
    5. Heurística (Só para os algoritmos Greedy, A*)