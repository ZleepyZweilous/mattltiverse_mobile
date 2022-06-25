import random

def post_strike(self, var):
    self.boost_stat(random.randint(0, 5), 3)
    self.boost_stat(random.randint(0, 5), -2)
