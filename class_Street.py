class Street(object):

    def __init__(self, street_name=None, street_points=None):
        if street_name is not None and street_points is not None:
            self.street_name = street_name
            self.street_point = street_points

        else:
            self.street_name = []
            self.street_point = []

    def __repr__(self):
        return '[' + str(self.street_name) + ', ' + str(self.street_point) + ']'