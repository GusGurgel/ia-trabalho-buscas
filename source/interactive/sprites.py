from settings import *

class Cell(pygame.sprite.Sprite):
    def __init__(self, matrix_pos=(0, 0), *groups):
        super().__init__(*groups)

        self.display_rect = pygame.display.get_surface().get_frect()

        self.state = "none"
        self.matrix_pos = matrix_pos

        self.image = pygame.surface.Surface(
            (CELL_SIZE, CELL_SIZE),
            pygame.SRCALPHA
        )

        self.rect = self.image.get_frect()

        self.rect.bottomleft = self.display_rect.bottomleft


        self.rect.bottomleft += pygame.Vector2(
             (CELL_SIZE * self.matrix_pos[0]),
            -(CELL_SIZE * self.matrix_pos[1]),
        )

        self.set_state(state="generated")

    def set_state(self, state="none"):
        if state not in CELL_STATES:
            raise Exception(f"Invalide cell state: {state}")
        
        self.state = state

        pygame.draw.rect(
            self.image, 
            COLORS["cell_" + state],
            pygame.Rect((0, 0), (CELL_SIZE, CELL_SIZE)),
        )
        
        pygame.draw.rect(
            self.image, 
            COLORS["cell_stroke"],
            pygame.Rect((0, 0), (CELL_SIZE, CELL_SIZE)),
            CELL_STROKE_SIZE
        )

        text = CELL_FONT.render(f"{self.matrix_pos[0]},{self.matrix_pos[1]}", True, COLORS["text_" + state])
        text_rect = text.get_frect(center=(CELL_SIZE/2, CELL_SIZE/2))
        self.image.blit(text, text_rect)

class Grid():
    def __init__(self, all_sprites):
        self.cells_matrix = [[]] * (MAP_SIZE+1)
        for i in range(MAP_SIZE+1):
            for j in range(MAP_SIZE+1):
                self.cells_matrix[i].append(Cell((i, j), all_sprites))
                
    
    def update(self, dt):
        pass
    
