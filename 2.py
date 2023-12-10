class Fibonacci:
    def __init__(self, n) -> None:
        self.a, self.b = 1, 1
        self.n = n
        self.i = 0

    def __next__(self):
        if self.i == 0:
            self.i += 1
            return self.a
        elif self.i < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.i += 1
            return self.a
        else:
            raise StopIteration
        
    def __iter__(self):
        return self
    
