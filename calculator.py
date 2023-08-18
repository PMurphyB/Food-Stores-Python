# @author Payton Murphy-Blanchard

import math
from display import Display

num_gels = 0
num_160 = 0
num_320 = 0
CARBS_160 = 40
CARBS_320 = 80
CARBS_BIG_BOTTLE = 120

class Calculator :
    def __init__(self, carbs, hours, minutes, gel, caffeine) :
        self.carbs = carbs
        self.hours = hours
        self.minutes = minutes
        self.gel = gel
        self.caffeine = caffeine
        
    def calculate_food(self) :
        num_160 = 0
        num_320 = 0
        num_big_bottle = 0        
        remaining_carbs = self.carbs - 80
        remaining_carbs = remaining_carbs * self.hours
        if self.gel == "SIS" :
            num_gels = self.hours * 2
            if self.minutes >= 30 :
                num_gels += 1
                
        num_160 = remaining_carbs / CARBS_160
        while num_160 > 1 :
            if (num_160 - 2) >= 0 :
                num_160 -= 2
                num_320 += 1
        while num_160 > 1 and num_320 > 1 :
            if ((num_160 - 1) >= 0) and ((num_320 - 1) >= 0) :
                num_160 -= 1
                num_320 -= 1
                num_big_bottle += 1

        final_result = Display(num_gels, num_160, num_320, num_big_bottle, self.hours, self.minutes, self.caffeine)
        final_result.display()
        
