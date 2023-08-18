# @author Payton Murphy-Blanchard

class Reader :
    def __init__(self, filename, users, passwords, stock_160, stock_320, stock_maurten, stock_caffeine) :
        self.filename = filename
        self.users = users
        self.passwords = passwords
        self.stock_160 = stock_160
        self.stock_320 = stock_320
        self.stock_maurten = stock_maurten
        self.stock_caffeine = stock_caffeine
        
    def getfilename(self) :
        return self.filename
    
    def getusers(self) :
        return self.users
    
    def getpasswords(self) :
        return self.passwords
    
    def get160(self) :
        return self.stock_160
    
    def get320(self) :
        return self.stock_320
    
    def getmaurten(self) :
        return self.stock_maurten
    
    def getcaffeine(self) :
        return self.stock_caffeine
    
    
    def read_users(self) :
        inFile = filename
        inFile = open(inFile, 'r')
        for line in inFile:
            line = line.rstrip()
            temps = line.split(',')
            users.append(temps[0])
            
    