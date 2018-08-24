
#include <SoftwareSerial.h>

int soil;


// replace with your channel's thingspeak API key
String apiKey = "PVKAH015ZZN2I70Z";

// connect 2 to TX of ESP
// connect 3 to RX of ESP
SoftwareSerial ser(2,3); // RX, TX

// this runs once
void setup() {                

  // enable debug serial
  Serial.begin(115200); 
  // enable software serial
  ser.begin(115200);
  
  // reset ESP8266
  //ser.println("AT+RST");
}


// the loop 
void loop() {
  soil = analogRead(A0);
  esp_8266();
}


void esp_8266()
{
 // convert to string
  String soil_send = String(soil);
  //Serial.print(soil_send);
  // TCP connection
  String cmd = "AT+CIPSTART=\"TCP\",\"";
  cmd += "184.106.153.149"; // api.thingspeak.com
  cmd += "\",80";
  ser.println(cmd);
   
  if(ser.find("Error")){
    Serial.println("AT+CIPSTART error");
    return;
  }
  
  // prepare GET string
  String getStr = "GET /update?api_key=";
  getStr += apiKey;
  getStr +="&field1=";
  getStr += soil_send;
  getStr += "\r\n\r\n";

  // send data length
  cmd = "AT+CIPSEND=";
  cmd += String(getStr.length());
  ser.println(cmd);

  if(ser.find(">")){
    ser.print(getStr);
  }
  else{
    ser.println("AT+CIPCLOSE");
    // alert user
    Serial.println("AT+CIPCLOSE");
  }
    
  // thingspeak needs 15 sec delay between updates
  delay(16000);  
}
