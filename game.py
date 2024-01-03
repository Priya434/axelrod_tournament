from player import Player
from scores import scores


class Game:

    # def play(self, player, coplayer):
    #     self.player._action = self.player.strategy(self.coplayer)
    #     self.coplayer._action = self.coplayer.strategy(self.player)

    # def set_score(self):
    #     self.player._score = scores[(
    #         self.player._action, self.coplayer._action)][0]
    #     self.coplayer._score = scores[(
    #         self.coplayer._action, self.player._action)][0]

    # def update_total_score(self):
    #     self.player.update_total_score(self.player._score)
    #     self.coplayer.update_total_score(self.coplayer._score)

    # def update_history(self):
    #     self.player.update_history(self.player._action, self.coplayer._action)
    #     self.coplayer.update_history(
    #         self.coplayer._action, self.player._action)

    def __init__(self, player: Player, coplayer: Player):

        # self.player = player
        # self.coplayer = coplayer

        # self.play()
        # self.set_score()
        # self.update_total_score()
        # self.update_history()

        player._action = player.strategy(coplayer)
        coplayer._action = coplayer.strategy(player)

        player._score = scores[(
            player._action, coplayer._action)][0]
        coplayer._score = scores[(
            coplayer._action, player._action)][0]

        player.update_total_score(player._score)
        coplayer.update_total_score(coplayer._score)

        player.update_history(player._action, coplayer._action)
        coplayer.update_history(coplayer._action, player._action)
