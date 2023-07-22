
import binascii
import sys
import time
from typing import List, Any
from PyQt5.QtCore import QTimer
import serial
import threading
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from serial_1 import Ui_MainWindow
receve_flag=False
data2='0'
data5=0
auto_mode=False
end_flag=False
def get_com_list():
    Com_List=[]
    plist=list(serial.tools.list_ports.comports())
    if len(plist)>0:
        for i in range(len(plist)):
            Com_List.append(list(plist[i])[0])
    print(Com_List)
    return Com_List
def send_r_s():
    request_data = '01 03 02 00 12'
    r_s = bytes.fromhex(request_data)
    ser2.write(r_s)
def send_r_s_periodically():
    global receve_flag
    while receve_flag:
        send_r_s()  # 调用 send_r_s 函数
        receve_flag=False
class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)
        self.setupUi(self)
        self.timer1=QTimer(self)
        self.timer2=QTimer(self)
        self.timer1.timeout.connect(self.time_out)
        self.timer2.timeout.connect(self.time_out2)
        self.thread=threading.Thread(target=self.my_loop)
        self.thread.start()
    def time_out(self):
        global ser,timer_value,data2
        data=ser.read(10)
        data2=str(data)[2:-1]  #去掉前面的b''
        if data2!='':
            if 'kpa' in data2:
                self.textBrowser_2.append(data2)
            else:
                self.textBrowser.append(data2)
        self.timer1.start(timer_value)
    def time_out2(self):
        global ser2,timer_value,receve_flag,data5
        data5=0
        data3=ser2.read(40)
        data4=str(data3)[2:-1]  #去掉前面的b''
        if data4!='':
            receve_flag=True
            send_r_s_periodically()
            if len(data4)>40:
                data4 = str(binascii.b2a_hex(data3))[20:26]  # 切片，选出传感器Z轴力数据
                data5 = int(data4, 16)
                data5 = str((8389017 - int(data4, 16) - 409) / 1000)  # 力数据转换单位与进制
                self.textBrowser_3.append(data5)
            else:
                data6 = str(binascii.b2a_hex(data3))[2:-1]
                self.textBrowser_3.append(data6)
        self.timer2.start(timer_value)
    def port_change1(self,text):
        global serialPort1
        serialPort1=text
        print('串口号：',serialPort1)
        ser.port=serialPort1
        print('port_change1')
    def baud_change1(self,text):
        global baudRate1
        baudRate1=int(text)
        print('波特率',baudRate1)
        print('baud_change1')
    def connect_btu1(self):
        global ser,serialPort1,baudRate1,com_list
        com_list=get_com_list()
        if com_list!=[]:
            if serialPort1!=None:
                ser.port=serialPort1
                ser.baudrate=baudRate1
                if self.pushButton.text()=='连接1':
                    ser.open()
                    self.timer1.start(timer_value)
                    self.pushButton.setText('关闭1')
                    print('串口已连接')
                else:
                    ser.close()
                    self.timer1.stop()
                    self.pushButton.setText('连接1')
                    print('串口已关闭')
            else:
                myWin.comboBox.clear()
                for i in range(len(com_list)):
                    myWin.comboBox.addItem(com_list[i])
                serialPort1=com_list[0]
        else:
            serialPort1=None
            myWin.comboBox.clear()
        print('connect_btu1')
    def set_dir(self):
        global serialPort1,ser
        if self.pushButton.text()=='关闭1' and serialPort1!=None:
            send_dir=self.textEdit.toPlainText()
            if send_dir=='1':
                SendDir='a'+'0'
                ser.write(SendDir.encode('utf-8'))
                print('发送数据:' + SendDir)
            elif send_dir=='2':
                SendDir='a'+'1'
                ser.write(SendDir.encode('utf-8'))
                print('发送数据:' + SendDir)
            elif send_dir=='3':
                SendDir='p'+'0'
                ser.write(SendDir.encode('utf-8'))
                print('发送数据:' + SendDir)
            elif send_dir=='4':
                SendDir='p'+'1'
                ser.write(SendDir.encode('utf-8'))
                print('发送数据:' + SendDir)
            else:
                print('输错了')
                ser.write('ha error!!!'.encode('utf-8'))
        else:
            print('先打开串口')
    def set_speed(self):
        global serialPort1, ser
        if self.pushButton.text() == '关闭1' and serialPort1 != None:
            send_speed = self.textEdit_3.toPlainText()
            send_dir = self.textEdit.toPlainText()
            print(send_dir)
            if send_dir=='1' or send_dir=='2':
                SendSpeed='b'+send_speed
                ser.write(SendSpeed.encode('utf-8'))
            elif send_dir=='3' or send_dir=='4':
                SendSpeed='q'+send_speed
                ser.write(SendSpeed.encode('utf-8'))
            else:
                print('输错了')
                ser.write('haha error!!!'.encode('utf-8'))
            print('发送数据:' + send_speed)
        else:
            print('先打开串口')
        print('set_speed')
    def set_step(self):
        global serialPort1, ser
        if self.pushButton.text() == '关闭1' and serialPort1 != None:
            send_step = self.textEdit_2.toPlainText()
            send_dir = self.textEdit.toPlainText()
            print(send_dir)
            if send_dir == '1' or send_dir == '2':
                SendStep = 'c' + send_step
                ser.write(SendStep.encode('utf-8'))
            elif send_dir == '3' or send_dir == '4':
                SendStep = 'r' + send_step
                ser.write(SendStep.encode('utf-8'))
            else:
                print('输错了')
                ser.write('hahaha error!!!'.encode('utf-8'))
            print('发送数据:' + send_step)
        else:
            print('先打开串口')
        print('set_step')
    def set_air(self):
        global serialPort1, ser
        if self.pushButton.text() == '关闭1' and serialPort1 != None:
            send_air = self.textEdit_4.toPlainText()
            print(send_air)
            SendAir='s'+send_air
            ser.write(SendAir.encode('UTF-8'))
            print('发送气压数据:' + send_air)
        else:
            print('先打开串口')
        print('set_speed')
    def port_change2(self,text):
        global serialPort2
        serialPort2=text
        print('串口号：',serialPort2)
        ser2.port=serialPort2
        print('port_change2')
    def baud_change2(self,text):
        global baudRate2
        baudRate2=int(text)
        print('波特率',baudRate2)
        print('baud_change2')
    def connect_btu2(self):
        global ser2, serialPort2, baudRate2, com_list2
        com_list2 = get_com_list()
        if com_list2 != []:
            if serialPort2 != None:
                ser2.port=serialPort2
                ser2.baudrate = baudRate2
                if self.pushButton_6.text() == '连接2':
                    ser2.open()
                    self.timer2.start(timer_value)
                    self.pushButton_6.setText('关闭2')
                    print('串口2已连接')
                else:
                    ser2.close()
                    self.timer2.stop()
                    self.pushButton_6.setText('连接2')
                    print('串口2已关闭')
            else:
                myWin.comboBox_3.clear()
                for i in range(len(com_list2)):
                    myWin.comboBox_3.addItem(com_list2[i])
                serialPort2 = com_list2[0]
        else:
            serialPort2 = None
            myWin.comboBox_3.clear()
        print('connect_btu2')
    def set_sensor(self):
        global serialPort2, ser2,receve_flag
        if self.pushButton_6.text() == '关闭2' and serialPort2 != None:
            send_sensor = self.textEdit_5.toPlainText()
            ss=bytes.fromhex(send_sensor)
            print(send_sensor)
            ser2.write(ss)
            time.sleep(0.1)
            receve_flag=True
            send_r_s_periodically()
        else:
            print('先打开串口')
        print('set_sensor')
    def my_loop(self):
        global ser,auto_mode
        while auto_mode:
            print('data2',data2)
            print('data5',data5)
            if 'done' in data2:
                ser.write('t'.encode('utf-8'))
            if float(data5) < -1:
                ser.write('z'.encode('utf-8'))
            time.sleep(0.1)
            if end_flag:
                break
    def set_auto(self):
        global ser,auto_mode
        ser.write('t'.encode('utf-8'))
        auto_mode = True
        thread = threading.Thread(target=self.my_loop)
        thread.daemon=True
        thread.start()
        auto_mode=True
app=QApplication(sys.argv)
myWin=MyWindow()
myWin.show()
baudRate1=9600
baudRate2=9600
timer_value=50
ser=serial.Serial(timeout=0.05)
ser2=serial.Serial(timeout=0.05)
com_list=get_com_list()
com_list2=get_com_list()
if com_list != []:
    for i in range(len(com_list)):
        myWin.comboBox.addItem(com_list[i])
        myWin.comboBox_3.addItem(com_list2[i])
    serialPort1=com_list[0]
    serialPort2=com_list2[0]
else:
    print('我找不到串口')
sys.exit(app.exec_())
timer_thread = threading.Thread(target=send_r_s_periodically)
timer_thread.start()
