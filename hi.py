import pygame
import random

# 初始化Pygame
pygame.init()

# 设置游戏窗口
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇")

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 定义蛇和食物的大小
snake_size = 20
food_size = 20

# 定义游戏时钟
clock = pygame.time.Clock()

# 定义字体
font = pygame.font.SysFont(None, 50)

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, GREEN, [x, y, snake_size, snake_size])

def message(msg, color):
    text = font.render(msg, True, color)
    window.blit(text, [width/2 - text.get_width()/2, height/2 - text.get_height()/2])

def game_loop():
    game_over = False
    game_close = False

    # 初始化蛇的位置
    x1 = width / 2
    y1 = height / 2

    # 初始化蛇的移动
    x1_change = 0
    y1_change = 0

    # 初始化蛇的长度
    snake_list = []
    length_of_snake = 1

    # 随机生成食物的位置
    foodx = round(random.randrange(0, width - food_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - food_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(BLACK)
            message("你输了！按Q退出或C重新开始", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        # 检查是否撞到边界
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)
        pygame.draw.rect(window, RED, [foodx, foody, food_size, food_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # 检查是否撞到自己
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_list)
        pygame.display.update()

        # 检查是否吃到食物
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - food_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - food_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(10)

    pygame.quit()
    quit()

game_loop()
