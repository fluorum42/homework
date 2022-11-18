class ChemElem:
    def __init__(self, melting_point, boiling_point):
        self.melting_point = melting_point  # t °C
        self.boiling_point = boiling_point  # t °C

    def get_state_temp(self, t, name_t):
        res_t = 0  # t °C
        to_k = 273  # t по Кельвину == 0 °C
        to_f = 32  # t по Фаренгейту == 0 °C
        if name_t == 'K' or name_t == 'k':
            res_t = t - to_k
        elif name_t == 'F' or name_t == 'f':
            res_t = (t - to_f) * (5/9)
        elif name_t == 'C' or name_t == 'c':
            res_t = t
        res_state = ''
        if res_t < self.melting_point:
            res_state = 'Element is solid'
        elif self.melting_point <= res_t <= self.boiling_point:
            res_state = 'Element is liquid'
        elif t > self.boiling_point:
            res_state = 'Element is gas'
        return f'{t} {name_t}, {res_state}'

water = ChemElem(melting_point=0,
                 boiling_point=100)
print(water.get_state_temp(4865, 'K'))
print(water.get_state_temp(31, 'C'))
print(water.get_state_temp(20, 'F'))