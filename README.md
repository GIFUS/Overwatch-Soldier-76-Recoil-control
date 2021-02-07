# Soldier76 Recoil control
The script was created to control the recoil on the character Soldier 76 in the game overwatch. It pulls your mouse down, thereby reducing the spread.

## Settings
All settings are found in the settings.yml file. Do not delete the settings file, otherwise the script may crash!

Change the value depending on your sensitivity in the game. The higher the value, the harder the script pulls the mouse down.
The standard settings are suitable for a sensitivity of 7.00 in the game and 500 dpi on the mouse(this is my sensitivity)
```yml
# Set the horizontal limit: 5 means a maximum of 5 pixels to the left or to the right every shot
horizontal_range: 2

# Set the minimum and maximum amount of pixels to move the mouse every shot
min_vertical: 5
max_vertical: 5.1

# Set the minimum and maximum amount of time in seconds to wait until moving the mouse again
min_firerate: 0.03
max_firerate: 0.04

# Set the toggle button
toggle_button: F5
```

### How to run?
There is no point in explaining for knowledgeable people. 
People who do not know how to use python can download the EXE file in the releases. https://github.com/GIFUS/Overwatch-Soldier-76-Recoil-control
