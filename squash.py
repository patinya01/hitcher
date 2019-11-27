import pygame
from pygame.locals import *

FPS = 50
WINDOW_SIZE = (500,500)
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
GREY  = pygame.Color('grey')

#########################################
class Ball(object):

    def __init__(self, radius=10, color=WHITE,
                 pos=(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2), speed=(100,0)):
        (self.x, self.y) = pos
        (self.vx, self.vy) = speed
        self.radius = radius
        self.color = color

    def move(self, delta_t, display, player):
        global score, game_over
        self.x += self.vx*delta_t
        self.y += self.vy*delta_t

        # player-hitting check
        if player.can_hit(self):
            score += 10
            render_score()
            self.vx = abs(self.vx) # bounce ball back

        # make ball bounce if hitting wall
        if self.x < self.radius:
            self.vx = abs(self.vx)
            game_over = True # game over when ball hits left wall
        if self.y < self.radius:
            self.vy = abs(self.vy)
        if self.x > display.get_width()-self.radius:
            self.vx = -abs(self.vx)
        if self.y > display.get_height()-self.radius:
            self.vy = -abs(self.vy)

    def draw(self, display):
        pos = (int(self.x),int(self.y))
        pygame.draw.circle(display, self.color, pos, self.radius, 0)

#########################################
class Player(object):

    THICKNESS = 10

    def __init__(self, pos=WINDOW_SIZE[1]/2, width=100, color=WHITE):
        self.width = width
        self.pos = pos
        self.color = color

    def can_hit(self, ball):
        return self.pos-self.width/2.0 < ball.y < self.pos+self.width/2.0 \
            and ball.x-ball.radius < self.THICKNESS

    def draw(self, display):
        pygame.draw.rect(display, self.color, pygame.Rect(
            0,
            self.pos - self.width/2.0,
            self.THICKNESS,
            self.width), 2)

#########################################
def render_score():
    '''Render score into an image for display'''
    global font,score,score_image
    score_image = font.render("Score fuck = %d" % score,0 ,WHITE)

#########################################
def main():
    global game_over,font,score,score_image

    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('llllSquash')
    game_over = False
    font = pygame.font.SysFont("monospace", 20)
    score = 0
    score_image = None
    render_score()

    ball = Ball(speed=(500,500))
    player = Player(color=pygame.Color('green'),pos=100)

    while not game_over:
        for event in pygame.event.get(): # process events
            if (event.type == QUIT) or \
               (event.type == KEYDOWN and event.key == K_ESCAPE):
                game_over = True

        if pygame.key.get_pressed()[K_UP]:
            player.pos -= 10
        elif pygame.key.get_pressed()[K_DOWN]:
            player.pos += 5

        display.fill(BLACK)  # clear screen
        display.blit(score_image, (150,10))  # draw score
        player.draw(display)  # draw player
        ball.move(1./FPS, display, player)  # move ball
        ball.draw(display)  # draw ball

        pygame.display.update()  # redraw the screen
        clock.tick(FPS)  # wait to limit FPS requirement

#########################################
if __name__=='__main__':
    main()
    print ("Game Over! Total score is %d." % score)
    pygame.quit()
