class Statistic():

    def __init__(self):
        self.reset_statistic()
        self.game_start = True
        with open('main_score.txt', 'r') as f:
            self.main_score = int(f.readline())

    def reset_statistic(self):
        self.guns_left = 2
        self.score = 0
