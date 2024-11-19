import sys
import math
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from datetime import datetime
import pytz


class ClockWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

        # 用于记录鼠标按下时的位置
        self.dragPosition = None

    def init_ui(self):
        layout = QVBoxLayout()

        self.setLayout(layout)
        self.setWindowTitle("PyQt5挂钟样式时钟")
        self.resize(800, 800)

        # 设置窗口为始终在最顶层、无边框且背景透明
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 将窗口移动到屏幕正中间
        screen_geometry = QApplication.desktop().screenGeometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = (screen_geometry.height() - self.height()) / 2
        self.move(int(x), int(y))

        # 创建定时器，每隔1秒更新时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 获取窗口中心坐标
        center_x = self.width() // 2
        center_y = self.height() // 2

        # 绘制时钟外圆
        painter.setPen(QPen(QColor(0, 0, 0), 5))
        painter.drawEllipse(center_x - 201, center_y - 201, 402, 402)

        # 绘制中心点
        painter.setPen(QPen(QColor(0, 0, 0), 5))
        painter.drawPoint(center_x, center_y)

        l0 = 190
        l1 = 200
        l3 = 192
        l4 = 170
        for i in range(60):
            angle = math.pi / 30 * i
            x = int(center_x + l0 * math.sin(angle))
            y = int(center_y - l0 * math.cos(angle))

            m = int(center_x + l1 * math.sin(angle))
            n = int(center_y - l1 * math.cos(angle))

            p = int(center_x + l3 * math.sin(angle))
            q = int(center_y - l3 * math.cos(angle))

            e = int(center_x + l4 * math.sin(angle))
            o = int(center_y - l4 * math.cos(angle))

            if i % 5 == 0:
                painter.setPen(QPen(QColor(138, 94, 20), 7))
                painter.drawLine(x, y, m, n)
                font_ = QFont("Arial", 12)
                painter.setFont(font_)
                painter.setPen(QPen(QColor(0, 0, 0), 4))
                painter.drawText(e - 5, o, '12' if str(int(i / 5)) == '0' else str(int(i / 5)))

            else:
                painter.setPen(QPen(QColor(0, 0, 0), 4))
                painter.drawLine(p, q, m, n)


        # 获取当前北京时间
        beijing_tz = pytz.timezone('Asia/shanghai')
        current_time = datetime.now(beijing_tz)
        hour = current_time.hour % 12
        minute = current_time.minute
        second = current_time.second

        # 绘制时针
        hour_angle = (hour + minute / 60 + second / 3600) * (math.pi / 6)
        self.draw_hand(painter, hour_angle, 50, 5, handel_type='hour')

        # 绘制分针
        minute_angle = (minute + second / 60) * (math.pi / 30)
        self.draw_hand(painter, minute_angle, 150, 4, "minute")

        # 绘制秒针
        second_angle = second * (math.pi / 30)
        self.draw_hand(painter, second_angle, 200, 2, "second")

    def draw_hand(self, painter, angle, length, width, handel_type: str):
        center_x = self.width() // 2
        center_y = self.height() // 2

        end_x = center_x + length * math.sin(angle)
        end_y = center_y - length * math.cos(angle)

        color_li = [(251, 146, 60), (6, 146, 207), (30, 31, 34)]
        if handel_type == 'second':
            painter.setPen(QPen(QColor(*color_li[0]), width))
        if handel_type == 'minute':
            painter.setPen(QPen(QColor(*color_li[1]), width))
        if handel_type == 'hour':
            painter.setPen(QPen(QColor(*color_li[2]), width))

        painter.drawLine(int(center_x), int(center_y), int(end_x), int(end_y))

    def update_clock(self):
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.dragPosition is not None:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.dragPosition is not None:
            self.dragPosition = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock_widget = ClockWidget()
    clock_widget.show()
    sys.exit(app.exec_())