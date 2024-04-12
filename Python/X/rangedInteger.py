#gives me an int which is limitied in range
class RangedInt:
    def __init__(self, startValue,minValue, maxValue):
        self.minValue = minValue 
        self.maxValue = maxValue
        self.number = startValue
    def raiseInt(self):
        self.number += 1
        if self.number > self.maxValue:
            self.number = self.minValue
        return self.number