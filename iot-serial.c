void setup() {
  // initialize serial communication at 9600 bits per second:
  
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);

}

// the loop routine runs over and over again forever:
void loop() {
  int sensorValue1 = analogRead(A1);
  int sensorValue2 = analogRead(A2);
  int sensorValue3 = analogRead(A3);
  
  // Prints the condition of soil.  Dry, Wet or Perfect
  if (sensorValue1 >= 1000) (Serial.print("1,too dry,"));
  else if ((sensorValue1 <= 999) && (sensorValue1 >=901)) (Serial.print("1,perfect,"));
  else if (sensorValue1 <= 900) (Serial.print("1,too wet,"));
  else;
  Serial.println(sensorValue1);


   // Prints the condition of soil.  Dry, Wet or Perfect
  if (sensorValue2 >= 1000) (Serial.print("2,too dry,"));
  else if ((sensorValue2 <= 999) && (sensorValue2 >=901)) (Serial.print("2,perfect,"));
  else if (sensorValue2 <= 900) (Serial.print("2,too wet,"));
  else;
  Serial.println(sensorValue2);
  
  // Prints the condition of soil.  Dry, Wet or Perfect
  if (sensorValue3 >= 1000) (Serial.print("3,too dry,"));
  else if ((sensorValue3 <= 999) && (sensorValue3 >=901)) (Serial.print("3,perfect,"));
  else if (sensorValue3 <= 900) (Serial.print("3,too wet,"));
  else;
  Serial.println(sensorValue3);
  Serial.println(500);
  delay(500);        // delay in between reads for stability



}