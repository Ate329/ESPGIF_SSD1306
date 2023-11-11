# ESPGIF_SSD1306
This repository is modified based on ESPGIF by shraiwi. It can display GIF for ESP8266 with SSD1306 OLED screen.  

**I hope everyone who has SSD1306 and struggling of converting GIF and displaying GIF on it will find this repository helpful!**


# Introduction
This project is based on [ESPGIF](https://github.com/shraiwi/ESPGIF) by [shraiwi](https://github.com/shraiwi).  

Now the GIFCovert can be used for any size of GIF and convert into a size that you want.  

GIFDisplay in the folder GIFDisplay is being changed based on the use of SSD1306 instead of SSD1351 OLED screen.  
  
GIF.h in the folder GIFdisplay is an example of convertion with the example gif in the ExampleGIF folder.  
(The example uses SSD1306 NOT SSD1351 OLED screen)  

I used an online GIF editer called [EZGIF](https://ezgif.com) to adjust my GIF to the resolution I want and the size can be loaded into ESP8266.  
(Due to the fact that most ESP8266 development boards have little flash memory)

The change in each file will be described in detail in the README in each folder.


## Wiring
The wiring of SSD1306 and SSD1351 is very different.  

 SSD1306 | ESP8266 
 ------- | ------- 
   GND   |    G 
   VCC   |   3V
   SCL   |   D1
   SDA   |   D2


# Final effect
Here is a video of the final effect with the example GIF in this repository:  


https://github.com/Ateee329/ESPGIF_SSD1306/assets/74974216/7515b0c4-bacd-4f93-b454-598329e4a9a6


Sorry for the poor video quality:(  


# Thanks to
ESPGIF https://github.com/shraiwi/ESPGIF  

and the author  

shraiwi https://github.com/shraiwi


# License
This repository is licensed the same as the repository this repository is based on - Apache License 2.0  


# README from the ESPGIF (the original repository) 
-----------------------------------
## ESPGIF
ESPGIF is a project which uses an ESP8266, and an SSD1351 OLED display to display a GIF! This project has the Arduino Code and a tool to convert the GIF into a byte array.
## How do I use it?!
This a quick tutorial on how to use the library.
### Step 1: Setup
You will need:
#### Hardware
  - An ESP8266
  - A SSD1351 OLED display
#### Software
  - Python 3.7
    - The [PILLOW Library](https://pillow.readthedocs.io/)
    - [TKinter](https://docs.python.org/3/library/tkinter.html) (comes preinstalled with newer versions of python)
  - Arduino IDE
    - I have a repository with the modded Adafruit GFX (Allows for fast SPI transfers)
    - The Adafruit_SSD1351 library
    - Note: Both of the libraries are bundled in the "libraries" folder.
### Step 2: Setting the stuff up
Make sure you have all of the stuff listed above. If not, download and/or buy the required materials.

Go ahead and download the repo and unzip it.
- Drag the files in the `libraries` folder into the Arduino's `libraries` folder, or just use the library importer.

Drag the `GIFDisplay` folder into your Arduino projects folder, and open the `GIFDisplay.ino` script.
There are two files:
- `GIFDisplay.ino`
  - Contains code to display the data.
- `GIF.h`
  - Contains the actual image data

Drag the "GIFConvert" folder wherever you want (I recommend your "Documents" folder)

### Step 3: Wiring
Now that you've set up the project, let's actually display a GIF!

Here's the wiring diagram:

 OLED | ESP8266 
 ---- | ------- 
 SCLK | GPIO14  
 MOSI | GPIO13  
 DC   | GPIO5   
 CS   | GPIO15  
 RST  | GPIO4   

Note: The SCLK and MOSI pin mappings are immutable because the library _requires_ hardware SPI for a viewable framerate.

Once you have the pins connected go ahead and upload the sketch. If you did it right, you should see a spinning globe!
### Step 4: Displaying your own GIFs!
So, you wanna display your own GIF? 

Don't worry, this is going to be easy!

Remember the GIFConvert folder? Go ahead and open it and find the python script called, `GIFConvert.py`. Run it. It'll open a file selector. Choose your desired GIF, and press "Open". It will convert the image into an Arduino-readable format and open a .txt file containing the byte array. 

Use Ctrl+A/⌘+A to select all of the text in the open file, and use Ctrl+C/⌘+C to copy it to your clipboard.
Open the `GIF.h` file in the `GIFDisplay` folder, and use Ctrl+A/⌘+A to select all of the text, and then Ctrl+V/⌘+V to copy over the text.
Upload the code, and you should see the updated GIF!

If there is an error compiling, the GIF is probably too big. Choose a shorter/ lower framerate GIF and repeat this process.
