'''
Working code to control motors with a Pololu Dual G2 High Power Motor Driver,
via an Arduino taking input data from a FrSky D4R-II receiver,
getting signals from a Taranis X9D+ RC controller

Input from RC controller code: www.sparkfun.com/tutorials/348
'''

int ch1;              // receiver channel 1
int ch3;              // receiver channel 3
int x;                // ch1 to motor
int y;                // ch3 to motor

int ch1_high = 2002;     // highest input value for ch1
int ch1_low = 984;      // lowest input value for ch1
int ch3_high = 2003;     // highest input value for ch3
int ch3_low = 984;      // lowest input value for ch3

void setup() {
  pinMode(4, INPUT);  // channel 1 connected to pin 4
  pinMode(13, INPUT);  // channel 3 connected to pin 13

  Serial.begin(9600);
}

void loop() {
  // read the pulse width of each channel
  ch1 = pulseIn(4, HIGH, 25000);
  ch3 = pulseIn(13, HIGH, 25000);
/*
  Serial.print(ch3);
  Serial.println();
  delay(200);
*/
  // remap and constrain values to values the motor driver can use
  x = map(ch1, ch1_low, ch1_high, -480, 480);
  x = constrain(x, -480, 480);
  y = map(ch3, ch3_low, ch3_high, -480, 480);
  y = constrain(y, -480, 480);

  // send motor values to raspberry pi
  Serial.print(x);
  Serial.print("  ");
  Serial.print(y);
  Serial.println();
  //delay(100);
}
