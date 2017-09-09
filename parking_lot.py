class Slot():
    def __init__(self, number, empty, electric, handicap=False):
        self.number = number
        self.empty = empty
        self.electric = electric
        self.handicap = handicap

    def is_empty(self):
        return self.empty

    def is_electric(self):
        return self.electric

    def is_handicap(self):
        return self.handicap

class ParkingLot():
    parking_spots = []

    def __init__(self, size):
        self.size = size

    def construct(self):
        for i in xrange(self.size):
            self.parking_spots.append(Slot(i, True, False))

if __name__ == '__main__':
    p = ParkingLot(10)
    p.construct()
    for i in p.parking_spots:
        print i.number, i.empty, i.electric, i.handicap