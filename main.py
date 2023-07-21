import pygame
import random

pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Определение размеров окна и ячейки
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
CELL_SIZE = 20

# Определение скорости змейки
SNAKE_SPEED = 10

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Змейка")

# Функция для вывода сообщения на экран
def message(msg, color, y_displace=0):
    font = pygame.font.SysFont(None, 30)
    text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + y_displace))
    window.blit(text, text_rect)

# Функция для отрисовки змейки
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(window, GREEN, [block[0], block[1], CELL_SIZE, CELL_SIZE])

# Главная функция для игры
def game_loop():
    snake_body = []
    snake_length = 1

    # Позиция и направление змейки
    snake_x, snake_y = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
    snake_x_change, snake_y_change = 0, 0

    # Позиция и размер еды
    food_x, food_y = round(random.randrange(0, WINDOW_WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE, round(
        random.randrange(0, WINDOW_HEIGHT - CELL_SIZE) / CELL_SIZE
    ) * CELL_SIZE

    # Основной цикл игры
    game_exit = False
    game_over = False
    while not game_exit:
        while game_over:
            window.fill(WHITE)
            message("Игра окончена! Нажмите Q для выхода или C для начала новой игры.", RED, y_displace=-50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -CELL_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = CELL_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -CELL_SIZE
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = CELL_SIZE
                    snake_x_change = 0

        # Обновление позиции змейки
        snake_x += snake_x_change
        snake_y += snake_y_change

        # Рисование фона
        window.fill(WHITE)

        # Рисование еды
        pygame.draw.rect(window, RED, [food_x, food_y, CELL_SIZE, CELL_SIZE])

        # Добавление новых координат в тело змейки
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        # Проверка на столкновение с краем окна или с самой собой
        for block in snake_body[:-1]:
            if block == snake_head:
                game_over = True

        if (
            snake_x < 0
            or snake_x >= WINDOW_WIDTH
            or snake_y < 0
            or snake_y >= WINDOW_HEIGHT
        ):
            game_over = True

        # Проверка на поедание еды
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = round(random.randrange(0, WINDOW_WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE, round(
                random.randrange(0, WINDOW_HEIGHT - CELL_SIZE) / CELL_SIZE
            ) * CELL_SIZE
            snake_length += 1

        # Отрисовка змейки
        draw_snake(snake_body)

        # Обновление экрана
        pygame.display.update()

        # Установка скорости змейки
        pygame.time.Clock().tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Запуск игры
game_loop()
