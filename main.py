# Example file showing a basic pygame "game loop"
from enum import Enum
import pygame
from game.game_renderer import GameRenderer
from menu.menu_renderer import MenuRenderer
from constants.mode import Mode
from mode_state import ModeState

MAX_FPS = 60
DIMENSIONS = (800, 600)

# pygame setup
pygame.init()

screen = pygame.display.set_mode(DIMENSIONS)
clock = pygame.time.Clock()

mode_state = ModeState()

renderers = {
    Mode.MENU: MenuRenderer(screen, mode_state),
    Mode.GAME: GameRenderer(screen, mode_state),
}


def handle_events(active_renderer) -> None:
    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        exit()
    active_renderer.update()


def render(active_renderer) -> None:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    active_renderer.render()
    # flip() the display to put your work on screen
    pygame.display.flip()


# Game Loop
while True:
    active_renderer = renderers[mode_state.mode]
    handle_events(active_renderer)
    render(active_renderer)
    clock.tick(MAX_FPS)
