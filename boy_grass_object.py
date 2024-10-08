from pico2d import *
import random
# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):self

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
         self.frame = (self.frame + 1) % 8
         self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball21x21:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.speed = random.randint(1, 10)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 50:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class Ball41x41:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.speed = random.randint(1, 10)
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 70:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for Ball21x21 in smallballs:
        Ball21x21.update()
    for Ball41x41 in bigballs:
        Ball41x41.update()

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for Ball21x21 in smallballs:
        Ball21x21.draw()
    for Ball41x41 in bigballs:
        Ball41x41.draw()
    update_canvas()

def reset_world():
    global running
    global grass
    global team
    global smallballs
    global bigballs

    ballcnt = random.randint(0, 20)
    running = True
    grass = Grass()
    team = [ Boy () for i in range(10)]
    smallballs = [Ball21x21() for i in range(ballcnt)]
    bigballs = [Ball41x41() for i in range(20-ballcnt)]

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
