def post_strike(self, var):
    for a in self.allies():
        a.boost_stat(3, 1)
