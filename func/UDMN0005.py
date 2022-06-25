def post_strike(self, var):
    var.cur_target.stats[1] -= 1
    var.cur_target.stats[2] -= 1
