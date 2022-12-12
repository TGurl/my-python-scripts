#!/usr/bin/env python

from classes import person, room


class Game:
    def __init__(self):
        self.rooms = []
        self.rooms.append(room('Bathroom', None, None, 1, None, False))
        self.rooms.append(room('Bedroom', 0, None, 2, None, False))
        self.rooms.append(room('Hallway', None, 3, 4, 6, True))
        self.rooms.append(room('Kitchen', None, 4, None, 2, False))
        self.rooms.append(room('Living room', 2, 6, 5, 3, False))
        self.rooms.append(room('Balcony', 4, None, None, None, False))
        self.rooms.append(room('Dining Room', None, 2, None, 4, False))

        self.persons = []
        self.persons.append(person('Jennifer', 'Rossi', 18, 'F', None, False))
        self.persons.append(person('Laura', 'Bailey', 19, 'F', None, False))

        self.location = 1

    def get_room_name(self, idx):
        return self.rooms[idx].name

    def show_routes(self):
        valid = []
        if self.rooms[self.location].north is not None:
            name = self.get_room_name(self.rooms[self.location].north)
            print(f"- You can go North to {name}")
            valid.append(self.rooms[self.location].north)
        if self.rooms[self.location].east is not None:
            name = self.get_room_name(self.rooms[self.location].east)
            print(f"- You can go East to {name}")
            valid.append(self.rooms[self.location].east)
        if self.rooms[self.location].south is not None:
            name = self.get_room_name(self.rooms[self.location].south)
            print(f"- You can go South to {name}")
            valid.append(self.rooms[self.location].south)
        if self.rooms[self.location].west is not None:
            name = self.get_room_name(self.rooms[self.location].west)
            print(f"- You can go West to {name}")
            valid.append(self.rooms[self.location].west)
        return valid

    def run(self):
        possible_routes = ['n', 'e', 's', 'w']
        running = True

        while running:
            print(self.rooms[self.location].name)
            valid_routes = self.show_routes()
            ans = input("Where you you want go? : ").lower()
            idx = possible_routes.index(ans)
            if idx not in valid_routes:
                print("You can't go there...")
            else:
                new_name = self.rooms[idx].name
                self.location = 

