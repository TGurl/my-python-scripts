#!/usr/bin/env python


from classes import person, room


rooms = []
#                                 N   E   S   W
rooms.append(room('Bathroom', None, None, 1, None, False))
rooms.append(room('Bedroom', 0, None, 4, None, False))
rooms.append(room('Hallway', None, 3, 4, 6, True))
rooms.append(room('Kitchen', None, 4, None, 2, False))
rooms.append(room('Living room', 2, 6, 5, 3, False))
rooms.append(room('Balcony', 4, None, None, None, False))
rooms.append(room('Dining Room', None, 2, None, 4, False))

persons = []
persons.append(person('Jennifer', 'Rossi', 18, 'F', None, False))
persons.append(person('Laura', 'Bailey', 19, 'F', None, False))
