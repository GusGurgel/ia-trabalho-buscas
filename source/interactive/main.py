from settings import *
from sprites import *

class App:
    def __init__(self):
        # Window size fix
        if system() == "Windows":
            ctypes.windll.user32.SetProcessDPIAware()

        # Init services
        pygame.init()

        # Creating main surface
        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT), vsync=1
        )

        # Set title
        pygame.display.set_caption(WINDOW_TITLE)

        # Proprieties
        self.running = True
        self.clock = pygame.Clock()
        self.all_sprites = pygame.sprite.Group()

        self.gride = Grid(self.all_sprites)

        # Setting up ui
        self.ui_manager = pygame_gui.UIManager(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            theme_path=join(RELATIVE_PATH, "ui_theme.json"),
        )

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.running = False

            self.ui_manager.update(dt)
            self.all_sprites.update(dt)

            self.display_surface.fill(COLORS["bg"])
            self.all_sprites.draw(self.display_surface)

            self.ui_manager.draw_ui(self.display_surface)

            # flip the screen buffer
            pygame.display.update()

        # Quit services
        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.run()