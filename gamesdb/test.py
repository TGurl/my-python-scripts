#!/usr/bin/env python
import os
import pickle
from time import sleep

class GameDB:
    def __init__(self):
        self.gamelist = []
        self.prompt = '> '

    def show_games(self):
        for item in self.gamelist:
            print(item[0], item[1])

    def input_new_game(self):
        while True:
            os.system('clear')
            name = input('Name  : ').lower()
            if name in ['q', 'quit']:
                break
            url = input('URL   : ').lower()
            new_game = (name, url, False)
            self.gamelist.append(new_game)
        self.gamelist.sort()

    def load_db(self):
        if os.path.exists('pickle.db'):
            with open('pickle.db', 'rb') as file:
                self.gamelist = pickle.load(file)

    def save_db(self):
        with open('pickle.db', 'wb') as file:
            pickle.dump(self.gamelist, file)

    def parse_gamelist(self):
        if os.path.exists('listofgames.txt'):
            with open('listofgames.txt', 'r') as file:
                lines = file.readlines()

            for line in lines:
                line = line.strip('\n').strip()
                if line.startswith('- ['):
                    line = line.replace('- [', '')
                    line = line.replace('](', '*|*')
                    line = line.replace(')', '')
                line = line.split('*|*')
                self.gamelist.append((line[0], line[1], False))
                print('added:', line[0])
            self.gamelist.sort()
            self.save_db()

    def search_database(self):
        query = input(self.prompt)
        while True:
            items_found = []
            for item in self.gamelist:
                if query.lower() in item[0].lower():
                    items_found.append(item)

            if query in ['quit', 'q']:
                self.prompt = '> '
                break

            if len(items_found) == 0:
                print("Nothing found...")
                query = input(self.prompt)
            else:
                for item in items_found:
                    print(item[0])
                query = input(self.prompt)

    def run(self):
        self.parse_gamelist()
        self.load_db()
        while True:
            os.system('clear')
            print('= GamesDB - A database of sexgames. =')
            print('>> System ready', end='\n\n')
            command = input(self.prompt).lower()
            match command:
                case 'query' | 'search':
                    self.prompt = 'query > '
                    self.search_database()
                case 'quit' | 'q':
                    break
                case _:
                    print(">> not a valid command, type 'help' for list of commands.")
                    sleep(2)


if __name__ == "__main__":
    app = GameDB()
    app.run()
