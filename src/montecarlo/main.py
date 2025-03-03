from random import uniform
import matplotlib.pyplot as plt

class Montecarlo:
    def __init__(self, a, b, f):
        assert a < b, 'a must be less than b'
        assert type(a) in (int, float), 'a must be a number'
        assert type(b) in (int, float), 'b must be a number'
        assert callable(f), 'f must be a function'
        self.a = a
        self.b = b
        self.f = f

    def integrate(self, n):
        '''Approximates the integral of f in the interval [a, b] using Monte
        Carlo integration with N random points.'''
        assert type(n) == int, 'n must be an integer'
        assert n > 0, 'n must be greater than 0'
        s = 0
        for i in range(n):
            x = uniform(self.a, self.b)
            s += self.f(x)
        return (self.b - self.a) * s / n
    def plot(self, n):
        '''Plots the result of the integration using 1 to N points, showing how the
        approximation converges to the true value as N increases.'''
        assert type(n) == int, 'n must be an integer'
        assert n > 0, 'n must be greater than 0'
        x = [uniform(self.a, self.b) for i in range(n)]
        y = [self.f(i) for i in x]
        plt.scatter(x, y, color='blue')
        plt.show()