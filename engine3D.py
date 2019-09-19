import pygame
import sys
import numpy as np
from math import tan, pi, radians
from camera import Camera


def create_projection_matrix(width, height):
    fNear = 0.1
    fFar = 1000.0
    fFov = 90.0
    fAspectRatio = float(height) / float(width)
    fFovRad = 1.0 / tan(radians(fFov * 0.5))

    projection_matrix = np.array([[fAspectRatio * fFovRad, 0, 0, 0],
                                  [0, fFovRad, 0, 0],
                                  [0, 0, fFar / (fFar - fNear), 1],
                                  [0, 0, (-fFar * fNear) / (fFar - fNear), 0]])

    return projection_matrix


class Engine3D:

    def __init__(self):
        pygame.init()

        self.width = None
        self.height = None
        self.window_name = None
        self.screen = None

        self.camera = Camera()

        self.tps = None
        self.tps_clock = pygame.time.Clock()
        self.tps_dt = 0.0

        self.running = False

        self.objects = []
        self.matrix = create_projection_matrix(1, 1)

    def construct_console(self, width=400, height=200, window_name="Default", tps=60.0):
        self.width = width
        self.height = height
        self.window_name = window_name
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.window_name)

        self.camera = Camera()

        self.tps = tps
        self.running = False

        self.matrix = create_projection_matrix(self.width, self.height)

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
            self.draw_obj()
            self.draw()
            pygame.display.flip()

    def draw_obj(self):
        for obj in self.objects:
            obj.draw(self)

    # functions to override
    def update(self):
        pass

    def tick(self):
        pass

    def draw(self):
        pass


