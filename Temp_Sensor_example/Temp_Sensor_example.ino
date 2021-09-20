/*************************************************** 
  This is a library example for the MLX90614 Temp Sensor

  Designed specifically to work with the MLX90614 sensors in the
  adafruit shop
  ----> https://www.adafruit.com/products/1748
  ----> https://www.adafruit.com/products/1749

  These sensors use I2C to communicate, 2 pins are required to  
  interface
  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Wire.h>
#include <Adafruit_MLX90614.h>
#include <SPI.h>
#include <SD.h>

boolean loud = false;
const int chipSelect = 4;
unsigned long runtime;
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
  Serial.begin(9600);
  //Serial.println("CLEARDATA"); //clears up any data from other programs
  //Serial.println("Adafruit MLX90614 test");  
  if (!SD.begin(chipSelect)) {

    Serial.println("initialization failed. Things to check:");

    Serial.println("1. is a card inserted?");

    Serial.println("2. is your wiring correct?");

    Serial.println("3. did you change the chipSelect pin to match your shield or module?");

    Serial.println("Note: press reset or reopen this serial monitor after fixing your issue!");

    while (true);

  }
  Serial.println("initialization done.");
  mlx.begin();  
}

void loop() {
  File dataFile = SD.open("datalog.txt", FILE_WRITE);
  if (dataFile) {
    if (loud) { //if you want the output to look prettier
      
    Serial.print("Ambient = "); Serial.print(mlx.readAmbientTempF()); 
    Serial.print("*F\tObject = "); Serial.print(mlx.readObjectTempF()); Serial.println("*F");
    Serial.print("Ambient = "); Serial.print(mlx.readAmbientTempC()); 
    Serial.print("*C\tObject = "); Serial.print(mlx.readObjectTempC()); Serial.println("*C");

    dataFile.print("Ambient = "); dataFile.print(mlx.readAmbientTempF()); 
    dataFile.print("*F\tObject = "); dataFile.print(mlx.readObjectTempF()); dataFile.println("*F");
    dataFile.print("Ambient = "); dataFile.print(mlx.readAmbientTempC()); 
    dataFile.print("*C\tObject = "); dataFile.print(mlx.readObjectTempC()); dataFile.println("*C");
    
    } else { // raw output with a delimiter for easier data gathering
    //print to serial
    runtime = millis();
    Serial.print(runtime); Serial.print("|");
    Serial.print(mlx.readAmbientTempF()); Serial.print(";"); 
    Serial.print(mlx.readObjectTempF()); Serial.print(";");
    Serial.print(mlx.readAmbientTempC()); Serial.print(";");
    Serial.print(mlx.readObjectTempC()); Serial.println(";");
    //print to sd card
    dataFile.print(runtime); dataFile.print("|");
    dataFile.print(mlx.readAmbientTempF()); dataFile.print(";"); 
    dataFile.print(mlx.readObjectTempF()); dataFile.print(";");
    dataFile.print(mlx.readAmbientTempC()); dataFile.print(";");
    dataFile.print(mlx.readObjectTempC()); dataFile.println(";");

    }
    dataFile.close();
  }
  
  //Serial.println();
  delay(500);
}
