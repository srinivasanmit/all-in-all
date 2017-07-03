class Test:
    def __init__(self, name):
        self.cards = []
        self.name = name

    def __str__(self):
        return '{0} holds ...'.format(self.name)

obj1 = Test('obj1')
print str(obj1.name)
print obj1
obj1.__repr__ = obj1.__str__
print `obj1`
print repr(obj1)

obj2 = Test('obj2')
print obj2
