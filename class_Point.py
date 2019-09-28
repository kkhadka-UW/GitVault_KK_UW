class Point:

    def __init__(self, x=None, y=None):
        if x is not None and y is not None:
            self.x_cor = round(float(x), 2)
            self.y_cor = round(float(y), 2)
        else:
            self.x_cor = None
            self.y_cor = None

    def __repr__(self):
        return '(' + str(self.x_cor) + ', ' + str(self.y_cor) + ')'
