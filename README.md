# Projeto Dino - Bernardo Mello Correia Lima

Esse projeto foi criado com o propósito de criar uma inteligência artificial para o jogo do Google o qual um dinossauro deve correr enquanto desviando de cactus e pterodatilos.
O projeto foi feito como atividade pontuada para a matéria de Tópicos Avançados de Inteligência Artificial.

# Algoritimos Escolhidos

- Para a execução do projeto, foi escolhido a técnica de Multi-Layer-Perceptron, utilizando os parâmetros de distância, velocidade e altura adquirido pelo comando get_state() para alimentar as camadas da rede neural. O código para o perceptron está sendo usado da seguinte maneira:

![image](https://github.com/user-attachments/assets/a45489b6-e858-4f49-a653-a92e66895785)

# Treinamento - Resolução

Para o processo de treinamento, foi definido um escopo de 100 dinossauros que irão correr ao mesmo tempo. 

```python
fps = 0
dino_count = 100
dead_dinos = 0
```

Cada um deles possuirá um genoma randomizado o qual cada posição do genoma está representando um valor de peso que será usado no processo de verificação no MLP.

```python
class Dino():
    genoma = [-744, 149, 728, -956, 82, 993, 833, -853, -843, 556] # 522
    altura = 0
    velocidade = 0
    distancia = 0
    score = 0
    next_step = ACTION_FORWARD
    mutation_scale = 5

    def randomizar_genoma(self):
        self.genoma = [random.randint(-1000, 1000) for _ in range(10)]
        pass
```

```python
def instanciar_prim_dinos(_dino_count):
    result = []
    for dino in range(_dino_count):
        dino = Dino()
        dino.randomizar_genoma()
        result.append(copy.deepcopy(dino))

    return result
```

A seguir está um vídeo demonstrando o processo de treino da primeira geração:

https://github.com/user-attachments/assets/c35f3f8e-1be7-44e5-926c-ca869d91d448

Quando todos os dinossauros morrerem, será feito o processo de seleção o qual o programa irá buscar o dinossauro que possuiu o melhor score durante a partida. Ele irá armazenar o genoma desse dinossauro e criar um novo escopo de 100 dinossauros com a mesma sequência de genomas.

```python
def check_all_dead(_game):
    for dino in _game.player_dinos:
        if not dino.is_dead:
            return False
        
    return True
```

```python
def get_bestest_score(_game, gen, best_score):
    scores = _game.get_scores()
    pos = 0
    _best_score = 0
    for x, dino_score in enumerate(scores):
        if best_score < dino_score:
            best_score = dino_score
            _best_score = best_score
            pos = x

    print(str(gen[pos].genoma) + " - " + str(_best_score))

    return gen[pos], best_score
```

Para a variação, foi feito também um processo de mutação o qual dado uma taxa de mutação será feito ou a adição ou a subtração dos pesos inseridos no genoma. 

```python
def Mutation(self):
    for x, gen in enumerate(self.genoma):
        a = random.randint(0, 100)
        if a <= self.mutation_scale:
            if random.randint(0, 100) % 2 == 0:
                self.genoma[x] += 1
            else:
                self.genoma[x] -= 1
```


Após 15 minutos, o código conseguiu gerar esse spécime com o score de 522. Entretanto, gerações futuras se mostraram ineficazes a atuar com os pterodatilos, mesmo considerando que a informação sobre esse obstaculo foi passado para o perceptron. A seguir está um vídeo demonstrando o melhor spécime. 

https://github.com/user-attachments/assets/047d352e-4c00-4bf1-a831-7c0368f212a2

# Considerações

Evidentemente, não foi possivel criar um algoritmo capaz de jogar o jogo de forma eficaz utilizando as técnicas aplicadas. Foi feito a tentativa de aplicar a técnica de cruzamento single point para a formação de novas gerações mas ele se provou muito ineficaz, muitas vezes gerando gerações de dinossauros que não conseguiam passar pelo primeiro cacto. Muito provavelmente o MLP foi feito de forma incorreta mas não consegui identificar o problema. 
