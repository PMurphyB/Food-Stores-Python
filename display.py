# @author Payton Murphy-Blanchard

class Display :
    def __init__(self, gels, num_160, num_320, num_big_bottle, hour, minute, caffeine) :
        self.gels = gels
        self.num_160 = num_160
        self.num_320 = num_320
        self.num_big_bottle = num_big_bottle
        self.hour = hour
        self.minute = minute
        self.caffeine = caffeine
        
    def display(self) :
        if self.minute == 0 :
            print(f"For your {self.hour} hour ride you will need: ", end = "")
        elif self.minute > 0 :
            print(f"For your {self.hour} hour and {self.minute} minute ride you will need: ", end = "")
        if self.gels > 0 :
            print(f"{self.gels} SIS gels, ", end = "")
        if self.num_160 == 1 :
            print(f"{int(self.num_160)} 160 satchel, ", end = "")
        elif self.num_160 > 1 :
            print(f"{int(self.num_160)} 160 satchels, ", end = "")
        if self.num_320 == 1 :
            print(f"{int(self.num_320)} 320 satchel which can be replaced with {self.num_320 * 2} 160 satchels, ", end = "")
        elif self.num_320 > 1 :
            print(f"{int(self.num_320)} 320 satchels which can be replaced with {self.num_320 * 2} 160 satchels, ", end = "")
        if self.num_big_bottle == 1 :
            print(f"{int(self.num_big_bottle)} 'big bottle' (a 750mL bottle with 1 and a half 320s)", end = "")
        elif self.num_big_bottle > 1 :
            print(f"{int(self.num_big_bottle)} 'big bottles' (a 750mL bottle with 1 and a half 320s)", end = "")
        if self.caffeine == "Yes" :
            print(f"and I would also recommend that you take a caffeinated gel.")
        if self.caffeine == "No" :
            print("and that should be all!")
        print("Have fun!")
            
        
        