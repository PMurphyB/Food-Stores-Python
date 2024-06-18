# @author Payton Murphy-Blanchard

from calculator import Calculator
from display import Display

class User :
    def __init__(self, user, password, stock_SIS, stock_160, stock_320, stock_maurten, stock_caffeine) :
        self.user = user
        self.password = password
        self.stock_SIS = stock_SIS
        self.stock_160 = stock_160
        self.stock_320 = stock_320
        self.stock_maurten = stock_maurten
        self.stock_caffeine = stock_caffeine
        
    def setuser(self, user) :
        self.user = user
    def getuser(self) :
        return self.users
    
    def setpassword(self, password) :
        self.password = password
    def getpassword(self) :
        return self.password
    
    def setSIS(self, stock_SIS) :
        self.stock_SIS = stock_SIS
    def getSIS(self) :
        return self.stock_SIS
    
    def set160(self, stock_160) :
        self.stock_160 = stock_160
    def get160(self) :
        return self.stock_160
    
    def set320(self, stock_320) :
        self.stock_320 = stock_320
    def get320(self) :
        return self.stock_320
    
    def setmaurten(self, stock_maurten) :
        self.stock_maurten = stock_maurten
    def getmaurten(self) :
        return self.stock_maurten
    
    def setcaffeine(self, stock_caffeine) :
        self.stock_caffeine = stock_caffeine
    def getcaffeine(self) :
        return self.stock_caffeine    
    
    def inventorycheck(self) :
        if int(self.stock_SIS) < 20 or int(self.stock_160) < 10 or int(self.stock_320) < 10 or int(self.stock_maurten) < 10 or int(self.stock_caffeine) < 10 :
            new_display = Display(self.stock_SIS, self.stock_160, self.stock_320, 0, 0, 0, self.stock_caffeine)
            new_display.setmaurten(self.stock_maurten)
            new_display.display_warning()