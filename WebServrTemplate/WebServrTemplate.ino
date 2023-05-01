#include <ArduinoHttpServer.h>
#include <SPI.h>
#include <WiFi101.h>
#include "ServoEasing.hpp"
#include "arduino_secrets.h" 
#include "DHT.h"

// PIN DEFINITIONS
#define DHTPIN1 5
#define DHTPIN2 9 

#define SMPIN1 A5  // Soil Meisture 
// #define SMPIN2 A6

#define PUMPPIN 10
// #define PUMPBUTTONPIN 4

#define SERVOPIN 8
// #define SERVOBUTTONPIN 9

#define HUMPIN 3

#define DHTTYPE DHT11   // DHT 11
// PIN DEFINITIONS

// VARIABLE DEFINITIONS
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
int keyIndex = 0;

int status = WL_IDLE_STATUS;

DHT dht1(DHTPIN1, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);
ServoEasing servo;

int smValue1 = 0;
int smValue2 = 0;
int smPrecentage1 = 0;
int smPrecentage2 = 0;
int pumpBtnState = 0;
int pumpState = 0;
int humidifierState = 0;
int pos = 0;

WiFiServer server(80);
// VARIABLE DEFINITIONS


String DhtToJson() {
  float humidity1 = dht1.readHumidity();
  float temperature1 = dht1.readTemperature();
  float humidity2 = dht2.readHumidity();
  float temperature2 = dht2.readTemperature();

  String dht1_stats = String("{\"id\": 1, \"temperature\": ") + String(temperature1) + String(", \"humidity\": ") + String(humidity1) + String("}");
  String dht2_stats = String("{\"id\": 2, \"temperature\": ") + String(temperature2) + String(", \"humidity\": ") + String(humidity2) + String("}");

  String json = String("[") + dht1_stats + String(",") + dht2_stats + String("]");

  return json;
}

String SmToJson() {
  smValue1 = analogRead(SMPIN1);
  smPrecentage1 = 100 - ((smValue1 / 1023.00) * 100);
  // smValue2 = analogRead(SMPIN2);    

  String sm1_stats = String("{\"id\": 1, \"humidity\": ") + String(smPrecentage1) + String("}");
  // String sm2_stats = String("{\"id\": 2, \"humidity\": ") + String(smValue2) + String("}");

  String json = String("[") + sm1_stats + String("]");

  return json;
}


void ForkStateChange(int newState) {
  int startPos = 0;
  int endPos = 70;

  if(newState == 1){
    servo.easeTo(endPos, 25);
  }
  if(newState == 0){
    servo.easeTo(startPos, 25);
  }
}

void PumpStateChange(int newState) {
  pumpState = newState;
}

void HumidifierStateChange(int newState) {
  humidifierState = newState;
}

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;
  }

  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("WiFi shield not present");
    while (true);
  }

  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
    delay(6000);
  }
  server.begin();
  printWiFiStatus();

  // Attaching pins to sensors
  pinMode(PUMPPIN, OUTPUT);
  pinMode(HUMPIN, OUTPUT);
  pinMode(SMPIN1, INPUT);
  // pinMode(SMPIN2, INPUT);


  servo.attach(SERVOPIN);

  dht1.begin();
  dht2.begin();
}

void loop() {

  // pumpBtnState = digitalRead(PUMPBUTTONPIN);

  if(pumpState == 1) digitalWrite(PUMPPIN, HIGH);

  if(pumpState == 0) digitalWrite(PUMPPIN, LOW);

  if(humidifierState == 1) digitalWrite(HUMPIN, HIGH);

  if(humidifierState == 0) digitalWrite(HUMPIN, LOW);


  WiFiClient client = server.available();
  if (client.connected())
   {
      // Connected to client. Allocate and initialize StreamHttpRequest object.
      ArduinoHttpServer::StreamHttpRequest<1024> httpRequest(client);

      if (httpRequest.readRequest())
      {
        String url = httpRequest.getResource()[0];
        Serial.println(url);

        String response = "";
         
        // /get_air_stats
        if(url == "get_air_stats") {
          response = DhtToJson();
        }

        // /get_soil_stats
        else if(url == "get_soil_stats") {
          response = SmToJson();
        }

        // /change_pump_state/0 or /change_pump_state/1
        else if(url == "change_pump_state") {
          int new_state = httpRequest.getResource()[1].toInt();
          PumpStateChange(new_state);
          response = "{\"status\": \"OK\"}";
        }

        // /change_fork_state/0 or /change_fork_state/1
        else if(url == "change_fork_state") {
          int new_state = httpRequest.getResource()[1].toInt();
          ForkStateChange(new_state);
          
          response = "{\"status\": \"OK\"}";
        }

        // /change_humidifier_state/0 or /change_humidifier_state/1
        else if(url == "change_humidifier_state") {
          int new_state = httpRequest.getResource()[1].toInt();
          HumidifierStateChange(new_state);
          
          response = "{\"status\": \"OK\"}";
        }

        else Serial.println("Unknown request");


        Serial.println(response);

        client.println("HTTP/1.1 200 OK");
        client.println("Content-Type: application/json");
        client.println();
        client.print(response);
      }
      else
      {
         ArduinoHttpServer::StreamHttpErrorReply httpReply(client, httpRequest.getContentType());
         const char *pErrorStr( httpRequest.getError().cStr() );
         String errorStr(pErrorStr);
         httpReply.send( errorStr );
      }

      delay(1); 
      Serial.println("client disconnected");
      Serial.println();
      client.stop();
  }
}

void printWiFiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}
