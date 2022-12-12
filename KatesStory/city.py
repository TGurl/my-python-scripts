#!/usr/bin/env python

from dataclasses import dataclass
import random

@dataclass
class blocks:
    turn_left: str
    turn_right: str
    turn_up: str
    turn_down: str
    horizontal: str
    vertical: str
    side_left: str
    side_right: str
    side_up: str
    side_down: str
    crossing: str
    building: str
    park: str

class City:
    def __init__(self):
        blocks.turn_left = "┘"
        blocks.turn_right = "┌"
        blocks.turn_up = "└"
        blocks.turn_down = "┐"
        blocks.side_left = "┤"
        blocks.side_right = "├"
        blocks.side_up = "┴"
        blocks.side_down = "┬"
        blocks.crossing = "┼"
        blocks.horizontal = "─"
        blocks.vertical = "│"
        blocks.building = "■"
        blocks.park = "░"

        self.blocks = [
            blocks.turn_left, blocks.turn_right,
            blocks.turn_up, blocks.turn_down,
            blocks.side_left, blocks.side_right,
            blocks.side_up, blocks.side_down,
            blocks.horizontal, blocks.vertical,
            blocks.building, blocks.park
        ]

        self.connections = []
        self.total_blocks = 13
        self.map = []

    def init(self):
        self.connections.append("1100")
        self.connections.append("1001")
        self.connections.append("0110")
        self.connections.append("0011")
        self.connections.append("1011")
        self.connections.append("1110")
        self.connections.append("1101")
        self.connections.append("0111")
        self.connections.append("1111")
        self.connections.append("0101")
        self.connections.append("1010")
        self.connections.append("rhdvlhuv")
        self.connections.append("rhdvlhuv")

    def generate_city(self):
        rows = 8
        columns = 8
        map = []
        map.append(blocks.turn_right)
        for x in range(rows * columns):
            block = random.randint(0, len(self.blocks) - 3)
            map.append(self.blocks[block])

        
        counter = 0
        for x in range(rows * columns):
            if counter == 8:
                endstr = "\n"
                counter = 0
            else:
                endstr = ""
                counter += 1
            print(map[x], end=endstr)
            




