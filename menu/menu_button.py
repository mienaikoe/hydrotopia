import pygame
from constants.colors import COLORS
from constants.fonts import FONTS
from interfaces.component_interface import ComponentInterface


class MenuButton(ComponentInterface):
    def __init__(
        self,
        screen: pygame.Surface,
        text: str,
        rect: pygame.Rect,
        on_click: callable,
    ):
        super().__init__(screen)
        self.text = text
        self.is_hover = False
        self.rect = rect
        self.on_click = on_click

    def update(self):
        mouse_coordinates = pygame.mouse.get_pos()
        self.is_hover = self.rect.collidepoint(mouse_coordinates)
        if self.is_hover and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            self.on_click()

    def render(self):
        background_color = COLORS["charcoal"] if self.is_hover else COLORS["gray"]
        pygame.draw.rect(self.screen, background_color, self.rect)

        words = FONTS["medium"].render(self.text, True, COLORS["white"])
        text_rect = words.get_rect(center=self.rect.center)
        self.screen.blit(words, text_rect)
