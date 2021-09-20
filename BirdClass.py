
class Bird:
    def __init__(self,posx,posy,speed,):
        self.posx = posx
        self.posy = posy
        self.speed = speed
    def fly(self):
        self.posx= self.posx+ self.speed*10
        if self.posx<20 or self.posx>680 :
            self.speed = self.speed * -1


