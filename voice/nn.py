import os
import time

# let AI help by scanning stackoverflow and giving any found solution to programmer
# within seconds

class VA:
    def __init__(self):
        self.name = "Rey"
        self.wakeUpCommands = {"Hey", "Rey", "Yo", "Hello"}

    def run(self):
        self.recognizer.listen()

    def quit(self):
        sys.exit()
