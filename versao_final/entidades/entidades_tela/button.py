import pygame


class Button:
    def __init__(self, posicao: tuple, click_method, img_static: str = "button-static.png", img_hover: str = "button-hover.png", text: str = None) -> None:
        super().__init__()
        self.__image_static = img_static
        self.__image_hover = img_hover
        self.__click_method = click_method
        self.__text = text  
        self.__posicao = posicao

        self.__image = pygame.image.load(f"versao_final/styles/assets/telas/buttons/{self.__image_static}")
        self.__rect = self.__image.get_rect()
        self.__rect.x = posicao[0]
        self.__rect.y = posicao[1]
        self.__text_color = (255,255,255)
        font_path = "versao_final/styles/assets/fonte.ttf"
        self.__font = pygame.font.Font(font_path, 50)

        self.__sound_click = pygame.mixer.Sound('versao_final/styles/assets/sound_effects/button-click.wav')

        if not self.__text is None:
            self.__text_surface = self.__font.render(self.__text, True, self.__text_color)
            self.__text_rect = self.__text_surface.get_rect()
            self.__text_rect.x = self.__rect.x + self.rect.width/2 - self.__text_rect.width/2 
            self.__text_rect.y = self.__rect.y + self.rect.height/2 - self.__text_rect.height/2

    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image
    
    def click(self):
        return self.__click_method()
    
    def update(self, event):
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]  # Verifica se o botão esquerdo do mouse foi pressionado

        if self.__rect.collidepoint(mouse_pos):
            if clicked:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__sound_click.play()
                    self.click()  # Chama a função associada ao clique
            else:
                self.__image = pygame.image.load(f"versao_final/styles/assets/telas/buttons/{self.__image_hover}")
                self.__text_color = (32, 28, 28)
                self.__text_surface = self.__font.render(self.__text, True, self.__text_color)
        else:
            self.__image = pygame.image.load(f"versao_final/styles/assets/telas/buttons/{self.__image_static}")
            self.__text_color = (255, 255, 255)
            self.__text_surface = self.__font.render(self.__text, True, self.__text_color)

    def desenhar_tela(self, tela):
        tela.blit(self.__image, self.rect)
        if not self.__text is None:
            tela.blit(self.__text_surface, self.__text_rect)


