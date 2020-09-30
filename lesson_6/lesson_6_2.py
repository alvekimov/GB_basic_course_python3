class road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def count_mass(self):
        """
            length and width are measured in meters
            weight 1 sq. m. of asphalt is 25 kg
            thickness asphalt is 5 sm
        """
        try:
            mass = self._length * self._width * 25 * 0.05
            print(f'Mass asphalt: {mass} kg or {(mass) / 1000} t.')
        except TypeError:
            print('Error! Length and width are measured in meters.')


mass_1 = road(15000, 6)
mass_1.count_mass()

mass_2 = road('dxzgd', 'xcdzdx')
mass_2.count_mass()
