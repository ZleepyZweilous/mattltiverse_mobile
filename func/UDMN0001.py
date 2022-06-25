passive_proced = False

def init(board):
    global passive_proced
    passive_proced = False
    
def on_take_damage(self, damage):
    if not passive_proced and self.curhp - round(damage) < self.stats[0] / 2:
        self.transform_into("UDMN0002")
