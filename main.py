from Engine3D import Engine3D
import pygame


class Engine(Engine3D):
    def __init__(self):
        super().__init__()
        self.objects = pygame.Rect(10, 10, 50, 50)

    def update(self):
        pass

    def tick(self):
        self.objects.x += 1

    def draw(self):
        # pass
        pygame.draw.rect(self.screen, (255, 255, 255), self.objects)


engine = Engine()

engine.construct_console(800, 400)

engine.start()
