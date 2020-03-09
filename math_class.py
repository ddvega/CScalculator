import math


class Mathematics:
    # converts string to float, performs calcuation then returns it as string
    def run(self, expression, function):
        try:
            result = round(function(float(expression)), 3)
        except:
            result = "ERROR"
        return str(result)

    def run2(self, a, b, function):
        try:
            result = function(int(a), int(b))
        except:
            result = "ERROR"
        return str(result)

    def basic(self, expression):
        return str(eval(expression))

    def log10(self, expression):
        return self.run(expression, math.log10)

    def squareRoot(self, expression):
        return self.run(expression, math.sqrt)

    def factorial(self, expression):
        expression = str(int(float(expression)))  # convert to int
        return self.run(expression, math.factorial)

    def log2(self, expression):
        return self.run(expression, math.log2)

    def greatestCDenom(self, a, b):
        return self.run2(a, b, math.gcd)


