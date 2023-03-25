import pygame
from interfaces.component_interface import ComponentInterface
from menu.menu_button import MenuButton
from mode_state import ModeState
from constants.mode import Mode

button_dimensions = (160, 40)
button_margin = 20


class MenuRenderer(ComponentInterface):
    def __init__(self, screen: pygame.Surface, mode_state: ModeState):
        super().__init__(screen)
        self.mode_state = mode_state
        self.center = (
            self.screen.get_width() / 2,
            self.screen.get_height() / 2,
        )
        self.newGameButton = MenuButton(
            screen,
            "New Game",
            pygame.Rect(
                [
                    *(
                        self.center[0] - (button_dimensions[0] / 2),
                        self.center[1] - (button_margin + button_dimensions[1]),
                    ),
                    *button_dimensions,
                ]
            ),
            self._startNewGame,
        )

    def _startNewGame(self):
        print("Starting New Game")
        self.mode_state.mode = Mode.GAME

    def update(self):
        if self.mode_state.mode != Mode.MENU:
            return
        self.newGameButton.update()

    def render(self):
        self.newGameButton.render()
