class Constraint():

    def __init__(self, lower_bound, upper_bound):
        self.lower = lower_bound
        self.upper = upper_bound
    
    def set_average(self, avg: int):
        self.average = avg