class Ojt:
    def __init__(self, name, passion):
        self.name = name
        self.passion = passion
    def printname(self):
        print(self.name, self.passion)
# ojt = Ojt("Ty","car")
# ojt.printname()

class Act:
    def __init__(self, name, passion):
        self.name = name
        self.passion = name
    def printname(self):
        print(self.name, self.passion)
class Act(Ojt):
    def printage(self):
        print(self.age)
act = Act("Tan","Game")
act.printname()
act.age = 20
act.printage()