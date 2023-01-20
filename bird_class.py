
import random

class Bird:

    def __init__(self,speed,):
        self.posx = random.randint( 10, 600 )
        self.posy = random.randint( 20, 100 )
        self.speed = speed


    def fly(self):
        self.posx= self.posx+ self.speed*10
        if self.posx<20 or self.posx>680 :
            self.speed = self.speed * -1

    def reinitialize_bird(self):
        self.posx = random.randint(10, 600)
        self.posy = random.randint( 20, 100 )




