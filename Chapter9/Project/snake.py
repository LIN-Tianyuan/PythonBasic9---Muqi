import pygame
import sys
import random

# 初始化
pygame.init()

# 蛇的移动速度
snake_speed = 30

# 窗口大小
window_x = 720
window_y = 480

# 颜色
green = (0, 255, 0)
white = (255, 255, 255)

game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake")

# FPS（每秒帧数)控制器
fps = pygame.time.Clock()
# 初始化蛇的位置
snake_position = [100, 50]
# 初始化蛇的身体（前4块）
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

fruit_position_x = random.randint(0, 720)
fruit_position_y = random.randint(0, 480)
fruit_position = [fruit_position_x, fruit_position_y]
fruit_spawn = True

# 初始方向
direction = 'RIGHT'
change_to = direction




while True:
    # 游戏每一帧都会清空屏幕，然后重新绘制
    for event in pygame.event.get():
        # 判断是不是键盘按下事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # 让蛇往上走
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 已经按了上键 但是同时此时的方向不能为下
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] = snake_position[1] - 10
    if direction == 'DOWN':
        snake_position[1] = snake_position[1] + 10
    if direction == 'LEFT':
        snake_position[0] = snake_position[0] - 10
    if direction == 'RIGHT':
        snake_position[0] = snake_position[0] + 10

    snake_body.insert(0, list(snake_position))

    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        fruit_spawn = False
    else:
        snake_body.pop()

    game_window.fill((0, 0, 0))

    # 画蛇
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    # 画水果
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    # 刷新屏幕
    pygame.display.flip()

    # 每秒帧数/刷新率
    fps.tick(snake_speed)

