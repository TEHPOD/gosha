//команда ГОША г. ВОлгоград РРО 2024 категория искусственный интеллект

//библиотека для подключения блютус дополнительные порты tx rx
#include <SoftwareSerial.h>

const int arduino_rx = 8; //порт отправки
const int arduino_tx = 10; //порт получения
SoftwareSerial mySerial (arduino_rx, arduino_tx); //создаем класс для обмена данными между ардуино и модулем блютус

int k = 0; //переменная которую ардуино отправляет в управляющий модуль
int rightHand = 0; //переменная фиксирующая цепь 5 вольт и ГНД правой руки
int leftHand = 0; //переменная фиксирующая цепь левой руки
int leftFoot = 0; //переменная фиксирующая цепь левой ноги
int rightFoot = 0; //переменная фиксирующая цепь правой ноги
int head = 0; //переменная фиксирующая цепь головы

//переменные для отправки в монитор порта ардино для тестирования функции
String rH = "rightHand";
String lH = "leftHand";
String lF = "leftFoot";
String rF = "rightFoot";
String h = "head";

//функция которая ничего не возвращает, но получает 3 переменные частота,
//текст в монитор порта и переменную для отпрвки в управляющий модуль
void kostum(int freq, String meat, int msg)
{
  tone(13, freq); //включаем пищалку
  mySerial.write(msg); //передаем переменную для передачи по блютус в управляющий модуль
  Serial.println(meat); вывод текстовых переменных в монитор порта
  delay(500);
}

void setup()  {
  pinMode( arduino_rx, INPUT); pinMode( arduino_tx, OUTPUT);
  Serial.begin(9600);       //обмен данными ардуинки и компьютера
  mySerial.begin(9600);    //по умолчанию скорость Bluetooth модуля с Arduino в режиме AT команд 38400 иногда 9600
  Serial.println( "<<< Start! send_kostum>>>");
  //объявляем порты на получение сигнала
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(13, OUTPUT); //объявляем порт пищалки
}

void loop() {
  //проверочные строки
  // Serial.println(k);
  /* mySerial.write(k);
    Serial.print( "k=");
    Serial.println( k);
    delay(500);*/
  //записываем в переменные текущее состояние порта ардуино для контроля целостности цепи
  rightHand = digitalRead(2);
  leftHand = digitalRead(3);
  leftFoot = digitalRead(4);
  rightFoot = digitalRead(5);
  head = digitalRead(6);
  //если в цепи будет разрыв, то в порт не будет поступать 5 вольт и на порту будет логический ноль
  if (rightHand < 1)
  {
    k = 2; //переменная для отпавки в управляющий модуль
    kostum(500, rH, k); //запуск функции
  }
  if (leftHand < 1)
  {
    k = 3; //переменная для отпавки в управляющий модуль
    kostum(700, rH, k);//запуск функции
  }
  if (leftFoot < 1)
  {
    k = 4; //переменная для отпавки в управляющий модуль
    kostum(900, rH, k);//запуск функции
  }
  if (rightFoot < 1)
  {
    k = 5;//переменная для отпавки в управляющий модуль
    kostum(1100, rH, k); //запуск функции
  }
  if (head < 1)
  {
    k = 6; //переменная для отпавки в управляющий модуль
    kostum(1500, rH, k); //запуск функции
  }
  noTone(13);
}
