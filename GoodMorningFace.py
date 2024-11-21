
class Clock:
    def run(self):
        print('闹钟运行')

    def stop(self):
        print('闹钟停止工作')

class Voice:
    def run(self):
        print('语音模块启动')

    def stop(self):
        print('语音模块停止')


class Message:
    def run(self):
        print('开始收集相关的信息')

    def stop(self):
        print('信息收集完毕')

class SysGoodMorning:
    def __init__(self):
        self.clock = Clock()
        self.voice = Voice()
        self.message = Message()

    def run(self):
        self.clock.run()
        self.voice.run()
        self.message.run()

    def stop(self):
        self.clock.stop()
        self.voice.stop()
        self.message.stop()

if __name__ == '__main__':
    GoodMorning = SysGoodMorning()
    GoodMorning.run()
    GoodMorning.stop()