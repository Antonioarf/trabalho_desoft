# Pitfall
### Pygame Documentation

To run the game, you need to have python 3 and the dependencies listed in the requirements.txt file installed.

Command to install dependencies:
```pip install -r requirements.txt```

Command to run the game:
```python3 Pitfall.py```

Source code available [publicly on GitHub](https://github.com/Antonioarf/trabalho_desoft)

## Files
On the **src** folder, you can find the following directories and files:

**Fontes**: Contains the necessary files to import the game's fonts.

**Imagens**: Contains the necessary files to import the game's sprites.

**Sons**: Contains the necessary files to import the game's sounds.

### Pitfall.py
This is the main file of the game. It contains the main loop and the game's initialization, as well dealing with events that kill the program and eventual crashes and errors.


### Configuracoes.py
This file contains the game's configurations, such as the screen's size, FPS, colors saved as constants, and manages the imports fo the the game's fonts, sounds and sprites as well as defining the initial state of the states machine for the game.


### Classes.py
This defines the following classes:

1. *Player*

    This class creates the player object. It has two methods: init and update.  
    The init method loads the player's sprites and defines the shape for the colider.  
    The update method is responsible for the player's movement, and makes sure the player doesn't go off screen. Also inside the update method is the code to check if is time to change the player's image, and if it is, it changes it. No methods return anything.


2. *BARRIL*

    This class creates the obstacles objects that the player must avoid. It has two methods: init and update.  
    The init method loads the obstacle asset and defines the shape for the colider.  
    The update method is responsible for the movement of the obstacle and for checking if it has reached the end of the screen, and if it has, it resets the obstacle to the beginning of the screen. Also inside the update method is the code to check if is time to change the obstacle's image, and if it is, it changes it. No methods return anything.

3. *UNIC*

    This class works basicly the same as the BARRIL class, but it creates the obstacles with a random Y position and a different set os sprites.

4. *HOLE*

    This class creates the holes objects that the player must jump over. It has two methods: init and update.  
    The init method loads the hole asset and defines the shape for the colider.  
    The update method is empty, since nether the position or the sprite changes, but is is necessary for the class to work because of the superclass. No methods return anything.

5. *Premio*

    This class creates the collectables objects that the player can collect to gain points. It has two methods: init and update.  
    The init method treasure asset and defines the shape for the colider. The update method is empty, but is is necessary for the class to work because of the superclass. No methods return anything.


6. *LIVES*

    This class defines the markers for the live count for the player. It has two methods: init and update.  
    The init method loads the initial live count (3) and the heart icon. The update method is empty, but is is necessary for the class to work because of the superclass. No methods return anything.


7. *PREMIO*

    This class controls the game's score marker (it is not responsible for the points count, just to display it). It has two methods: init and update.  
    The init method loads the initial score (0) and the treasure icon. The update method is empty, but is is necessary for the class to work because of the superclass. No methods return anything.

8. *Back*

    This class controls the background of the game. It has two methods: init and update.  
    The init method loads the first background image and scales it to the screen's size. The update method is called every frame, and it checks if the time to change the image has been reached, and if it has, it loads the next image and scales it to the screen's size. No methods return anything.


9. *load_assets*

    This method loads the game's assets, by creating a dictionary with the sprites necessaries for objects from the classes above, and returns it. For assets that require animations on screen, the code creates a secondary list, with one object with each frame of the animation, and then adds it to the dictionary.

        def load_assets(img_dir, snd_dir, fnt_dir):
        assets = {}
        ...
        return assets

### Tela.py

This file contains the following functions:

1. *init_screen*
    
    This function is responsible for creating all assets to be used (according to the *load_assets* function) and wait for the first input from the user to start the game. It returns a state variable for the gameover.

2. *game_screen*

    This function is responsible for the game's main loop. It creates all the objects necessary for the game to run, and updates them every frame. It also checks for collisions between the player and the obstacles, and between the player and the collectables. It returns a state variable for the gameover and the score to be displayed.

3. *end_game* 

    This function is responsible for displaying the gameover screen, and wait for the first input from the user to restart the game or kill the program. It returns a state variable for the gameover.



## Credits
	Antonio Fonseca
	Gabriela Moreno Boriero
	Caroline Chaim

Game develop for "Desing de Software 2019.1" class at Insper, taught by professor Fabio Ayres.
    The documentation was develop for "Desenvolvimento Open-Source 2023.2" class at Insper, taught by professor Igor Montagner.