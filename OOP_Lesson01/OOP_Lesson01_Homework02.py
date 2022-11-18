class ChemElem:
    def __init__(self, melting_point, boiling_point):
        self.melting_point = melting_point  # t °C
        self.boiling_point = boiling_point  # t °C

    def get_state(self, temp):
        result_state = ''
        if temp < self.melting_point:
            result_state = 'Element is solid'
        elif temp >= self.melting_point and temp <= self.boiling_point:
            result_state = 'Element is liquid'
        elif temp > self.boiling_point:
            result_state = 'Element is gas'
        return result_state

    def get_t(self, t, name_t):
        res_t = 0  # t °C
        to_k = 273  # t по Кельвину == 0 °C
        to_f = 32  # t по Фаренгейту == 0 °C
        if name_t == 'K' or name_t == 'k':
            res_t = t - to_k
        elif name_t == 'F' or name_t == 'f':
            res_t = (t - to_f) * (5/9)
        elif name_t == 'C' or name_t == 'c':
            res_t = t
        return f'{res_t} C'


water = ChemElem(melting_point=0,
                 boiling_point=100)
print(water.get_state(-5))
print(water.get_state(1))
print(water.get_state(115))
print(water.get_t(212, 'F'))
print(water.get_t(373, 'K'))
print(water.get_t(100, 'C'))
