
class Node:
    def __init__(self, canvas, x, y, rank):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.rank = rank
        self.canvas.create_oval(x, y, x + 2, y + 2)

    def increase_rank(self):
        self.rank += 1

    def get_rank(self):
        return self.rank

    def get_coord_x(self):
        return self.x

    def get_coord_y(self):
        return self.y


