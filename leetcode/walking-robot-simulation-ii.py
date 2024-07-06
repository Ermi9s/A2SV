class Robot:
    def __init__(self, width, height):
        self.h = height
        self.w = width
        self.peri = 2*(height + width) - 4
        self.dir = "East"
        self.pos = [0,0]
        self.curr = 0
    
        self.ex = {}

        num = self.peri + 0

        for i in range(height):
            self.ex[(num)%self.peri] = [0 , i]
            num -= 1
        
        for i in range(1,width):
            self.ex[(num)%self.peri] = [i , (height -1)]
            num -= 1
        
        for i in range(height -2, -1 , -1):
            self.ex[(num)%self.peri] = [width -1, i]
            num -= 1

        for i in range(width-2, -1, -1):
            self.ex[(num)%self.peri] = [i , 0]
            num -= 1
    

    def step(self, num):
        self.curr = (num + self.curr)% self.peri
        self.pos = self.ex[self.curr]

        if self.pos[1] == 0 and self.pos[0] != 0:
            self.dir = "East"
        elif self.pos[0] == self.w-1  and self.pos[1] != 0:
            self.dir = "North"

        elif self.pos[1] == self.h -1  and self.pos[0] != self.w - 1:
            self.dir = "West"
        else:
            self.dir = "South"


    def getPos(self):
        return self.pos
        

    def getDir(self):
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()