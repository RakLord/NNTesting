import config
from config import *
from ball import Player

from text import Text



class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.target_fps = 240
        self.fps = self.target_fps
        self.dt = 1
        self.background_color = (32, 32, 32)
        self.window_size = SCREEN_SIZE
        self.window_title = "Rak"
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)

        self.keys = []
        self.player = Player(400, 300, 10, (255, 255, 255))
        self.enemy = Player(800, 800, 10, (30, 90, 78))


        self.text = {}
        self.text["fps"] = Text(self.window, f"FPS: {round(self.fps)}", (10, 10), (255, 255, 255), 20)
        self.text["dt"] = Text(self.window, f"DT: {round(self.dt)}", (10, 30), (255, 255, 255), 20)



    def run(self):
        while self.running:
            self.dt = self.clock.tick(self.target_fps)
            self.fps = self.clock.get_fps()

            self.events()
            self.update()
            self.draw()
        
        pygame.quit()

    def events(self):
        self.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                if event.key == pygame.K_r:
                    new_vel = vector2(random.randrange(-500, 500), random.randrange(-500, 500))
                    self.player.velocity = new_vel
                    print(new_vel)
        
                
    def update(self):
        self.player.update(self.keys, self.dt)
        self.enemy.update(self.keys, self.dt)
        self.text["fps"].change_text(f"FPS: {round(self.fps)}")
        self.text["dt"].change_text(f"DT: {round(self.dt)}")


    def draw(self):
        self.window.fill(self.background_color)
        self.player.draw(self.window)
        self.enemy.draw(self.window)
        for key in self.text:
            self.text[key].draw()

        pygame.display.update()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
