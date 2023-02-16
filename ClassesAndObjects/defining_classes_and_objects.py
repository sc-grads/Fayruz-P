class Robot:
    population = 0  # class attribute
    """This class implements a Robot"""

    def __int__(self, name, year):
        self.name = name
        self.year = year
        Robot.population += 1

    def __del__(self):
        print('Robot destroyed')

    def setEnergy(self, energy):
        self.energy = energy


r1 = Robot('R1', 2023)
print(r1.__doc__)
print(f'Robot name:{r1.name}')
r1.setEnergy(500)
print(r1.energy)
print(getattr(r1, 'energy'))
print(r1.__dict__)
