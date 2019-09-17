import pygame
import sys


class Engine3D:

    def __init__(self):
        pygame.init()

        self.width = None
        self.height = None
        self.window_name = None
        self.screen = None

        self.tps = None
        self.tps_clock = pygame.time.Clock()
        self.tps_dt = 0.0

        self.running = False

        self.objects = None

    def construct_console(self, width=400, height=200, window_name="Default", tps=60.0):
        self.width = width
        self.height = height
        self.window_name = window_name
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.window_name)

        self.tps = tps
        self.running = False

        return True

    def start(self):

        self.running = True
        self.main_loop()

    def main_loop(self):

        while self.running:

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit(0)

                self.update()

            # Tick
            self.tps_dt += self.tps_clock.tick() / 1000.0

            while self.tps_dt > 1 / self.tps:
                self.tps_dt -= 1 / self.tps
                self.tick()

            # Render
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    # functions to override
    def update(self):
        pass

    def tick(self):
        pass

    def draw(self):
        pass
