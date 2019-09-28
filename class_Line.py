class Line:

    def __init__(self, ip=None, fp=None):
        if ip is not None and fp is not None:
            self.ipt = ip
            self.fpt = fp

        else:
            self.ipt = []
            self.fpt = []

    def __repr__(self):
        return '[' + str(self.ipt) + '-->' + str(self.fpt) + ']'
