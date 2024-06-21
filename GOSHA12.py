import RPi.GPIO as GPIO     #импорт нужных библиотек
import time                                     
from tkinter import *
from PIL import Image
import matplotlib.pyplot as plt
import cv2


def blink(pin):              #функция для гуделки    
    GPIO.output(pin,GPIO.HIGH)  
    time.sleep(1)  
    GPIO.output(pin,GPIO.LOW)  
    time.sleep(1)  
    return  

def clicked():                      #функция для фоторграфии

    cap = cv2.VideoCapture(0)               # обозначаем камеру
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    ret, frame = cap.read()             #возвращает Тrue если кадр прочитан 
    cv2.imwrite("panda.jpg", frame)     #записывваем фото в папку с кодом
    cap.release()                       #освобождаем камеру 
    img = Image.open('panda.jpg')       #открываем это фото
    fig = plt.figure(figsize=(6,4))     
    ax = fig.add_subplot()
    ax.imshow(img)
    plt.show()

def cnock():                    #функция для видео
    motion_threshold=100
    video = cv2.VideoCapture(0)
 
    ret, fart1 = video.read()
    ret, fart2= video.read()
    ko1, ko2, ko3, ko4 = int(txt1.get()), int(txt2.get()), int(txt3.get()), int(txt4.get())
    frame1 = fart1[ko1:ko2, ko3:ko4]
    frame2 = fart2[ko1:ko2, ko3:ko4]
    fart1=fart2
    frame1 = frame2
    while video.isOpened():
        a, vid = video.read() 
        cv2.rectangle(vid, (ko3, ko1),(ko3+ko4, ko1+ko2), color=(0,0,225),thickness=4)
        src = cv2.absdiff(frame1, frame2)
        image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY ) 
        blur = cv2.GaussianBlur(image, (5,5), 0)
        _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilate = cv2.dilate(threshold, None, iterations=3)
        contour, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contour:  
            if cv2.contourArea(contour) > motion_threshold:
                # использовать номера выводов платы Raspberry Pi  
                GPIO.setmode(GPIO.BOARD)  

# настроить GPIO на выход  
                GPIO.setup(11, GPIO.OUT)  

# моргнуть GPIO17 50 раз  
                for i in range(0,1):  
                    blink(11)

                GPIO.cleanup()
                #winsound.Beep(1000, 1000)
               #playsound('50be6a16213ba29.mp3')
                break                               
        cv2.imshow("image", vid)
        fart1 = fart2
        frame1 = frame2
        ret, fart2 = video.read()
        frame2 = fart2[ko1:ko2, ko3:ko4]
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):        
            video.release() 
            cv2.destroyAllWindows()
            break
    
    
window = Tk()
window.title('GOSHA')
window.geometry('500x500')
#ввод нужного текста
txt1 = Entry(window, width=10)
txt1.place(x=250, y=55)
txt2 = Entry(window, width=10)
txt2.place(x=250, y=75)
txt3 = Entry(window, width=10)
txt3.place(x=250, y=130)
txt4 = Entry(window, width=10)
txt4.place(x=250, y=150)
#текста
lbl = Label(window, text='сделать фото', font=('Arial Bold', 17))
lbl.place(x=0, y=0)
lbl_2 = Label(window, text='вписать координаты', font=('Arial Bold', 17))
lbl_2.place(x=0, y=50)
lbl_4 = Label(window, text='y1',font=(10))
lbl_4.place(x=220, y=55)
lbl_5 = Label(window, text='y2',font=(10))
lbl_5.place(x=220, y=75)
lbl_6 = Label(window, text='x1',font=(10))
lbl_6.place(x=220, y=130)
lbl_7 = Label(window, text='x2',font=(10))
lbl_7.place(x=220, y=150)
#кнопки
btn = Button(window, text='сделать фото', command=clicked)
btn.place(x=320, y=0)
btn_2 = Button(window, text='вывести видео', command=cnock)
btn_2.place(x=320, y=95)

window.mainloop()
