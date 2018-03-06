class MathDojo(object):
    def __init__(self):
        self.sum = 0
    def add(self, *pars):
        for par in pars:
            if type(par) == int or type(par) == float:
                self.sum += par
            elif type(par) == list or type(par) == tuple:
                for item in par:
                    self.sum += item
        return self
    def subtract(self, *pars):
        for par in pars:
            if type(par) == int or type(par) == float:
                self.sum -= par
            elif type(par) == list or type(par) == tuple:
                for item in par:
                    self.sum -= item
        return self

md = MathDojo()
print(md.add([1], (3,4)).add((3,5,7,8), [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).sum)