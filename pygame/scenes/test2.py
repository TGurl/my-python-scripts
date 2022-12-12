#!/usr/bin/env python

import pygame
from time import sleep
from pygame.mixer import fadeout

from pygame.time import delay


class LongHornBar:
    def __init__(self):
        self.music = pygame.mixer.Sound("./data/music/Chill2.ogg")
        self.channel = pygame.mixer.Channel(0)
        self.background = pygame.image.load("./data/img/longhornbar.jpg")

    def on_start(self, screen):
        screen.blit(self.background, (0,0))
        self.channel.play(self.music, loops=-1, fade_ms=5000)

    def update(self):
        pygame.display.update()
        showmap = True
        while showmap:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        showmap = False

    def on_exit(self):
        self.channel.stop()


class CityMap:
    def __init__(self):
        self.music = pygame.mixer.Sound("./data/music/Overworld.ogg")
        self.channel = pygame.mixer.Channel(0)
        self.background = pygame.image.load("./data/img/citymap.png")

    def on_start(self, screen):
        screen.blit(self.background, (0,0))
        self.channel.play(self.music, loops=-1, fade_ms=5000)

    def update(self):
        pygame.display.update()
        showmap = True
        while showmap:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        showmap = False

    def on_exit(self):
        self.channel.stop()



class Game:
    def __init__(self):
        self.music = pygame.mixer.Sound("./data/music/Home.ogg")
        self.channel = pygame.mixer.Channel(0)
        self.background = pygame.image.load("./data/img/bg.jpg")

    def on_start(self, screen):
        screen.blit(self.background, (0,0))
        self.channel.play(self.music, loops=-1, fade_ms=1000)

    def on_return(self, screen):
        screen.blit(self.background, (0,0))
        self.channel.play(self.music, loops=-1, fade_ms=1000)

    def update(self):
        pygame.display.update()

    def on_exit(self):
        self.channel.pause()

