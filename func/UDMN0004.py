# attack_val = 0

def pre_strike(self, var):
    var.targets.clear()
    for a in self.allies():
        a.heal(a.stats[0] * 0.07)
#     global attack_val
#     attack_val = self.stats[1]
#     self.stats_val = 0
    
# def post_strike(self, var):
#     self.stats[1] = attack_val
