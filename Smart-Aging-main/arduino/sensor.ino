#include <esp_now.h>
#include <WiFi.h>
#include <HTTPClient.h>

const int PIR_SENSOR_OUTPUT_PIN = 13;  /* PIR sensor O/P pin */
int warm_up;
int d=4;
bool b=1,c=0;
int count1=0;
int count2=0;
const char* ssid = "<wifi_name>";
const char* password = "<wifi_password>";
String URL = "http://192.168.1.9:8000/api/motion/";

void connectWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
}

void setup() {
  pinMode(PIR_SENSOR_OUTPUT_PIN, INPUT);
  Serial.begin(115200); /* Define baud rate for serial communication */
  Serial.println("Waiting For Power On Warm Up");
  delay(3000); /* Power On Warm Up Delay */
  Serial.println("Ready!");
  connectWiFi();
}

void loop() {
   int sensor_output;
  sensor_output = digitalRead(PIR_SENSOR_OUTPUT_PIN);
  if( sensor_output == LOW )
  {
    if( warm_up == 1 )
     {
      Serial.print("Warming Up\n\n");
      warm_up = 0;
      delay(500);
     }
  count2++;  
  if(count2==1)
  {
    HTTPClient http; 
    http.begin(URL);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    
    String postData = "SensorId=" + String(d) + "&SensorStatus=" + String(c); 
    int httpCode = http.POST(postData); 
    String payload = http.getString(); 
    
    Serial.print("URL : "); Serial.println(URL); 
    Serial.print("Data: "); Serial.println(postData); 
    Serial.print("httpCode: "); Serial.println(httpCode); 
    Serial.print("payload : "); Serial.println(payload); 
    Serial.println("--------------------------------------------------");
    Serial.print("No object in sight\n\n");
    }
    count1=0;
    delay(1000);
  }
  else
  {count1++; 
  if(count1==1)
  {
    HTTPClient http; 
    http.begin(URL);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    
    String postData = "SensorId=" + String(d) + "&SensorStatus=" + String(b); 
    int httpCode = http.POST(postData); 
    String payload = http.getString(); 
    
    Serial.print("URL : "); Serial.println(URL); 
    Serial.print("Data: "); Serial.println(postData); 
    Serial.print("httpCode: "); Serial.println(httpCode); 
    Serial.print("payload : "); Serial.println(payload); 
    Serial.println("--------------------------------------------------");
    Serial.print("Object detected\n\n"); 
    warm_up = 1;
    delay(1000);
    }
   count2=0;
  }
}