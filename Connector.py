class Connector:
    def __init__(self, canvas, nodeS, nodeD):
        self.source = nodeS
        self.distinct = nodeD
        self.canvas = canvas

    def connect(self):
        #self.canvas.create_line(self.source.get_coord_x, self.source.get_coord_y, self.distinct.get_coord_x, self.distinct.get_coord_y)
        self.canvas.create_line(self.source.x, self.source.y, self.distinct.x, self.distinct.y)
        self.source.increase_rank()
        self.distinct.increase_rank()
