# Introduction
GIFDisplay.py is the original file created by [shraiwi](https://github.com/shraiwi).

GIFDisplayNew.py is the file modified one based on the need of using SSD1306 instead of SSD1351.


# Changes
There might be some changes are not being mentioned.  


## Added
```c
#include <Wire.h>
```
```c
#define OLED_RESET    -1
#define SCREEN_ADDRESS 0x3C  // You might need to change this based on your display
```


## Deleted
```c
// Replace with your SPI Pins. 
// SCLK and MOSI definitions are just there for reference, changing those values will not change their actual mappings.
// BTW, these map to the GPIOs of the ESP8266, not what it says on the board. CHECK YOUR BOARD'S PINOUTS!!!
#define SCLK_PIN 14
#define MOSI_PIN 13
#define DC_PIN   5
#define CS_PIN   15
#define RST_PIN  4
```
```c
uint32_t start = 0;
uint32_t end = 0;

uint16_t buf[NUM_PIXELS];
```


## Modifications

### Changed from
```c
#define SCREEN_HEIGHT 128
```
to
```c
#define SCREEN_HEIGHT 64
```

### Changed from
```c
Adafruit_SSD1351 tft = Adafruit_SSD1351(SCREEN_WIDTH, SCREEN_HEIGHT, &SPI, CS_PIN, DC_PIN, RST_PIN);
```
to
```c
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
```

### Changed from
```c
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  
  tft.begin();
  
  // Tried to save some power here, lol.
  // WiFi.disconnect();
  // WiFi.forceSleepBegin();
  
  // Was used for debug
  // displayFrame(10);
  // displayFrame(0);
}
```
to
```c
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  display.display();
  delay(2000);  // Pause for 2 seconds

  testdrawstyles(); 
  
  display.clearDisplay();
  display.display();
}
```

### Changed from
```c
  delay(DELAY);
```
in loop() to
```c
  delay(130);
```

### Changed from
```c
void displayFrame(byte frame) {
  
  for (uint16_t i = 0; i < NUM_PIXELS; i++){
    byte index = pgm_read_byte_near(&frameData[frame][i]);
    buf[i] = pgm_read_word_near(&palette[index]);
  }
  
  tft.startWrite();

  tft.setAddrWindow(0, 0, 128, 128);
  
  for (uint16_t i = 0; i < NUM_PIXELS; i++){
    tft.write16(buf[i]);
  }
  
  tft.endWrite();
}
```
to
```c
void displayFrame(byte frame) {
  display.clearDisplay();

  for (uint16_t i = 0; i < NUM_PIXELS; i++){
    byte index = pgm_read_byte_near(&frameData[frame][i]);
    uint16_t color = pgm_read_word_near(&palette[index]);
    if (color != 0) {  // Check if the pixel is not transparent
      display.drawPixel(i % SCREEN_WIDTH, i / SCREEN_WIDTH, SSD1306_WHITE);
    }
  }
  
  display.display();
}
```
