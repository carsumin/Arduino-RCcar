from tkinter import*
import socket
from tkinter import ttk
import time
import json

#connection create
#소켓을 생성한다
UDPsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

#dest
dest=("192.168.0.69",2391)

UDPsocket.setblocking(0)


#버튼클릭이벤트

def pressed():
    ttk.configure(text="RC카 조종기")
    
def processbtnLeft():
    print(1)
    a = "1"

    UDPsocket.sendto(a.encode(), dest)

    try :
        recved = UDPsocket.recvfrom(128)
        json_obj = json.loads(received[0])
        
        textbox.insert(json_obj.get('aCommand').get('aCommand'))

    except :
        pass

            
def processbtnRight():
    print(2)
    a = "2"

    UDPsocket.sendto(a.encode(), dest)

    try :
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0,recved[0])

    except :
        pass
    
def processbtnTop():
    print(3)
    a = "3"

    UDPsocket.sendto(a.encode(), dest)

    try :
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0,recved[0])

    except :
        pass
    
def processbtnBottom():
    print(4)
    a = "4"

    UDPsocket.sendto(a.encode(), dest)

    try :
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0,recved[0])

    except :
        pass

def processbtnStop():
    print(5)
    a = "5"

    UDPsocket.sendto(a.encode(), dest)

    try :
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0,recved[0])

    except :
        pass

def processbtnS():
    print(9)
    a = "9"

    UDPsocket.sendto(a.encode(), dest)

    try:
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0, recved[0])
    except:
        pass

#키보드이벤트
def processbtnLeft_key(event):
    print(1)
    a = "1"

    UDPsocket.sendto(a.encode(), dest)

    try :
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0,recved[0])

    except :
        pass
    
def processbtnRight_key(event):
    print(2)
    a = "2"

    UDPsocket.sendto(a.encode(), dest)

    try :
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0,recved[0])

    except :
        pass
    
def processbtnTop_key(event):
    print(3)
    a = "3"

    UDPsocket.sendto(a.encode(), dest)

    try :
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0,recved[0])

    except :
        pass

def processbtnBottom_key(evnet):
    print(4)
    a = "4"

    UDPsocket.sendto(a.encode(), dest)

    try :
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0,recved[0])

    except :
        pass
    
def processbtnStop_key(event):
    print(5)
    a = "5"

    UDPsocket.sendto(a.encode(), dest)

    try :
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0,recved[0])

    except :
        pass

def processbtnS_key(event):
    print(9)
    a = "9"

    UDPsocket.sendto(a.encode(), dest)

    try:
        recved = UDPsocket.recvfrom(128)
        textbox.insert(0, recved[0])
    except:
        pass

window = Tk()

#타이틀설정
window.title("tkinter 테스트")

#윈도우사이즈설정
window.geometry('320x240')
window.resizable(False, False)

    
buttonLeft = Button(window, width=10, text="◀", overrelief="solid", command=processbtnLeft)
buttonLeft.place(x=0, y=80)
window.bind("<Left>", processbtnLeft_key)

buttonRight = Button(window, width=10, text="▶", overrelief="solid", command=processbtnRight)
buttonRight.place(x=240, y=80)
window.bind("<Right>", processbtnRight_key)

buttonTop = Button(window, width=10, text="▲", overrelief="solid", command=processbtnTop)
buttonTop.place(x=120, y=30)
window.bind("<Up>", processbtnTop_key)

buttonBottom = Button(window, width=10, text="▼", overrelief="solid", command=processbtnBottom)
buttonBottom.place(x=120, y=130)
window.bind("<Down>", processbtnBottom_key)

buttonCenter = Button(window, width=10, text="STOP", overrelief="solid", command=processbtnStop)
buttonCenter.place(x=120, y=80)
window.bind("<space>", processbtnStop_key)

buttonCenter = Button(window, width=10, text="SENSOR", overrelief="solid", command=processbtnS)
buttonCenter.place(x=120, y=170)
window.bind("<Caps_Lock>",processbtnS_key)

str = StringVar() 
textbox = ttk.Entry(window, width=20)
textbox.pack()
textbox.insert(0, "센서값 출력창입니다.")
textbox.place(x=85, y=210)


window.mainloop()
UDPsocket.close()
