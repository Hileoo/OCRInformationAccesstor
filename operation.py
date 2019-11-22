import subprocess
import time
import OCR
import random

count = 0

class Screenshot():
    def __init__(self):
        connect = subprocess.Popen("adb devices", stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = connect.communicate()

    def screen(self, cmd):
        screenExecute = subprocess.Popen(str(cmd), shell=True)


    def saveComputer(self, cmd):
        screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

def screenshot(localDir, index):
    cmd1 = r"adb shell /system/bin/screencap -p /storage/emulated/0/DCIM/Screenshots/%d.png"%(index)
    cmd2 = r"adb pull /storage/emulated/0/DCIM/Screenshots/%d.png %s%d.png"%(index, localDir, index)
    screen = Screenshot()
    screen.screen(cmd1)
    screen.saveComputer(cmd2)


def click(x, y, t):
    cmd = "adb shell input tap %d %d"%(x,y)
    subprocess.Popen(str(cmd), shell=True)
    time.sleep(t)

def swipe(start, end, t):
    global count
    cmd = "adb shell input swipe 500 %d 500 %d 2000"%(start, end)
    subprocess.Popen(str(cmd), shell=True)
    time.sleep(3)
    for i in range(6):
        click(600, 445 + i * 270, 2+random.random())
        click(540, 550, 4+random.random())
        count = count + 1
        screenshot(r"./picture/", count)
        time.sleep(2+random.random())
        OCR.ocr_function(("picture/%d.png"%(count)), count)
        back()
        time.sleep(1+random.random())
        back()
        time.sleep(1+random.random())
    time.sleep(1+random.random())

def back():
    cmd = "adb shell input keyevent 4"
    subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

def home():
    cmd = "adb shell input keyevent 3"
    subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
