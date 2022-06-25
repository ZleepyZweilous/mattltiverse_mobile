import random
# passive_proced = False

# def init():
#     global passive_proced
#     passive_proced = False

def on_ally_die(self, ally):
    if len(self.allies(self.NONINST(self))) == 0:
        target = random.choice(self.allies(self.NONINST(self), False))
        target.dead = False
#         target.curhp = round(target.stats[0] / 2)
        target.heal(target.stats[0] / 2)
