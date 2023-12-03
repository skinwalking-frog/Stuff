"""
Oliver Rothe
classes for use in project 7
"""

class headphone():
    def __init__(self):
        self.connected = True
        self.color = "black"
        


    def __str__(self):
        return f"connection: {self.connected}"
    






class NoAudioError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
