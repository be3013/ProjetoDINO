"""
This is the main entry point of the application.

Import the bare minimum needed and add any initialization code here.
"""
from chrome_trex import MultiDinoGame, ACTION_UP, ACTION_FORWARD, ACTION_DOWN
import random
from random import randrange
import copy

fps = 60
dino_count = 100
dead_dinos = 0

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
    
    def check_next_step(self):
        primeiro_neuronio = self.distancia*self.genoma[0] + self.altura*self.genoma[1] + self.velocidade*self.genoma[2]
        segundo_neuronio = self.distancia*self.genoma[3] + self.altura*self.genoma[4] + self.velocidade*self.genoma[5]

        if primeiro_neuronio <= 0:
            primeiro_neuronio = 0
        if segundo_neuronio <= 0:
            segundo_neuronio = 0

        terceiro_neuronio = primeiro_neuronio*self.genoma[6] + segundo_neuronio*self.genoma[7]
        quarto_neuronio = primeiro_neuronio*self.genoma[8] + segundo_neuronio*self.genoma[9]

        if terceiro_neuronio > 0:
            self.next_step = ACTION_UP
        elif quarto_neuronio > 0:
            self.next_step = ACTION_DOWN
        else:
            self.next_step = ACTION_FORWARD

    def Mutation(self):
        for x, gen in enumerate(self.genoma):
            a = random.randint(0, 100)
            if a <= self.mutation_scale:
                if random.randint(0, 100) % 2 == 0:
                    self.genoma[x] += 1
                else:
                    self.genoma[x] -= 1

def instanciar_prim_dinos(_dino_count):
    result = []
    for dino in range(_dino_count):
        dino = Dino()
        dino.randomizar_genoma()
        result.append(copy.deepcopy(dino))

    return result

def main():
    game = MultiDinoGame(fps=fps, dino_count=dino_count)

    first_gen = instanciar_prim_dinos(dino_count)
    best_score = 0
    best_dino = Dino()

    while True:
        action_list = []
        current_state = game.get_state()
        for dino in first_gen:
            dino.check_next_step()

            dino.distancia = current_state[0]
            dino.altura = current_state[1]
            dino.velocidade = current_state[len(current_state) - 1]

            action_list.append(dino.next_step)

        game.step(action_list)
        if check_all_dead(game):
            potential_dino, potential_score = get_bestest_score(game, first_gen, best_score)
            if potential_score > best_score:
                best_dino = potential_dino
                best_score = potential_score
                changed = True
            else:
                changed = False

            print(changed)
            reasign_best_genoma(first_gen, best_dino)
            for dino in first_gen:
                dino.Mutation()
            game.reset()

    return 0
 
def check_all_dead(_game):
    for dino in _game.player_dinos:
        if not dino.is_dead:
            return False
        
    return True

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

def reasign_best_genoma(gen, best_dino):
    for d in gen:
        d.genoma = best_dino.genoma

if __name__ == "__main__":
    SystemExit(main())
