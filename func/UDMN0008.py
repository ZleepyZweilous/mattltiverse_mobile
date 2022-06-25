import random

def pre_strike(self, var):
    var.targets.clear()
    for a in self.allies():
        a.boost_stat(random.randint(0,5), 1)
