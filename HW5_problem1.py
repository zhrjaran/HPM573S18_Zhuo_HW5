import numpy as np
import scr.FigureSupport as FigSupport


class Game(object):
    def __init__(self, id, prob_head):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(id)
        self._probHead = prob_head  # probability of flipping a head
        self._countWins = 0  # number of wins, set to 0 to begin

    def simulate(self, n_of_flips):

        count_tails = 0  # number of consecutive tails so far, set to 0 to begin

        # flip the coin 20 times
        for i in range(n_of_flips):

            # in the case of flipping a heads
            if self._rnd.random_sample() < self._probHead:
                if count_tails >= 2:  # if the series is ..., T, T, H
                    self._countWins += 1  # increase the number of wins by 1
                count_tails = 0  # the tails counter needs to be reset to 0 because a heads was flipped

            # in the case of flipping a tails
            else:
                count_tails += 1  # increase tails count by one
        print self._countWins

    def get_reward(self):
        # calculate the reward from playing a single game
        return  100*self._countWins - 250

class SetOfGames:
    def __init__(self, prob_head, n_games):
        self._gametimes=n_games
        self._gameRewards = []  # create an empty list where rewards will be stored

         # simulate the games
        for n in range(n_games):
                # create a new game
            game = Game(id=n, prob_head=prob_head)
                # simulate the game with 20 flips
            game.simulate(20)
                # store the reward
            self._gameRewards.append(game.get_reward())

    def get_ave_reward(self):
            """ returns the average reward from all games"""
            return sum(self._gameRewards) / len(self._gameRewards)


    def get_game_times(self):
        return self._gametimes

    def get_game_rewards(self):
        return self._gameRewards



games = SetOfGames(prob_head=0.5, n_games=1000)

# print the average reward
print('Expected reward when the probability of head is 0.5:', games.get_ave_reward())
print min(games.get_game_rewards()), max(games.get_game_rewards())

# create a histogram of patient survival time
FigSupport.graph_histogram(
    observations= games.get_game_rewards(),
    title="Histogram of Rewards Distribution",
    x_label="The amount of money we win(dollar)",
    y_label="Count",
    x_range=[min(games.get_game_rewards()),max(games.get_game_rewards())])

# In 20 times filp, we would expect the maximum money we won achieved at 6 time all win "TTH":
# So the maximum reward should be 6*100-250=350
# and the mininum reward shoule be 6*0-250 = -250
