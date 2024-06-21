//Гоша г.Волгоград искусственный интеллект

#include <Servo.h>

Servo myservo5;  //объявляем серву за горизонтальное перемещение
Servo myservo6;//объявляем серву за вертикальное перемещение


int max_=180; //максимальный угол поворота сервы
int min_=0; //минимальный угол поворота сервы
int up_cur=90; //текущий угол поворота вертикальной сервы
int down_cur=90;//текущий угол поворота горизонтальной сервы
int up=0; //состояние кнопки вверх
int down=0; //состояние кнопки вниз
int right=0; //состояние кнопки вправо
int left=0;// состояние кнопки влево
void setup() {
  myservo5.attach(5);  //привязка сервы к порту 5
  myservo6.attach(6); //привязка сервы к порту 6
pinMode(4, INPUT); //вниз кнопка
pinMode(7, INPUT); //влево  кнопка
pinMode(8, INPUT);//вправо кнопка
pinMode(11, INPUT); //вверх кнопка
Serial.begin(9600); //обмен данным с пк
//считываем состояие кнопок
right=digitalRead(8); 
left=digitalRead(7);
up=digitalRead(11);
down=digitalRead(4);
Serial.println("Start_servo");
delay(1000);
Serial.print("right = ");
Serial.println(right);
Serial.print("left = ");
Serial.println(left);
Serial.print("up = ");
Serial.println(up);
Serial.print("down");
Serial.println(down);
Serial.println("zero_position wait 5 sek");
delay(2000);
//приводим сервы стартовое положение

myservo5.write(up_cur);                  
myservo6.write(down_cur);                  
delay(3000);
Serial.println("run");
}

void loop() {
  //считываем состояние кнопок
right=digitalRead(8);
left=digitalRead(7);
up=digitalRead(11);
down=digitalRead(4);
//проверка нажата ли кнопка вправо
  if (right>0 and down_cur<max_)
  {
    down_cur=down_cur+5; //изменение угла
    myservo6.write(down_cur); //пововрот сервы
    Serial.print("vpravo na = ");
    Serial.println(down_cur);
    delay(300);
    }
    //проверка нажата ли кнопка влево
   if (left>0 and down_cur>min_)
  {
    down_cur=down_cur-5; //изменение угла
    myservo6.write(down_cur); //пововрот сервы
    Serial.print("vlevo na = ");
    Serial.println(down_cur);
    delay(300);
    }
    //проверка нажата ли кнопка вверх

  if (up>0 and up_cur<max_)
  {
    up_cur=up_cur+5;//изменение угла
    myservo5.write(up_cur);//пововрот сервы
    Serial.print("vverh na = ");
    Serial.println(up_cur);
    delay(300);
    }
    //проверка нажата ли кнопка вниз
   if (down>0 and up_cur>min_)
  {
    up_cur=up_cur-5;//изменение угла
    myservo5.write(up_cur);//пововрот сервы
    Serial.print("vniz na = ");
    Serial.println(up_cur);
    delay(300);
    }
  
  }
