# ShadowverseTool
Tools help playing Shadowverse. [WIP]  
**Note**  
- all of the scripts will play the game by reading your screen and controling your mouse.
- trigger fail-safe by keep moving mouse cursor to upper-left corner in case that you can't stop the program properly.
- all script only work in game window resolution `1024 x 768`.
- all templates are captured in traditional chinese, you have to take the screenshot and crop your templates if you want to work in different language or game resolution.

**TODO**
- python interface to play the game

## Dependency
In windows: `pip install -r requires.txt`  
In MacOS: `pip install -r requires-MacOS.txt`  
In Ubuntu: not tested yet.

## `2pick.py`
This tool will automatically exchange **all** your `take two tickets` to `pack tickets` by entering arena and give up immediately. This programe will stop when you have no `take two tickets` left (or you can stop the program by trigger fail-safe). 

To start the program:  
1. setting shadowverse resolution to `1024 x 768`
2. switch to main page
3. run the script `python 2pick.py`. please ensure that all the buttons to click is visible on the screen.
