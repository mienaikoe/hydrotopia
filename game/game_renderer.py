import pygame
from interfaces.component_interface import ComponentInterface
from mode_state import ModeState


class GameRenderer(ComponentInterface):
    def __init__(self, screen: pygame.Surface, mode_state: ModeState):
        super().__init__(screen)
        self.mode_state = mode_state

    def update(self):
        pass

    def render(self):
        pass
