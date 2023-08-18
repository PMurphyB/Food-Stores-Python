# @author Payton Murphy-Blanchard

class User :
    def __init__(self, user, password, stock_160, stock_320, stock_maurten, stock_caffeine) :
        self.filename = filename
        self.user = user
        self.password = password
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
        return self.passwords
    
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
    