#!/usr/bin/env python

import pygame

WIDTH, HEIGHT = 640, 480

class Scene:
    def on_start(self):
        pass

    def update(self, events, dt):
        pass

    def on_exit(self):
        pass


class Menu(Scene):
    def __init__(self, screen, scenes):
        self.scenes = scenes
        self.screen = screen
        self.font = pygame.font.Font('./data/fonts/QarmicSans.ttf', 32)
        self.music = pygame.mixer.Sound("./data/music/Overworld.ogg")
        self.channel = pygame.mixer.Channel(0)

    def on_start(self):
        self.channel.play(self.music, loops=-1, fade_ms=5000)

    def update(self, events, dt):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click, *_ = pygame.mouse.get_pressed()
                if left_click:
                    return self.scenes['game']

        # self.screen.blit(self.screen, "./data/img/citymap.png", (0,0))
        self.screen.blit(self.font.render("CITY MAP", True, 'white'), (60, 150))
        return self


class Game(Scene):
    def __init__(self, screen, scenes):
        self.scenes = scenes
        self.screen = screen
        self.font = pygame.font.Font("./data/fonts/QarmicSans.ttf", 32)
        self.music = pygame.mixer.Sound("./data/music/Home.ogg")
        self.channel = pygame.mixer.Channel(0)
        self.timer = 0

    def on_start(self):
        self.channel.play(self.music, loops=-1, fade_ms=5000)

    def update(self, events, dt):
        # Go back to menu if there hasn't been any events for 5 seconds
        if not events:
            self.timer += dt
            if self.timer >= 5:
                return self.scenes['menu']
            else:
                self.timer = 0

        # self.screen.blit(self.screen, "./data/img/bg.jpg", (0,0))
        self.screen.blit(self.font.render("This is Scene1", True, 'white'), (WIDTH / 15, 200))
        return self

    def on_exit(self):
        self.channel.stop()


def main():
    pygame.init()
    screen = pygame.display.set_mode((900,600), 0, 32)
    clock = pygame.time.Clock()

    # all the scenes
    scenes = {}
    scenes["menu"] = Menu(screen, scenes)
    scenes["game"] = Game(screen, scenes)

    # Start with menu
    scene = scenes["game"]
    scene.on_start()
    running = True
    while running:
        dt = clock.tick(30) / 1000.0

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    scene.on_exit()
                    scene = scenes['menu']
                    scene.on_start()
                    pygame.display.update()
                elif event.key == pygame.K_a:
                    scene.on_exit()
                    scene = scenes['game']
                    scene.on_start()
                    pygame.display.update()
                elif event.key == pygame.K_q:
                    running = False
            elif event.type == pygame.QUIT:
                running = False

        # switch scenes if there is a new scene
        scene.update(events, dt)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
