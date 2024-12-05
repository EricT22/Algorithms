class Edge():
    def __init__(self, costFrom, to):
        self.costFrom = costFrom
        self.to = to

    
    def __str__(self) -> str:
        if self.costFrom < 0 or self.to < 0:
            return "No connection"
        
        return str(self.costFrom) + " to go to " + str(self.to)


    def get_costFrom(self):
        return self.costFrom


    def get_to(self):
        return self.to