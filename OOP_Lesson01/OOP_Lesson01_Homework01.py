class ChemElem:
    def __init__(self, melting_point, boiling_point):
        self.melting_point = melting_point # t °C
        self.boiling_point = boiling_point # t °C

    def get_state(self, temp):
        result = ''
        if temp < self.melting_point:
            result = 'Element is solid'
        elif temp >= self.melting_point and temp <= self.boiling_point:
            result = 'Element is liquid'
        elif temp > self.boiling_point:
            result = 'Element is gas'
        return result

water = ChemElem(melting_point = 0,
                 boiling_point = 100)
print(water.get_state(-5))
print(water.get_state(1))
print(water.get_state(115))