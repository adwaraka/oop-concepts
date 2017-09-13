from abc import ABCMeta, abstractmethod

class Vehicle(object):
    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        if self.sold_on is not None:
            return 0.0
        return 5000.0 * self.wheels

    def purchase_price(self):
        if self.sold_on is None:
            return 0.0
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        pass

class Car(Vehicle):
    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        return 'car'
		
def main():
    c = Car(4, 0, 'Honda', 'Accord', 2014)
    print c.sale_price(), c.purchase_price(), c.vehicle_type()

if __name__ == '__main__':
    main()