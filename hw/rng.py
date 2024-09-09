# best case that I found by playing around: m = 103 a = 21
# N = 10,000,000 results
# 10000000 Python: 50.4997794997795, 28.866028663695054
# 10000000 Mine: 49.55884691884692, 29.346328711447374

class RNG:
    def __init__(self, seed) -> None:
        self.m = 2**31-1
        self.a = 48271
        self.c = 0
        self.x = seed


    def _next(self):
        self.x = (self.a * self.x + self.c) % self.m

        return self.x


    # Returns a random number between [1, bound] using the LCG algorithm
    def nextInt(self, upper_bound):
        return (self._next() % upper_bound) + 1
    

# testing to make sure it works
# rng = RNG(1)
# arr = []
# for i in range(5000):
#     arr.append(rng.nextInt(100))

# print(arr)