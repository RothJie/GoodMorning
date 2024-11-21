from playsound3 import playsound
import json

class AlarmMusic:
    # 定时播放音乐
    def play_music(self):
        # 音乐文件路径
        music_path = ".\ConfigFile\\path_to_your_music.mp3"
        # 播放音乐
        playsound(music_path)

    @classmethod
    def get_alarm_time(self):
        with open(".\ConfigFile\\alarmtime.json", "r", encoding="utf-8") as f:
            alarm_time = json.load(f)
            return alarm_time['alarmTime']


if __name__ == '__main__':
    a = AlarmMusic()
    a.play_music()
    print(AlarmMusic.get_alarm_time())
