

class Wire():

    x = 0
    y = 0

    def __init__(self):

        print("Added new wire...")

    def move(self, command):

        direction = command[0]
        distance = int(command[1:])

        if direction == "U":
            self.y+= distance     

        elif direction == "D":
            self.y-=distance

        elif direction == "R":
            self.x+=distance

        elif direction == "L":
            self.x-=distance

        print("Moving...", direction, distance)

def main():

    with open("input.txt","r") as f:

        wire1,wire2 = f.readlines()

        moves1 = wire1.split(",")
        moves2 = wire2.split(",")

        wire1 = Wire()
        wire2 = Wire()

        [wire1.move(move) for move in moves1]
        [wire2.move(move) for move in moves2]

        print(wire1.x,wire1.y)
        print(wire2.x,wire2.y)


        ##movements
        #print(*movement)


if __name__ == "__main__":
    main()