class Introduction:
    def __init__(self):
        self.music = pygame.mixer.Sound("./data/music/Home2.ogg")
        self.channel = pygame.mixer.Channel(0)
        self.font = pygame.font.Font("./data/fonts/QarmicSans.ttf", 48)
        self.gamefont = pygame.font.Font("./data/fonts/Allura-Regular.ttf", 64)
        self.description = pygame.font.Font("./data/fonts/mplus-1m-regular.ttf", 64)
        self.titlefont = pygame.font.Font("./data/fonts/BLKCHCRY.TTF", 180)
        self.background = pygame.image.load("./data/img/intro3.jpg")
    
    def on_start(self, screen):
        screen.blit(self.background, (0,0))
        self.channel.play(self.music, loops=-1, fade_ms=1000)

    def update(self, screen):
        lines = [
            "warning/This game contains incest and bestiality.",
            "description/Four years ago today",
            "mandy/No, Daddy, no...",
            "daddy/Be quiet! Stop crying like a baby!",
            "mandy/It hurts Daddy! It hurts...",
            "daddy/Oh, just stop whining and spread your legs!",
            "mandy/No, Daddy. I don't want to.",
            "daddy/Quiet! Time to grow up!",
            "mother/Ssh, baby. Just relax, just relax sweetie.",
            "mandy/Why mom? Why?",
            "daddy/My god, she's tight!",
            "mother/You are fourteen now and a almost woman.",
            "mother/And us women exist just to please all boys.",
            "mother/That's our purpose in life.",
            "mandy/Mommy, it hurts so much!",
            "mother/We are sluts and whores, on earth just to please.",
            "daddy/Almost, stop resisting!",
            "mother/Just relax baby. Just let him in.",
            "mandy/OUCH! STOP IT! IT HURTS!",
            "mandy/OUCH DADDY!",
            "daddy/Oh yeah, I'm in.",
            "mandy/OH GOD! I CAN FEEL HIM INSIDE ME!",
            "daddy/You're no longer a virgin babygirl!",
            "mother/Oh sweetie, congratulations!",
            "daddy/You're a woman now!",
            "mandy/He's in so deep, Mommy.",
            "mother/I am so proud of you.",
            "daddy/Oh God, she's so tight!",
            "mandy/Just be gentle Daddy. It still hurts a little.",
            "daddy/Don't worry, I will be gentle.",
            "mother/Does it feel better?",
            "mandy/A little.",
            "daddy/I will start moving now.",
            "mandy/Just move slowly Daddy.",
            "mother/It will feel better if Daddy starts moving.",
            "mother/I promise it will",
            "daddy/I love this tight pussy!",
            "mandy/Will Daddy make me a mommy too?",
            "mother/In time, sweetie, in time.",
            "mother/Just relax and enjoy!",
            "mandy/Oh Daddy!",
            "mandy/You are so deep inside me",
            "mother/See? It feels nice, doesn't it?",
            "mandy/Yes Mommy, it feels good now.",
            "mother/Daddy has a nice cock, doesn't he?",
            "mandy/I love Daddy's cock, Mommy. It feels so good!",
            "daddy/Wow, I love me some virgin pussy!",
            "mandy/You're so big Daddy!",
            "daddy/You're a slut now, Mandy!",
            "mother/Daddy is going to fuck you every night.",
            "daddy/Would you like that?",
            "mandy/Oh yes Daddy, you can fuck me any time.",
            "mandy/Any place you want.",
            "mandy/I love you Daddy!",
            "mother/And soon Daddy will make you a mommy too.",
            "mother/Just like Grandpa did for me.",
            "mandy/I would love that, Daddy!",
            "mandy/I want to have all your babies, Daddy.",
            "mother/Do like it when Daddy fucks you?",
            "mandy/Oh yes, I love it when Daddy fucks me!",
            "mandy/Fuck me hard, Daddy!",
            "mother/Give her all your cum, honey.",
            "mother/Fill that tiny pussy with your seed.",
            "mandy/Oh yes, I want to feel you come inside me!",
            "mother/You heard her.",
            "mandy/I want to be fucked all day long, Mommy.",
            "mother/Would you like all boys to fuck you?",
            "mandy/I will fuck anyone you want me to!",
            "mandy/Just as long as the pay me enough.",
            "mother/She's ready now.",
            "mother/Our little whore.",
            "mandy/Oh yes, I am a",
            "title/Natural Born Hooker",
            "gameby/A sensual game by Transgirl",
        ]
        wait = 4
        color = 'wite'
        for line in lines:

            text = line.split('/')
            if text[0] == 'title':
                color = 'gold3'
                wait = 10
            elif text[0] == 'description':
                wait = 3
            elif text[0] == 'warning':
                color = 'red'
                wait = 2
            elif text[0] == "gameby":
                color = 'burlywood1'
                wait = 3
            elif text[0] == 'mother':
                color = 'deeppink3'
                wait = 3
            elif text[0] == 'mandy':
                color = 'fuchsia'
                wait = 3
            elif text[0] == 'daddy':
                color = 'royalblue'
                wait = 3
            elif text[0] == 'black':
                color = 'black'
                wait = 3
            
            if text[0] == 'title':
                on_screen = self.titlefont.render(text[1], True, color)
            elif text[0] == 'description':
                on_screen = self.description.render(text[1], True, 'white')
            elif text[0] == 'warning':
                on_screen = self.description.render(text[1], True, color)
            elif text[0] == 'gameby':
                on_screen = self.gamefont.render(text[1], True, color)
            else:
                on_screen = self.font.render(text[1], True, color)

            on_screen_rect = on_screen.get_rect(center=(1920/2, 1080/2))

            # fade in
            for x in range(255):
                screen.fill((0,0,0))
                screen.blit(self.background, (0,0))
                on_screen.set_alpha(x)
                screen.blit(on_screen, on_screen_rect)
                pygame.display.update()
                pygame.time.delay(2)
            
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    self.on_exit()
                elif event == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.on_exit()

            pygame.time.delay(wait * 1000)
           
            # fade out
            for x in range(255):
                screen.fill((0,0,0))
                screen.blit(self.background, (0,0))
                on_screen.set_alpha(255 - x)
                screen.blit(on_screen, on_screen_rect)
                pygame.display.flip()
                pygame.time.delay(2)


    def on_exit(self):
        wait = 3000
        self.channel.fadeout(wait)
        pygame.time.delay(wait)
        self.channel.stop()


def main():
    pygame.init()
    screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
    # clock = pygame.time.Clock()
    intro = Introduction()
    game = Game()
    citymap = CityMap()
    lbar = LongHornBar()


    running = True

    intro.on_start(screen)
    intro.update(screen)
    intro.on_exit()
    game.on_start(screen)
    while running:
        game.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    game.on_exit()
                    citymap.on_start(screen)
                    citymap.update()
                    game.on_return(screen)
                elif event.key == pygame.K_b:
                    game.on_exit()
                    lbar.on_start(screen)
                    lbar.update()
                    game.on_return(screen)
                elif event.key == pygame.K_q:
                    running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
