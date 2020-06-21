"""
This is module for player class
"""


# ← ↑ → ↓


class Player():
    """
    PLayer class
    """

    def __init__(self, y, x, glyph):
        self.y = y
        self.x = x
        self.glyph = glyph

    def move(self, direction):
        """
        method to move player on grid
        """
        if direction == "left":
            self.x -= 1
            self.glyph = "←"
        elif direction == "right":
            self.x += 1
            self.glyph = "→"
        elif direction == "up":
            self.y -= 1
            self.glyph = "↑"
        elif direction == "down":
            self.y += 1
            self.glyph = "↓"
