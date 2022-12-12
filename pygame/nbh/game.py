#!/usr/bin/env python

import os
import pygame


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.cwd = os.getcwd()
        self.imagedir = os.path.join(self.cwd, "data", "images")
        self.musicdir = os.path.join(self.cwd, "data", "music")
        self.textdir = os.path.join(self.cwd, "data", "text")
        self.confdir = os.path.join(self.cwd, "data", "config")
        self.fontdir = os.path.join(self.cwd, "data", "fonts")

        self.background = pygame.image.load(
            os.path.join(self.imagedir, "bg.png")
        ).convert()
        self.gui = pygame.image.load(
            os.path.join(self.imagedir, 'gui.png')
        )
        self.music = pygame.mixer.Sound(
            os.path.join(self.musicdir, "Home.ogg")
        )
        self.channel = pygame.mixer.Channel(0)
        self.barfont = pygame.font.Font(
            os.path.join(self.fontdir, 'QarmicSans.ttf'),
            32
        )

    def start_music(self):
        self.channel.set_volume(0.5)
        self.channel.play(self.music, loops=-1, fade_ms=5000)

    def pause_music(self):
        self.channel.pause()

    def stop_music(self):
        wait = 2000
        self.channel.fadeout(wait)
        pygame.time.wait(wait)

    def quit_dialog(self, screen):
        return False

    def start(self):
        # Enter the game
        self.start_music()

        running = True
        while running:
            bar = self.barfont.render(
                "Day: 1  Sexy: 0%  Bank: $0  Cup: A",
                True,
                'fuchsia'
            )
            bar2 = self.barfont.render(
                "Rent: $100  Slept with: 0  Job: None  Health: 100%",
                True,
                'fuchsia'
            )
            width = self.screen.get_width()
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.gui, (0, 0))
            self.screen.blit(bar, ((width - bar.get_width())/2, 10))
            self.screen.blit(bar2, ((width - bar2.get_width())/2, 54))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = self.quit_dialog(self.screen)

            # Update the screen
            pygame.display.update()

        # Exit the game
        self.stop_music()
        pygame.quit()
