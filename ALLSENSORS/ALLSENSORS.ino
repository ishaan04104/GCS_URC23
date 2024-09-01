
#include "SparkFun_AS7265X.h" //Click here to get the library: http://librarymanager/All#SparkFun_AS7265X
#include <dht11.h>


#define DHT11PIN 4 // Analog Pin sensor is connected to
dht11 DHT11;
AS7265X sensor;
int sv;
int sensorPin = A0; 
int sensorValue;  
int limit = 300;

int greenLed = 11;
int smokeA0 = A3;
// Your threshold value
int sensorThres = 1000;


void setup()
{
  pinMode(greenLed, OUTPUT);
  pinMode(smokeA0, INPUT);
  
  Serial.begin(9600);

  delay(500);//Delay to let system boot
  delay(1000);//Wait before accessing Sensor

  if (sensor.begin() == false)
  {
    Serial.println("Sensor does not appear to be connected. Please check wiring. Freezing...");
    while (1);
  }
}

void loop()
{

// riad
          sensor.takeMeasurements(); //This is a hard wait while all 18 channels are measured

          Serial.print(sensor.getCalibratedA()); //410nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedB()); //435nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedC()); //460nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedD()); //485nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedE()); //510nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedF()); //535nm
          Serial.print(",");

          Serial.print(sensor.getCalibratedG()); //560nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedH()); //585nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedR()); //610nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedI()); //645nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedS()); //680nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedJ()); //705nm
          Serial.print(",");

          Serial.print(sensor.getCalibratedT()); //730nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedU()); //760nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedV()); //810nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedW()); //860nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedK()); //900nm
          Serial.print(",");
          Serial.print(sensor.getCalibratedL()); //940nm
          Serial.print(",");

          Serial.println();


// Soil
        sensorValue = analogRead(sensorPin); 
        Serial.println(sensorValue);
        
        if (sensorValue<limit) {
        digitalWrite(13, HIGH); 
        }
        else {
        digitalWrite(13, LOW); 
        }
        delay(1000);


// gas
        int analogSensor = analogRead(smokeA0);
        
        Serial.println(analogSensor);
        // Checks if it has reached the threshold value
        if (analogSensor > sensorThres)
        {
          digitalWrite(greenLed, LOW);
        }
        else
        {
          digitalWrite(greenLed, HIGH);
        }
        delay(100);

//DH 11

        int chk = DHT11.read(DHT11PIN);
        Serial.println((float)DHT11.humidity, 2);
        Serial.println((float)DHT11.temperature, 2);
      
        delay(2000);



  }