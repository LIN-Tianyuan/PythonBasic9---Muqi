# 导包
import pygame
import sys

# 初始化
pygame.init()

# 设置窗口
screen = pygame.display.set_mode((400, 400))
# 大屏的背景色
screen.fill((156, 156, 156))
# 设置标题
pygame.display.set_caption("My first game")

# 字体
f = pygame.font.SysFont('Arial', 50)

# RGB: Red Green Blue (0~255)
# (0, 0, 0) 黑色
#
# 生成文字
text = f.render("Happy game", True, (255, 182, 193), (128, 0, 128))
# 获取一个长方形
text_rect = text.get_rect()
# 放在中间
text_rect.center = (200, 200)
# 把文字放到屏幕上
# 把文字画面 text，画到 text_rect 指定的位置
screen.blit(text, text_rect)
while True:
    # 获取事件
    for event in pygame.event.get():
        # 当点击上方的x键时，检测到退出事件
        if event.type == pygame.QUIT:
            # 退出游戏
            pygame.quit()
            # 清空进程
            sys.exit()
    # 刷新页面，更新内容
    pygame.display.flip()

# display: 创建窗口，更新画面
# time: 控制帧率和计时
# fps: frames per second
# Clock(): 创建时钟对象
# tick(): 限制帧率
# draw: 绘制矩形、圆、线等基本图形