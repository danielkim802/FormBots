int n1 = 9;
int n2 = 8;
int p1 = 10;
int p2 = 16;
int led = 7;


void setup() {
  delay(3000);
  pinMode(p1, OUTPUT);
  pinMode(p2, OUTPUT);
  pinMode(n1, OUTPUT);
  pinMode(n2, OUTPUT);
  pinMode(led, OUTPUT);

  digitalWrite(p1, LOW);
  digitalWrite(p2, LOW);
  digitalWrite(n1, HIGH);
  digitalWrite(n2, HIGH);
  delay(1000);
  forward();
  delay(500);
}

void loop() {
  // put your main code here, to run repeatedly:

  
}

//// Reverse, OUT2 HIGH
void reverse() {
  digitalWrite(p1, LOW);
  digitalWrite(p2, HIGH);
  digitalWrite(n1, HIGH);
  digitalWrite(n2, LOW);

  delayMicroseconds(400);
  //delay(500);
  
  digitalWrite(p1, LOW);
  digitalWrite(p2, LOW);
  digitalWrite(n1, HIGH);
  digitalWrite(n2, HIGH);
}

// Forward
void forward() {
  digitalWrite(p1, HIGH);
  digitalWrite(p2, LOW);
  digitalWrite(n1, LOW);
  digitalWrite(n2, HIGH);  

  delayMicroseconds(500);

  digitalWrite(p1, LOW);
  digitalWrite(p2, LOW);
  digitalWrite(n1, HIGH);
  digitalWrite(n2, HIGH);
}

