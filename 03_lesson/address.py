class Address:

    def __init__(self, index, city, street, building, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment

    def __str__(self):
        return f'{self.index}, {self.city}, {self.street}, {self.building} - {self.apartment}'