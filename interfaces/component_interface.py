import pygame
from mode_state import ModeState


class ComponentInterface:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def update(self):
        pass

    def render(self):
        pass
