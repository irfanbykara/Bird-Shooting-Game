import pygame
import consts

class GameLogic:

    def __init__(self,score_text,bird,screen):
        super().__init__()
        self.well_shot = 0
        self._score_text = score_text
        self.seconds = 0
        self.screen = screen
        self.start_ticks = pygame.time.get_ticks()
        self.bird = bird


    def inc_well_shot(self):
        self.well_shot += 1

    def get_well_shot(self):
        return self.well_shot

    def set_score_text(self):
        self._score_text = consts.FONT.render("Score:  " + str(self.well_shot), 1, consts.BLACK)

    def get_score_text(self):
        return self._score_text

    def aim_handle(self,hands,detector,screen):
        if hands:
            lmList = hands[0]['lmList']
            cursor = lmList[8]
            screen.blit(consts.AIM, (cursor[0] - 10, cursor[1] - 10))

            # pygame.display.flip()
            length, info = detector.findDistance(lmList[8], lmList[12])

            if length < 45:  # this means index finger and mid finger is close enough
                pygame.draw.circle(screen, consts.RED, (cursor[0]+3, cursor[1]+3), 5)
                consts.GUN_SOUND.play()
                self.check_shot(cursor)

    def set_seconds(self):
        self.seconds = int( (pygame.time.get_ticks() - self.start_ticks) / 1000 )


    def get_seconds(self):
        return self.seconds

    def check_shot(self,cursor, ):

        dist = self.get_dist(self.bird.posx, self.bird.posy,cursor[0],cursor[1])

        if self.seconds >= 10:  # If the time is up.
            restart_pos_x = self.screen.get_width() / 2 - 100
            restart_pos_y = self.screen.get_height() / 2 +50
            dist_to_restart = self.get_dist(restart_pos_x,restart_pos_y, cursor[0], cursor[1])

            if dist_to_restart <= 150:
                self.start_ticks = pygame.time.get_ticks()  # Game is restarting, resetting the timer.
                self.well_shot = 0
                self.set_score_text()
                pygame.display.flip()

        if dist < 50:
            self.inc_well_shot()
            self.set_score_text()
            self.bird.reinitialize_bird()
            self.screen.blit(consts.BIRD_IMG, (self.bird.posx, self.bird.posy))

    @staticmethod
    def get_dist(x1,y1,x2,y2):
        dist = ((x1 - x2) ** 2 + (
                y1 - y2) ** 2) ** 0.5  # Distance between our shot and the bird.

        return dist


