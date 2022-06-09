int data;
void setup()
{
    Serial.begin(9600);
    pinMode(13, OUTPUT);
    pinMode(12, OUTPUT);
    pinMode(8, OUTPUT);
    digitalWrite(13, LOW); /** LEFT **/
    digitalWrite(12, LOW); /** CENTER **/
    digitalWrite(8, LOW); /** RIGHT **/
    
}

void loop()
{
    while (Serial.available())
    {
        data = Serial.read();
    }

    if (data == '1'){ /** LEFT **/
        digitalWrite(13, HIGH);
        digitalWrite(8, LOW);
        digitalWrite(12, LOW); 
    }
    else if (data == '2'){ /** CENTER **/
        digitalWrite(13, LOW);
        digitalWrite(8, LOW); 
        digitalWrite(12, HIGH);
    }
    else if (data == '3'){ /** RIGHT **/
        digitalWrite(13, LOW); 
        digitalWrite(8, HIGH);
        digitalWrite(12, LOW);
    }
    else if (data=='4'){
        digitalWrite(13, LOW); 
        digitalWrite(8, LOW);
        digitalWrite(12, LOW);
    }
    
}
