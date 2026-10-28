import pygame
import sys

pygame.init()

# 窗口大小
window_x = 720
window_y = 480

# 颜色
green = (0, 255, 0)

# 初始化蛇的位置
snake_position = [100, 50]
# 初始化蛇的身体（前4块）
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake")

while True:
    # 游戏每一帧都会清空屏幕，然后重新绘制
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
