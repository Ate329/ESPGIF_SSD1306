#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Wire.h>
#include <SPI.h>
#include "GIF.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define NUM_PIXELS (SCREEN_WIDTH * SCREEN_HEIGHT)

#define OLED_RESET    -1
#define SCREEN_ADDRESS 0x3C  // You might need to change this based on your display

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

byte counter = 0;

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

void testdrawstyles(){
  //test text output
  display.clearDisplay();

  display.setTextSize(3);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,6);
  display.println(F("Hello, "));

  display.setTextSize(3);
  display.setCursor(0,40);
  display.println(F("World!!"));

  display.display();
  delay(2800);
  display.clearDisplay();
}

void loop() {
  // put your main code here, to run repeatedly:
  displayFrame(counter);
  
  counter++;
  if (counter == NUM_FRAMES) {
    counter = 0;
  }
  delay(130); //here you can adjust the display speed of each fram (1000 = 1s)
}

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
