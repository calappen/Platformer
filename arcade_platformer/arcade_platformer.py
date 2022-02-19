import arcade

class Platformer(arcade.Window):
    def __init__(self):
        pass

    def setup(self):
        #sets up game for current level
        pass

    def on_key_press(self, key: int, modifiers: int):
        #processes key presses

    def on_key_release(self, key: int, modifiers: int):
        #processes key releases

    def on_update(self, delta_time: float):
        #updates position of all game objects
        pass

    def on_draw(self):
        pass

if __name_ == "__main__":
    window = PLatformer()
    window.setup()
    arcade.run()