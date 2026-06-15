class Apple:
    print("")

class Snake:
    print()

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def render(self):
        print("Height: ", self.height)
        print("Width: ", self.width)


game = Game(10, 20)
game.render()