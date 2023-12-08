int ledPin = 13; // Pin number for the built-in LED
char command;    // Variable to store the received command

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW); // Initial state is off
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming command
    command = Serial.read();

    // Process the received command
    if (command == '1') {
      digitalWrite(ledPin, HIGH); // Turn on the LED
      Serial.println("LED is ON");
    } else if (command == '0') {
      digitalWrite(ledPin, LOW); // Turn off the LED
      Serial.println("LED is OFF");
    }
  }

  // Your other code here
}
