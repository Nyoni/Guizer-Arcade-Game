import arcade 
import pathlib

#Game constants
#Window dimensions

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Guizer Arcade"

#Assets path
ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"

class Platformer(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        #List to hold different sets of sprites
        self.coins = None
        self.background = None
        self.walls = None
        self.ladders = None
        self.goals = None
        self.enemies = None

        #one sprite for the player
        self.player = None

        #physics engine inodikwa
        self.pysics_engine = None

        #keeping score
        self.score = 0

        #keeping track of the level yatiri
        self.level = 1

        #load up our sounds here
        self.coin_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds"/ "coin.wav")
        )
        self.jump_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds"/ "jump.wav")

        )
        self.victory_sound = aracade.load_sound(
            str(ASSETS_PATH / "sounds"/ "victory.wav")
        )

    def setup(self):    #sets up the game to be begin playing. Add code that may need to be repeated throughout the game. eg initialize new levels on success or reset the current level on failure
        """This function sets game for the current level"""
        pass

    def on_key_press(self, key: int, modifiers: int ):  ##on key press & release allows for processing keyboard input independently.      #
        """Processes key presses

        -key(int)---> which key was pressed
        -modifiers(int)---> which modifiers where down at the time
        """

    def on_key_release(self, key: int, modifiers: int):
        """Processes key releases"""

    def on_update(self, delta_time: float):
        """Updates the position of game objects

        -delta_time(float)---> time after last call
        """
        pass

    def on_draw(self):  #where everything displayed in your game drawn
        pass


if __name__ == "__main__": #main entry point of the game
    window = Platformer()   #game object window based on the class defined
    window.setup()  #setup the game by calling window.setup
    arcade.run()    #start game loop by calling arcade.run                    