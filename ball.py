from config import *
import config

class Trail:
    def __init__(self, max_length=200):
        self.trail = []
        self.max_length = max_length
        self.trail_color = (190, 16, 24)
    
    # add a new Ball to the trail, check if the length of the self.trail is more than self.trail length if it is pop of the first value
    def add(self, pos):
        self.trail.append(Ball(pos.x, pos.y, 5, self.trail_color))
        if len(self.trail) > self.max_length:
            self.trail.pop(0)

    def draw(self, window):
        for ball in self.trail:
            ball.draw(window)

    def update(self, dt):
        for ball in self.trail:
            ball.radius -= (0.002 * dt)


class Ball:
    def __init__(self, x, y, radius, color, controlable=False, trail=True):
        self.pos = vector2(x, y)
        self.velocity = vector2(0, 0)
        self.acceletation = vector2(1, 1)
        self.velocity_max = vector2(10, 10)
        self.direction = math.pi
        self.drag = vector2(0.5, 0.5)

        self.controlable = controlable
        if trail:
            self.trail = Trail()

        self.radius = radius
        self.color = color

    def draw(self, window):
        self.trail.draw(window)
        pygame.draw.circle(window, self.color, self.pos, self.radius)

    
    def update(self, keys, dt):
        self.trail.add(self.pos)
        if self.controlable:
            if keys[pygame.K_w]:
                if self.velocity.y > -self.velocity_max.y:
                    self.velocity.y -= self.acceletation.y
            if keys[pygame.K_s]:
                if self.velocity.y < self.velocity_max.y:
                    self.velocity.y += self.acceletation.y
            if keys[pygame.K_a]:
                if self.velocity.x > -self.velocity_max.x:
                    self.velocity.x -= self.acceletation.x
            if keys[pygame.K_d]:
                if self.velocity.x < self.velocity_max.x:
                    self.velocity.x += self.acceletation.x

        # if self.velocity != vector2(0, 0):
        #     print(self.velocity)

        self.check_bounce()
        self.pos.x += (self.velocity.x / 50) * dt
        self.pos.y += (self.velocity.y / 50) * dt
        

        # reduce the velocity by the drag value if it is more than 0, include delta time
        if self.velocity.x > 0:
            self.velocity.x -= self.drag.x / dt
        elif self.velocity.x < 0:
            self.velocity.x += self.drag.x / dt 
        if self.velocity.y > 0:
            self.velocity.y -= self.drag.y / dt
        elif self.velocity.y < 0:
            self.velocity.y += self.drag.y / dt

        
class Player(Ball):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color)
        self.controlable = True


    def check_bounce(self):
        if self.pos.x + self.radius > SCREEN_SIZE.x or self.pos.x - self.radius < 0:
            self.velocity.x *= -1
        if self.pos.y + self.radius > SCREEN_SIZE.y or self.pos.y - self.radius < 0:
            self.velocity.y *= -1