# ESPGIF_SSD1306
This repository is modified based on [ESPGIF](https://github.com/shraiwi/ESPGIF) (for SSD1351) by [shraiwi](https://github.com/shraiwi). It can display GIF for ESP8266 with SSD1306 OLED screen.  

**I hope everyone who has SSD1306 and struggling of converting GIF and displaying GIF on it will find this repository helpful!**


## Introduction
This project is based on [ESPGIF](https://github.com/shraiwi/ESPGIF) (for SSD1351) by [shraiwi](https://github.com/shraiwi).    

Now the GIFCovert can be used for any size of GIF and convert into a size that you want.  

GIFDisplay in the folder GIFDisplay is being changed based on the use of SSD1306 instead of SSD1351 OLED screen.  
  
GIF.h in the folder ExampleGIF is an example of convertion with the example gif in the ExampleGIF folder.  
(The example uses SSD1306 NOT SSD1351 OLED screen)  

I used an online GIF editer called [EZGIF](https://ezgif.com) to adjust my GIF to the resolution I want and the size can be loaded into ESP8266.  
(Due to the fact that most ESP8266 development boards have little flash memory)  

**YOU NEDD TO PUT THE CONVERTED FILE(GIF.h) IN THE SAME FOLDER WITH GIFDisplay.ino or GIFDisplayOld.ino or CHANGE THE CODE DEPENDING ON THE SCREEN YOU HAVE.**  

The change in each file will be described in detail in the README in each folder.


## Wiring
The wiring of SSD1306 and SSD1351 is quite different.  

 SSD1306 | ESP8266 
 ------- | ------- 
   GND   |    G 
   VCC   |   3V
   SCL   |   D1
   SDA   |   D2


## Demonstration
Here is a video of the final effect with the example GIF in this repository:  



https://github.com/Ate329/ESPGIF_SSD1306/assets/74974216/619176a2-10b5-434a-b542-7463140fce5e



Sorry for the poor video quality :(  


## Thanks to
ESPGIF https://github.com/shraiwi/ESPGIF  

## License
This repository is under the Apache 2.0 License, the same as [ESPGIF](https://github.com/shraiwi/ESPGIF).
