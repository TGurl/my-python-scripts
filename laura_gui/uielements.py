import pygame
import pygame.freetype
from pygame.sprite import Sprite

class UIElements(Sprite):
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        self.center_position = center_position
        self.text = text
        self.font_size = font_size
        self.bg_rgb = bg_rgb
        self.text_rgb = text_rgb
        self.action = action
        self.mouse_over = False

        self.generate_elements()
        super().__init__()

    def generate_elements(self):
        default_image = self.create_surface_with_text()
        highlighted_image = self.create_surface_with_text(expand=True)

        self.images = [default_image, highlighted_image]

        self.rects = [default_image.get_rect(center=self.center_position),
                      highlighted_image.get_rect(center=self.center_position)]

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
    
    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def create_ui_element(self):
        pass

    def create_surface_with_text(self, text, font_size, text_rgb, bg_rgb, expand=False):
        """ Returns surface with text written on """
        if not expand:
            font = pygame.freetype.SysFont("Courier", self.font_size, bold=True)
        else:
            font = pygame.freetype.SysFont("Courier", self.font_size * 1.2, bold=True)

        surface, _ = font.render(text=self.text, fgcolor=self.text_rgb, bgcolor=self.bg_rgb)
        return surface.convert_alpha()
