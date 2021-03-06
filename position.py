class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def gety(self):
        return self.y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def print_position(self):
        print(self.x,self.y,sep=" ", end= "\n")