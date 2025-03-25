import pygame
import random

pygame.init()


WIDTH, HEIGHT, CELL = 400, 400, 20
speed, level, score = 10, 1, 0


BLACK, GREEN, RED, WHITE = (0, 0, 0), (0, 255, 0), (255, 0, 0), (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
snake = [(5, 5)]
direction = (1, 0)

def new_food():
    while (pos := (random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))) in snake:
        pass
    return pos

food = new_food()
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1): direction = (0, -1)
            if event.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
            if event.key == pygame.K_LEFT and direction != (1, 0): direction = (-1, 0)
            if event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1, 0)
    
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if new_head in snake or not (0 <= new_head[0] < WIDTH // CELL and 0 <= new_head[1] < HEIGHT // CELL):
        break
    
    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        food = new_food()
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()
    
    for seg in snake:
        pygame.draw.rect(screen, GREEN, (seg[0] * CELL, seg[1] * CELL, CELL, CELL))
    pygame.draw.rect(screen, RED, (food[0] * CELL, food[1] * CELL, CELL, CELL))
    
    text = pygame.font.Font(None, 30).render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
