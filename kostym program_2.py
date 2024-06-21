import cv2  #подключаем библиотеку опен сиви
import serial #подключем библиотеку для работы с портами tx rx
#для передачи и получения команд по блютус
from time import sleep #подключаем бибилотеку для расстановки пауз
received_data = 0

# созраняем в переменные изображения рук, ног и головы
rightHand = cv2.imread("right_hand.jpg")
leftHand = cv2.imread("left_hand.jpg")
leftFoot = cv2.imread("left_noga.jpg")
rightFoot = cv2.imread("right_noga.jpg")
head = cv2.imread("head.png")

#настраиваем подключение по портам tx rx на скорости 9600 бод
#аналогично скороти работы блютус модуля
ser = serial.Serial ("/dev/ttyS0", 9600)
#запускаем цикл программы
while True:
    #считываем в переменную байты с блютус модуля
    received_data = ser.read()
    sleep(0.03)#ждем 30 мили секунд
    data_left = ser.inWaiting()
    received_data += ser.read(data_left)
    print (received_data)#выводим пришедшее значение на экран
    mur=int(received_data[len(received_data)-2])#сохраняем в переменную только полезные значения из полученных
    print ("received_data=",received_data[len(received_data)-2])
    print("mur=",mur)
    ser.write(received_data) #отправляем значение назад возможно для реализации контроля
    #в соответсвии с полученной командой 2,3,4,5,6 ВЫВОДИМ содержание картинки соответсвующей переменной рука, нога, голова
    if mur == 2:
        cv2.imshow("rightHand",rightHand)
        cv2.waitKey(0) #ждем нажатие любой клавиши
    if mur == 3:
        cv2.imshow("leftHand",leftHand)
        cv2.waitKey(0)#ждем нажатие любой клавиши
    if mur == 4:
        cv2.imshow("leftFoot",leftFoot)
        cv2.waitKey(0)#ждем нажатие любой клавиши
    if mur == 5:
        cv2.imshow("rightFoot",rightFoot)
        cv2.waitKey(0)#ждем нажатие любой клавиши
    if mur == 6:
        cv2.imshow("head",head)
        cv2.waitKey(0)#ждем нажатие любой клавиши

   
