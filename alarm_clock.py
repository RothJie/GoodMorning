import time
import winsound
from playsound3 import playsound
import json

# 设定闹钟时间
def set_alarm(alarm_time):
    while time.time() < time.mktime(time.strptime(alarm_time, "%Y-%m-%d %H:%M:%S")):
        time.sleep(1)
    # 触发闹钟
    winsound.Beep(500, 1000)

# 定时播放音乐
def play_music():
    # 音乐文件路径
    music_path = ".\ConfigFile\\path_to_your_music.mp3"
    # 播放音乐
    playsound(music_path)

def get_alarm_time():
    with open(".\ConfigFile\\alarmtime.json", "r", encoding="utf-8") as f:
        alarm_time = json.load(f)
        return alarm_time['alarmTime']

# 主函数
def main():
    set_alarm(get_alarm_time())
    # 定时播放音乐
    play_music()



if __name__ == '__main__':
    main()
    # print(get_alarm_time())
    # current_time = datetime.datetime.now()
    # print(time.time())
    # set_alarm(get_alarm_time())



