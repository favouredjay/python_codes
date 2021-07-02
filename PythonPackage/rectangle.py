class Rectangle(object):
    width = 1.0
    length = 1.0

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def set_width(self, local_width: float):
        if 0.0 < local_width <= 20.0:
            self.width = local_width
        else:
            print("width is invalid")

    def set_length(self, local_length: float):
        if 0.0 < local_length <= 20.0:
            self.length = local_length
        else:
            print("length is invalid")

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
