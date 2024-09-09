class RNG:
    def __init__(self, seed) -> None:
        self.m = 103
        self.a = 21
        self.c = 0
        self.x = seed


    def _next(self):
        self.x = (self.a * self.x + self.c) % self.m

        return self.x


    # Returns a random number between [1, bound] using the LCG algorith
    def nextInt(self, upper_bound):
        return (self._next() % upper_bound) + 1
    

# testing to make sure it works
# rng = RNG(1)
# arr = []
# for i in range(5000):
#     arr.append(rng.nextInt(100))

# print(arr)