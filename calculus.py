#Series of helper functions I'm using over and over for the Coursera Calculus 1
#class

TODO: Testing
class Fx(object):
    def __init__(self, f):
        self.f = f
        assert callable(self.f)

    def limit_analysis(self, x):
        # analyze value of function nearer and nearer to limit
        self.X = self.limit_range(x, 8)
        s = 'x=%0.10f y=%0.10f'
        return '\n'.join([s % (x, self.f(x), ) for x in self.X])


    @staticmethod
    def limit_range(x, n=10):
        """
        x: limit value
        n: number of points near limit to analyze. symmetrical + and - of x
        """

        X =      [x+10 ** -_ for _ in range(1, n)]
        X.extend([x-10 ** -_ for _ in range(1, n)])
        X = sorted(X)
        return X
