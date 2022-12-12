#!/usr/bin/env python

import pygame
from utils import Utils

class Intro:
    def __init__(self):
        self.debug = False
        self.utils = Utils()
        self.screen = pygame.display.set_mode(
            (1920, 1080),
            pygame.FULLSCREEN
        )
        self.music, self.channel = self.utils.load_music(
            'Emotion2.ogg'
        )
        self.bg = self.utils.load_image_convert(
            'bg.png'
        )
        self.font = self.utils.load_font(
            'TypeMachine.ttf',
            32
        )
        self.warning_font = self.utils.load_font(
            'Typewriter.otf',
            32
        )
        self.girl_font = self.utils.load_font(
            'Valentina.ttf',
            78
        )
        self.man_font = self.utils.load_font(
            'Signatra.ttf',
            78
        )
        self.card_font = self.utils.load_font(
            'TypeMachine.ttf',
            80
        )
        self.title_font = self.utils.load_font(
            'DonGraffiti.otf',
            200
        )
        self.screen.blit(
            self.bg,
            (0,0)
        )

    def fadein(self, text):
        for x in range(255):
            text.set_alpha(x)
            text_rect = text.get_rect(
                center = self.screen.get_rect().center
            )
            self.screen.blit(
                self.bg,
                (0,0)
            )
            self.screen.blit(
                text,
                text_rect
            )
            pygame.display.flip()
            pygame.time.delay(2)

    def fadeout(self, text):
        for x in range(255):
            text.set_alpha(255 - x)
            text_rect = text.get_rect(
                center = self.screen.get_rect().center
            )
            self.screen.blit(
                self.bg,
                (0,0)
            )
            self.screen.blit(
                text,
                text_rect
            )
            pygame.display.flip()
            pygame.time.delay(2)

    def fadetoblack(self, delay=1):
        self.channel.fadeout(delay * 1000)
        for x in range(255):
            self.screen.fill((0, 0, 0))
            self.bg.set_alpha(255 - x)
            self.screen.blit(
                self.bg,
                (0,0)
            )
            pygame.display.update()
            pygame.time.wait(2)
        pygame.time.delay(delay * 1000)

    def run(self):
        self.channel.play(
            self.music,
            loops=-1,
            fade_ms=1000
        )
        lines = self.utils.read_text(
            'intro.txt'
        )

        for line in lines:
            text = line.split('/')
            speaker = text[0]
            spoken = text[1]
            pause = int(text[2])
            match speaker:
                case 'uncle':
                    render_text = self.man_font.render(
                        spoken,
                        True,
                        'mediumblue'
                    )
                case 'girl':
                    render_text = self.girl_font.render(
                        spoken,
                        True,
                        'fuchsia'
                    )
                case 'buttler':
                    render_text = self.man_font.render(
                        spoken,
                        True,
                        'deepskyblue'
                    )
                case 'warning':
                    render_text = self.warning_font.render(
                        spoken,
                        True,
                        'red'
                    )
                case 'title':
                    render_text = self.title_font.render(
                        spoken,
                        True,
                        'goldenrod3'
                    )
                case 'card':
                    render_text = self.card_font.render(
                        spoken,
                        True,
                        'white'
                    )
                case 'blank':
                    render_text = self.font.render(
                        spoken,
                        True,
                        'black'
                    )
                case _:
                    render_text = self.font.render(
                        spoken,
                        True,
                        'white'
                    )
            self.fadein(render_text)
            delay = 1000 if not self.debug else 0
            pygame.time.delay(pause * delay)
            self.fadeout(render_text)

        self.fadetoblack()
        
