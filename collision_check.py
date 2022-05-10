import math

class Player:
    def __init__(self, height = 0, radius = 0, pos = (0, 0, 0)):
        self.height = height
        self.radius = radius
        self.pos = pos

def vectorAtoB(a, b):
    return math.sqrt(math.pow((b.pos[0] - a.pos[0]), 2) + math.pow((b.pos[1] - a.pos[1]), 2) + math.pow((b.pos[2] - a.pos[2]), 2))

def checkCollision(a, b):
    if (a.radius + b.radius) > vectorAtoB(a, b):
        return True
    else:
        return False

def main():
    P1 = Player(3, 2, (-2,2,0))
    P2 = Player(4, 4, (2,4,2))
    P3 = Player(1, 2, (-4,8,2))
    P4 = Player(5,8, (2,-6,5))
    
    print("Combined radius:\t" + str(P1.radius + P2.radius))
    print("Vector P1 to P2:\t" + str(round(vectorAtoB(P1, P2), 2)))
    print("Players touching:\t" + str(checkCollision(P1, P2)))
    print()
    print("Combined radius:\t" + str(P1.radius + P3.radius))
    print("Vector P1 to P3:\t" + str(round(vectorAtoB(P1, P3), 2)))
    print("Players touching:\t" + str(checkCollision(P1, P3)))
    print()
    print("Combined radius:\t" + str(P1.radius + P4.radius))
    print("Vector P1 to P4:\t" + str(round(vectorAtoB(P1, P4), 2)))
    print("Players touching:\t" + str(checkCollision(P1, P4)))
    print()
    print("Combined radius:\t" + str(P2.radius + P3.radius))
    print("Vector P2 to P3:\t" + str(round(vectorAtoB(P2, P3), 2)))
    print("Players touching:\t" + str(checkCollision(P2, P3)))
    print()
    print("Combined radius:\t" + str(P2.radius + P4.radius))
    print("Vector P2 to P4:\t" + str(round(vectorAtoB(P2, P4), 2)))
    print("Players touching:\t" + str(checkCollision(P2, P4)))
    print()
    print("Combined radius:\t" + str(P3.radius + P4.radius))
    print("Vector P3 to P4:\t" + str(round(vectorAtoB(P3, P4), 2)))
    print("Players touching:\t" + str(checkCollision(P3, P4)))
    
if __name__ == "__main__":
    main()
