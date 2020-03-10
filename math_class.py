from math import gcd, log2, log10, sqrt, factorial


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
        expression = str(eval(expression))
        return self.run(expression, log10)

    def squareRoot(self, expression):
        expression = str(eval(expression))
        return self.run(expression, sqrt)

    def factorial(self, expression):
        expression = str(int(eval(expression)))
        return self.run(expression, factorial)

    def log2(self, expression):
        expression = str(eval(expression))
        return self.run(expression, log2)

    def greatestCDenom(self, a, b):
        return self.run2(a, b, gcd)


