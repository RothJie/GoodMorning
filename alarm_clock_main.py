import time
import json
from playsound3 import playsound
from abc import ABCMeta,abstractmethod
from alarm_clock_of_music import AlarmMusic

class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
       pass

    @abstractmethod
    def alarm(self):
        pass

    def run(self):
        self.start()
        while time.time() < time.mktime(time.strptime(AlarmMusic.get_alarm_time(), "%Y-%m-%d %H:%M:%S")):
            self.repaint()
        else:
            self.alarm()
        self.stop()

class MyWindow(Window):
    def __init__(self,msg):
        self.msg = msg

    def start(self):
        print('闹钟唤醒程序已启动')

    def stop(self):
        print('闹钟已关闭')

    def alarm(self):
        print('播放音乐')
        a = AlarmMusic().play_music()

    def repaint(self):
        time.sleep(60)
        print('休息一分钟！！')

MyWindow('闹钟').run()