#!/usr/bin/env python

import os
import toml
import pygame

class Utils:
    def __init__(self):
        pygame.init()
        self.imagedir = os.path.join(
            os.getcwd(),
            'data',
            'images'
        )
        self.musicdir = os.path.join(
            os.getcwd(),
            'data',
            'music'
        )
        self.fontdir = os.path.join(
            os.getcwd(),
            'data',
            'fonts'
        )
        self.textdir = os.path.join(
            os.getcwd(),
            'data',
            'text'
        )
        self.tomldir = os.path.join(
            os.getcwd(),
            'data',
            'toml'
        )
        self.config =  self.read_toml(
            'config.toml'
        )

    def read_toml(self, toml_file_name):
        path = os.path.join(
            self.tomldir,
            toml_file_name
        )
        return toml.load(path)

    def save_toml(self, toml_file_name, data):
        path = os.path.join(
            self.tomldir,
            toml_file_name
        )
        with open(path, 'w') as f:
            result = toml.dump(data, f)
        return result

    def read_text(self, text_file_name):
        path = os.path.join(
            self.textdir,
            text_file_name
        )
        with open(path, 'r') as f:
            data = f.read().splitlines()
        return data
        
    def load_font(self, font_name, font_size):
        font = pygame.font.Font(
            os.path.join(
                self.fontdir,
                font_name
            ),
            font_size
        )
        return font

    def load_image(self, image_name):
        image = pygame.image.load(
            os.path.join(
                self.imagedir,
                image_name
            )
        )
        return image

    def load_image_convert(self, image_name):
        image = pygame.image.load(
            os.path.join(
                self.imagedir,
                image_name
            )
        ).convert()
        return image

    def load_music(self, music_file, channel=0, volume=0.5):
        music = pygame.mixer.Sound(
            os.path.join(
                os.path.join(
                    self.musicdir,
                    music_file
                )
            )
        )
        channel = pygame.mixer.Channel(channel)
        volume = channel.set_volume(volume)
        
        return music, channel
