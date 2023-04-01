#!/usr/bin/python3
"""ThreadBots module."""
import sys
import threading
from queue import Queue
from attr import attrs, attrib


class ThreadBot(threading.Thread):
    """ThreadBots module."""

    def __init__(self):
        """Initialize the thread."""
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()

    def manage_table(self):
        """
        Manage table.

        (1) prepare table
        (2) clear table
        (3) shutdown
        """
        while True:
            task = self.tasks.get()
            if task == 'prepare table':
                kitchen.give(to_=self.cutlery, knives=4, forks=4)
            elif task == 'clear table':
                self.cutlery.give(to_=kitchen, knives=4, forks=4)
            elif task == 'shutdown':
                return


@attrs
class Cutlery:
    """
    Cutlery class.

    Attributes:
        knives (int): number of knives
        forks (int): number of forks
    """

    knives: int = attrib(default=0)
    forks: int = attrib(default=0)
    lock = threading.Lock()

    def give(self, to_: 'Cutlery', knives=0, forks=0):
        """Give new cutlery."""
        self.change(-knives, -forks)
        to_.change(knives, forks)

    def change(self, knives, forks):
        """Change used knives and forks."""
        with self.lock:
            self.knives += knives
            self.forks += forks


kitchen = Cutlery(knives=100, forks=100)
bots: list[ThreadBot] = [ThreadBot() for i in range(10)]

for bot in bots:
    for i in range(int(sys.argv[1])):
        bot.tasks.put('prepare table')
        bot.tasks.put('clear table')
    bot.tasks.put('shutdown')

print('Kitchen inventory before service: ', kitchen)
for bot in bots:
    bot.start()

for bot in bots:
    bot.join()
print('Kitchen inventory after service: ', kitchen)
